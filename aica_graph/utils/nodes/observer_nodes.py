from aica_graph.utils.state import AicaGraphState
import re

async def correspondence_between_users_observer_node(state: AicaGraphState) -> AicaGraphState:
    email_pattern = r'[\w\.-]+@[\w\.-]+'

    emails_in_from_user = re.findall(email_pattern, state["from_user"])
    emails_in_to_user = re.findall(email_pattern, state["to_user"])
    print(f"founded_emails_in_from_user: {emails_in_from_user}")
    print(f"founded_emails_in_to_user: {emails_in_to_user}")

    for email in emails_in_from_user:
        if email.endswith('@aica.bot'):
            return {"isCorrespondenceBetweenUsersBool": False}

    for email in emails_in_to_user:
        if email.endswith('@aica.bot'):
            return {"isCorrespondenceBetweenUsersBool": False}
    
    return {"isCorrespondenceBetweenUsersBool": True}

async def aica_in_copy_observer_node(state: AicaGraphState) -> AicaGraphState:
    email_pattern = r'[\w\.-]+@[\w\.-]+'

    emails_in_cc = re.findall(email_pattern, state["cc"])
    emails_in_bcc = re.findall(email_pattern, state["bcc"])
    print(f"founded_emails_in_cc: {emails_in_cc}")
    print(f"founded_emails_in_bcc: {emails_in_bcc}")

    for email in emails_in_cc:
        if email.endswith('@aica.bot'):
            return {"isAicaInCopyBool": True}

    for email in emails_in_bcc:
        if email.endswith('@aica.bot'):
            return {"isAicaInCopyBool": True}
    
    return {"isAicaInCopyBool": False}

# async def determine_mood(state: AicaGraphState) -> str:
#     return state["mood"]

async def end_and_return_state(state: AicaGraphState) -> AicaGraphState:
    return state