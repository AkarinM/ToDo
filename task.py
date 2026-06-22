from enum import Enum


class State(Enum):
    TODO = 1  # сделать
    RUN = 2  # в работе
    COMPLETED = 3  # выполнена


class Task:
    """
    Класс, описывающий объект Задача
    """

    _max_uni_num: int = 0

    def __init__(self, uni_num, name: str, create_dttm, plan_dttm, state, description: str = None):
        self._uni_num = uni_num
        self._name = name
        self.create_dttm = create_dttm
        self.plan_dttm = plan_dttm
        self._state = state
        self.description = description

        Task.set_max_uni_num()

    @property
    def uni_num(self):
        return self._uni_num

    @uni_num.setter
    def uni_num(self, val: int):
        if val < 1:
            raise Exception('uni_num не может быть меньше 1')

        self._uni_num = val

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val: str):
        if val is None or val.strip() == '':
            raise Exception('name не может быть пустым')

        self._name = val

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, val: State):
        self._state = val

    @classmethod
    def get_next_uni_num(cls) -> int:
        """
        возвращает следующий номер задачи
        :return:
        """
        return cls._max_uni_num + 1

    @classmethod
    def set_max_uni_num(cls):
        cls._max_uni_num += 1
