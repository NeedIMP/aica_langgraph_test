import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import END, START, StateGraph
from langfuse import Langfuse
from langfuse.callback import CallbackHandler
from dotenv import load_dotenv
from aica_graph.nodes_dict import nodes, conditional_functions
from aica_graph.utils.state import AicaGraphState

load_dotenv()

os.environ["LANGFUSE_PUBLIC_KEY"] = os.getenv("LANGFUSE_PUBLIC_KEY")
os.environ["LANGFUSE_SECRET_KEY"] = os.getenv("LANGFUSE_SECRET_KEY")
os.environ["LANGFUSE_HOST"] = "https://cloud.langfuse.com"
os.environ["OPENAI_API_KEY"] = os.getenv("openai_api_key")

langfuse = Langfuse()
langfuse_callback_handler = CallbackHandler()

def build_the_graph_with_solver_prompt():
    langfuse_prompt = langfuse.get_prompt("solver_prompt")
    langchain_prompt = ChatPromptTemplate.from_template(langfuse_prompt.get_langchain_prompt())
    formatted_prompt = langchain_prompt.messages[0].prompt.template
    workflow = StateGraph(AicaGraphState)
    used_nodes = set()
    
    lines = formatted_prompt.strip().split("\n")
   
    for line in lines:
        if "->" in line:
            left, right = line.split("->")
            left = left.strip()
            right = right.strip()

            used_nodes.add(left)
            used_nodes.add(right)

            if left == "START":
                workflow.add_edge(START, right)
            elif right == "END":
                workflow.add_edge(left, END)
            elif "(" in left and ")" in left:
                node_name, condition = left.split(" (")
                condition = condition.replace(")", "").strip()

                if condition in conditional_functions:
                    condition_func = conditional_functions[condition]
                else:
                    raise ValueError(f"Condition function for '{condition}' not found.")
                
                conditions = {}
                for cond in right.split(","):
                    state, target = cond.split(":")
                    conditions[state.strip()] = target.strip()
                    used_nodes.add(target.strip())

                workflow.add_conditional_edges(node_name.strip(), condition_func, conditions)
            else:
                workflow.add_edge(left, right)
    
    for node_name in used_nodes:
        if node_name in nodes: 
            workflow.add_node(node_name, nodes[node_name])

    return workflow