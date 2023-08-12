#!/usr/bin/python3
"""My console"""

import cmd
import re
import shlex
import ast
from datetime import datetime

import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models.amenity import Amenity


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
        return True

    def do_EOF(self, _):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        return False

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
            print("** instance id missing **")
        else:
            obj = models.storage.all().get(class_+"."+id_)

            if obj is None:
                print('** no instance found **')
            else:
                print(obj)

    def do_destroy(self, args):
        """
         Deletes an instance based on the class name and id
         (save the change into the JSON file)
        """
        class_ = self.parseline(args)[0]
        id_ = self.parseline(args)[1]

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

    def do_all(self, args):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        class_ = self.parseline(args)[0]
        objs = models.storage.all()
        if class_ is None:
            print([str(objs[obj]) for obj in objs])
        elif class_ in self.existed_classes:
            keys = objs.keys()
            print([str(objs[key]) for key in keys
                   if key.startswith(class_)])
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.existed_classes:
            print("** class doesn't exist **")
            return
        try:
            args[1]
        except Exception:
            print("** instance id missing **")
            return
        objects_dict = models.storage.all()
        my_key = args[0] + "." + args[1]
        if my_key not in objects_dict:
            print("** no instance found **")
            return
        try:
            args[2]
        except Exception:
            print("** attribute name missing **")
            return
        try:
            args[3]
        except Exception:
            print("** value missing **")
            return
        if args[3]:
            setattr(objects_dict[my_key], args[2], args[3])
            my_obj = objects_dict[my_key]
            my_obj.updated_at = datetime.now()
            models.storage.save()

    def analyze_parameter_value(self, value):
        """
        Checks a parameter value for an update and
        analyse if is a string that needs conversion
        to a float or integer
        """
        if value.isdigit():
            return int(value)
        elif value.replace('.', '', 1).isdigit():
            return float(value)

        return value

    def default(self, arg):
        """
        This looks for whether the command entered has the syntax:
        "<class name>.<method name>" or not
        """
        if '.' in arg:
            split = re.split(r'\.|\(|\)', arg)
            class_ = split[0]
            method_name = split[1]

            if class_ in self.existed_classes:
                if method_name == 'all':
                    print(self.get_objects(class_))
                elif method_name == 'count':
                    print(len(self.get_objects(class_)))
                elif method_name == 'show':
                    class_id = split[2][1:-1]
                    self.do_show(class_ + ' ' + class_id)
                elif method_name == 'destroy':
                    class_id = split[2][1:-1]
                    self.do_destroy(class_ + ' ' + class_id)
                elif method_name == 'update':
                    update_data = split[2].split(",")
                    print(update_data)
                    if update_data is None or len(update_data) == 0:
                        print('** instance id missing **')
                    elif len(update_data) == 1:
                        print('** attribute name missing **')
                    elif len(update_data) == 2:
                        possible_dict = update_data[1]
                        print(update_data)
                        possible_dict = ast.literal_eval(possible_dict)

                        if isinstance(possible_dict, dict):
                            self.update_with_dict(class_,
                                                  update_data[0][1:-1],
                                                  possible_dict)
                        else:
                            print('** value missing **')
                    else:
                        class_id = update_data[0][1:-1]
                        attr_name = update_data[1][2:-1]
                        attr_value = update_data[2][1:]
                        other = ""
                        if len(update_data) > 3:
                            other = " ".join(update_data[3:])
                        self.do_update(" ".join([class_,
                                                 class_id, attr_name,
                                                 attr_value, other]))

    def update_with_dict(self, class_, class_id, dict_):
        """
        Update your command interpreter (console.py) to
        update an instance based on his ID with a dictionary:
        <class name>.update(<id>, <dictionary representation>)
        """

        attr_val = ""
        for key, val in dict_.items():
            attr_val = str(val)
            if isinstance(val, str):
                attr_val = '"{}"'.format(val)
            self.do_update(" ".join([class_,
                                     class_id, key, attr_val]))

    def get_objects(self, instance=''):
        """
        Gets the elements created by the console
        """
        objects = models.storage.all()

        if instance:
            keys = objects.keys()
            return [str(val) for key, val in objects.items()
                    if key.startswith(instance)]
        return [str(val) for key, val in objects.items()]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
