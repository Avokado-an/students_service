from action_command import AddCommand, DeleteCommand, ReviewCommand, FilterCommand, ExitCommand
from input_command import AddCommandInput, DeleteCommandInput, ReviewCommandInput, FilterCommandInput


class ActionController:
    def __init__(self):
        self._commands = {}
        self._commands_input = {}
        self.register("1", AddCommand(), AddCommandInput())
        self.register("2", DeleteCommand(), DeleteCommandInput())
        self.register("3", ReviewCommand(), ReviewCommandInput())
        self.register("4", FilterCommand(), FilterCommandInput())
        self.register("5", ExitCommand(), None)

    def register(self, command_name, command, command_input):
        self._commands[command_name] = command
        self._commands_input[command_name] = command_input

    def execute(self, command_name):
        if command_name in self._commands.keys():
            args = self._commands_input[command_name].input()
            return self._commands[command_name].execute(args)
        else:
            command_name = "5"
            self._commands[command_name].execute(args=None)
