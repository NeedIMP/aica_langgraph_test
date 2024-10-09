from aica_graph.utils.state import AicaGraphState

async def aica_action_executer_node(state: AicaGraphState) -> AicaGraphState:
    aica_action_terminal_message= """Aica should intervene and take some action!!!"""

    return {"aica_action_terminal_message": aica_action_terminal_message}