from tasks import storage
from tasks.cli import handle_action, handle_interrupt

def main():
    while True:
        try:
            handle_action()
           
        except KeyboardInterrupt:
            result = handle_interrupt(KeyboardInterrupt)
            if result == True:
                break
            else:
                continue
if __name__ == '__main__':

    # storage.add_task("pet the cat")
    # storage.add_task("drink beer")
    # storage.mark_task_completed(1,True)
    # print(storage.get_all_tasks())

    main()