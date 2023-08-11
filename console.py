#!/usr/bin/python3
"""My console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB console"""

    def __init__(self):
        """instanciate the class"""
        super().__init__()
        self.prompt = '(hbnb) '

    def do_quit(self, _):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, _):
        """EOF command to exit the program"""
        exit()

    def emptyline(self):
        """Do nothing on an empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
