from typing import List, NamedTuple, Optional

import db


def delTaskAll() -> None:
    db.dellAll()


def add_Task(raw_message: str) -> None:
    db.addTask(raw_message)


def delTask(row_id: int) -> None:
    db.delTask(row_id)


def editTaskOk(row_id: int) -> None:
    db.editTaskOk(row_id)


class Task(NamedTuple):
    id: Optional[int]
    text: str
    ok: bool


def getTasks() -> List[Task]:
    tasks = db.getTasks()
    text = [Task(id=row[0], text=row[1], ok=row[2])
            for row in tasks]
    return text


if __name__ == '__main__':
    print(getTasks())


