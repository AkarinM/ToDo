from task import Task
from datetime import datetime


def task_factory(name: str, plan_dttm: datetime, state=None, description='') -> Task:
    """
    Фабрика для создания задачи
    :returns: задача
    """
    uni_num = Task.get_next_uni_num()

    create_dttm = datetime.now()

    task = Task(uni_num, name, create_dttm, plan_dttm, state, description)

    return task
