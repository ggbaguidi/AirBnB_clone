#!/usr/bin/python3
"""My console"""

import cmd

from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNB console"""

    def __init__(self):
        """instanciate the class"""
        super().__init__()
        self.prompt = '(hbnb) '
        self.existed_classes = ['BaseModel', 'User',
                                'State', 'City', 'Amenity',
                                'Place', 'Review']

    def do_quit(self, _):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, _):
        """EOF command to exit the program"""
        exit()

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel,
        saves it
        and print the id.
        """

        command = self.parseline(args)[0]
        if command is None:
            print("** class name missing **")
        elif command not in self.existed_classes:
            print("** class doesn't exist **")
        else:
            new = eval(command)()
            new.save()
            print(new.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
