from aica_graph.utils.state import AicaGraphState

async def aica_intervent_classifier_node(state: AicaGraphState) -> str:
    if state["isCorrespondenceBetweenUsersBool"] == False and state["isAicaInCopyBool"] == False:
        return "action"
    else:
        return "_end"