
from typing import List, Tuple
from openpyxl import Workbook


def save_to_file(tasks: List[Tuple[int, str, bool]], file_name: str) -> None:
    wb = Workbook()
    # grab the active worksheet
    ws = wb.active
    ws.append(['Index', 'Title', 'Completed'])

    for task in tasks:
        ws.append(task)

    # Save the file
    wb.save(f'./out/{file_name}.xlsx')
