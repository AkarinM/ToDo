from factory import task_factory
from task import Task, State
from datetime import datetime


class Controller:
    def __init__(self):
        self.task_list = []

    def get_task_list(self):
        return self.task_list if len(self.task_list) > 0 else None

    def add_task(self, name, date_str, description):
        plan_dttm = datetime.strptime(date_str, 'YYYY-MM-DD HH:MM:SS')

        state = State.TODO

        try:
            task = task_factory(name, plan_dttm, state, description)
        except Exception as e:
            return e

        self.task_list.append(task)

    def get_task_by_num(self, uni_num: int):
        ...

    def del_task(self, task: Task):
       ...

    def check_task_list(self) -> bool:
        return len(self.task_list) > 0

    @staticmethod
    def update_task(task: Task, name: str, plan_dttm, description: str = None):
        task.name = name
        task.plan_dttm = plan_dttm
        task.description = description

    def set_run_state(self, task: Task):
        self._change_state(task, State.RUN)

    def set_completed_state(self, task: Task):
        self._change_state(task, State.COMPLETED)

    @staticmethod
    def _change_state(task: Task, state: State):
        """
        Изменяет статус задачи
        :param state:
        :return:
        """

        task.state = state
