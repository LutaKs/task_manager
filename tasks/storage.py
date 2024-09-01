
from typing import List, Tuple


_DB = []


def add_task(title: str) -> None:
    _DB.append({
        'title': title,
        'completed': False
    })


def remove_task(index: int) -> None:
    if index < 0 or index >= len(_DB):
        return
    del _DB[index]


def mark_task_completed(index: int, completed: bool) -> None:
    if index >= len(_DB) or index < 0:
        return
    _DB[index]['completed'] = completed


def get_all_tasks() -> List[Tuple[int, str, bool]]:
    return [
        (i, task['title'], task['completed'])
        for i, task in enumerate(_DB)
    ]


def print_tasks() -> None:
    print(get_all_tasks())
