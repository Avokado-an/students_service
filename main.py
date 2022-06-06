from comand_controller.action_controller import ActionController

if __name__ == '__main__':
    continue_processing = True
    while continue_processing:
        command = raw_input("1 - add student, 2 - delete student, 3 - see students, 4 - filter students, other - exit\n")
        continue_processing = ActionController().execute(command)

