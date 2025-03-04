from typing import Dict, List, Union

admins: Dict[int, List[int]] = {}


def set(chat_id: int, admins_: List[int]):
    admins[chat_id] = admins_


def get(chat_id: int) -> Union[List[int], bool]:
    return admins[chat_id] if chat_id in admins else False
