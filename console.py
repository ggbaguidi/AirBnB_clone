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

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        args = shlex.split(arg)
        args_size = len(args)
        if args_size == 0:
            print('** class name missing **')
        elif args[0] not in self.existed_classes:
            print("** class doesn't exist **")
        elif args_size == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            inst_data = models.storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            if args_size == 2:
                print('** attribute name missing **')
            elif args_size == 3:
                print('** value missing **')
            else:
                args[3] = self.analyze_parameter_value(args[3])
                try:
                    setattr(inst_data, args[2], args[3])
                    setattr(inst_data, 'updated_at', datetime.now())
                except AttributeError:
                    pass
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
