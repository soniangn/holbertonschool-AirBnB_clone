#!/usr/bin/python3
"""The console"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interprete"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Create a new instances """
        arg = line.split(" ")
        if arg[0] == "":
            print("** class name missing **")
        else:
            if arg[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                new_inst = BaseModel()
                new_inst.save()
                print(new_inst.id)

    def do_show(self, line):
        """Print instances"""
        arg = line.split(" ")
        if arg[0] == "":
            print('** class name missing **')
        elif len(arg) == 1:
            print('** instance id missing **')
        else:
            if arg[0] == "BaseModel":
                try:
                    storage_all = storage.all()
                    obj = arg[0] + "." + arg[1]
                    instance = storage_all[f"{obj}"]
                    print(instance)
                except KeyError:
                    print('** no instance found **')
            else:
                print('** class doesn\'t exist **')

    def do_destroy(self, line):
        """Deletes an instance"""
        arg = line.split(" ")
        print(arg)
        if arg[0] == "":
            print("** class name missing **")
        else:
            if arg[0] != "BaseModel":
                print("** class doesn\'t exist **")
            elif len(arg) == 1:
                print("** instance id missing **")
            else:
                all_objs = storage.all()
                obj = arg[0] + "." + arg[1]
                if obj in all_objs.keys():
                    del all_objs[obj]
                    storage.save()
                else:
                    print(obj)
                    print("** no instance found **")

    def do_all(self, line):
        """Print all instances"""
        arg = line.split(" ")
        list = []
        storage_all = storage.all()
        if arg[0] == "":
            print(storage_all)
        else:
            try:
                eval(arg[0])
                for obj in storage_all:
                    key = obj.split('.')
                    if key[0] == arg[0]:
                        list.append(str(storage_all[obj]))
                print(list)
            except NameError:
                print('** class doesn\'t exist **')

    def do_update(self, line):
        arg = line.split(" ")
        all_objs = storage.all()

        if arg[0] == "":
            print("** class name missing **")
        else:
            if arg[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(arg) == 1:
                print("** instance id missing **")
            elif len(arg) == 2:
                print("** attribute name missing **")
            elif len(arg) == 3:
                print("** value missing **")
            else:
                obj = arg[0] + "." + arg[1]
                if obj not in all_objs:
                    print("** no instance found **")
                else:
                    all_objs[obj].__dict__[arg[2]] = eval(arg[3])
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()