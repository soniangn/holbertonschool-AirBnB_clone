#!/usr/bin/python3
"""The console"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interprete"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        "command to exit the program"
        return True

    def emptyline(self):
        pass

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def do_create(self, line):
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
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
