from tasks import storage
from tasks import export


def handle_action():
    user_input = input('What action do you want to take?\n'
                       '1 - add task\n'
                       '2 - remove task\n'
                       '3 - mark as done\n'
                       '4 - show tasks\n'
                       '5 - save tasks')
    print(user_input)
    match user_input:
        case '1':
            name = input("Enter task name: ")
            storage.add_task(name)

        case '2':
            index = input('Enter task index: ')
            if index.isdigit() == False:
                index = -1
            else:
                index = int(index)
            storage.remove_task(index)
        case '3':
            index = input('Enter task index: ')
            is_complete = input('mark task comlete? (y/n) y-default: ')
            if len(is_complete) != 0:
                is_complete = is_complete == 'y'
            else:
                is_complete = True

            if index.isdigit() == False:
                index = -1
            else:
                index = int(index)
            storage.mark_task_completed(index, is_complete)
        case '4':
            storage.print_tasks()
        case '5':
            file_name = input('Enter file name[default sample]: ')
            if file_name.strip() == "":
                file_name = "sample"

            export.save_to_file(storage.get_all_tasks(), file_name)
        case _:
            print('Not found')


def handle_interrupt(interrupt) -> bool:
    if KeyboardInterrupt == interrupt:
        user_input = input('\nDo you want to exit(y/n)?')
        return user_input == 'y'
