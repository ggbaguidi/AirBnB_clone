#!/usr/bin/python3
"""My console"""

import cmd

import models
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

        class_ = self.parseline(args)[0]
        if class_ is None:
            print("** class name missing **")
        elif class_ not in self.existed_classes:
            print("** class doesn't exist **")
        else:
            new = eval(class_)()
            new.save()
            print(new.id)

    def do_show(self, args):
        """
        Prints the string representation of
        an instance based on the class name and id
        """

        class_ = self.parseline(args)[0]
        id_ = self.parseline(args)[1]

        if class_ is None:
            print("** class name missing **")
        elif class_ not in self.existed_classes:
            print("** class doesn't exist **")
        elif id_ == '':
            print("** no instance found **")
        else:
            obj = models.storage.all().get(class_+"."+id_)

            if obj is None:
                print('** no instance found **')
            else:
                print(obj)

    def do_destroy(self, arg):
        """
         Deletes an instance based on the class name and id
         (save the change into the JSON file)
        """
        class_ = self.parseline(arg)[0]
        id_ = self.parseline(arg)[1]

        if class_ is None:
            print("** class name missing **")
        elif class_ not in self.existed_classes:
            print("** class doesn't exist **")
        elif id_ == '':
            print("** instance id missing **")
        else:
            key = class_ + '.' + id_
            obj = models.storage.all().get(key)
            if obj is None:
                print('** no instance found **')
            else:
                del models.storage.all()[key]
                models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
