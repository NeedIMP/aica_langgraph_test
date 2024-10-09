from aica_graph.utils.nodes.action_executer_nodes import aica_action_executer_node
from aica_graph.utils.nodes.observer_nodes import (
    correspondence_between_users_observer_node,
    aica_in_copy_observer_node,
    end_and_return_state
)
from aica_graph.utils.nodes.classifier_nodes import aica_intervent_classifier_node

nodes = {
    "CorrespondenceBetweenUsersObserver": correspondence_between_users_observer_node,
    "AicaInCopyObserver": aica_in_copy_observer_node,
    "AicaActionExecuter": aica_action_executer_node,
    "EndAndReturnState": end_and_return_state
}

conditional_functions = {
    "determine_intervent": aica_intervent_classifier_node
}