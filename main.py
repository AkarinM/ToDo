from time import strftime, strptime

# from view import View
from control import Controller


controller = None


def no_tasks():
    while(True):
        print_menu_mini()

        action = False

        while (action is False):
            action = input_action('Введите действие: ')

            if check_action(action) is False:
                action = False

            action = int(action)

            if action == 1:
                add_task()
            elif action == 7:
                ...
            else:
                print('Не верное действие!')
                action = False

        break

def add_task():
    message = ''
    while(True):
        print(message + '\n')
        name = input_action('Введите название задачи: ')
        print('\n')
        date_str = input_action('Введите дату, на которую запланировать задачу: ')
        print('\n')
        description = input_action('Введите описание: ')

        message = controller.add_task(name, date_str, description)

        if message == '':
            print('Задача добавлена успешно!')
            break


def del_task():
    message = ''
    while (True):
        print(message + '\n')
        num = input_action('Введите номер задачи, которую хотите удалить. Чтобы отменить действие, введите 0: ')

        if check_action(num):
            if num == 0:
                break

            task = controller.get_task_by_num(int(num))

            if task is not None:
                controller.del_task(task)
                print('Задача удалена успешно!')
                break
            else:
                message = 'Задачи с таким номером не существует! Повторите ввод!'


def set_run_state():
    message = ''

    while (True):
        print(message + '\n')
        num = input_action('Введите номер задачи, которую хотите взять в работу. Чтобы отменить действие, введите 0: ')

        if check_action(num):
            if num == 0:
                break

            task = controller.get_task_by_num(int(num))

            if task is not None:
                controller.set_run_state(task)
                print('Задача взята в работу успешно!')
                break
            else:
                message = 'Задачи с таким номером не существует! Повторите ввод!'


def set_completed_state():
    message = ''

    while (True):
        print(message + '\n')
        num = input_action('Введите номер задачи, которую хотите выполнить. Чтобы отменить действие, введите 0: ')

        if check_action(num):
            if num == 0:
                break

            task = controller.get_task_by_num(int(num))

            if task is not None:
                controller.set_completed_state(task)
                print('Задача выполнена успешно!')
                break
            else:
                message = 'Задачи с таким номером не существует! Повторите ввод!'


def update_task():
    message = ''

    while(True):
        print(message + '\n')
        num = input_action('Введите номер задачи, которую хотите изменить. Чтобы отменить действие, введите 0: ')

        if check_action(num):
            if num == 0:
                break

            task = controller.get_task_by_num(int(num))

            if task is not None:
                print(f"Текущие данные:\n{task}")
                print("Введите новые значения (Enter — оставить без изменений):")
                name = input_action("Новое название: ")
                plan_dttm = input_action("Новая дата (ГГГГ-ММ-ДД): ")
                description = input_action("Новое описание: ")

                #TODO: реализовать проверку даты

                controller.update_task(task, name, plan_dttm, description)
                print("Задача обновлена.")
            else:
                message = 'Задачи с таким номером не существует! Повторите ввод!'



def check_action(action):
    try:
        int(action)
        return True
    except ValueError:
        return False


def print_list(tasks):
    print('\n'.join(tasks))


def print_menu():
    print("\n=== Менеджер задач ===")
    print("1. Создать задачу")
    print("2. Удалить задачу")
    print("3. Изменить задачу")
    print("4. Взять задачу в работу")
    print("5. Выполнить задачу")
    # print("6. Показать все задачи")
    print("7. Выход")
    print("======================")


def print_menu_mini():
    print("\n=== Нет задач ===")
    print("\n=== Менеджер задач ===")
    print("1. Создать задачу")
    print("7. Выход")
    print("======================")

def input_action(mess: str):
    return input(mess).strip()


if __name__ == '__main__':
    action = None

    controller = Controller()

    while(True):
        if controller.check_task_list():
            tasks = controller.get_task_list()
            print_list(tasks)
            print_menu()

            action = False

            while(action is False):
                action = input_action('Введите действие: ')

                if check_action(action) is False:
                    action = False

                action = int(action)

                if action == 1:
                    add_task()
                elif action == 2:
                    del_task()
                elif action == 3:
                    change_task
                elif action == 4:
                    set_run_state()
                elif action == 5:
                    set_completed_state()
                elif action == 7:
                    ...
        else:
            no_tasks()
