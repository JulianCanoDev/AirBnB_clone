#!/usr/bin/python3
"""
This is the main console command interpeter
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models import storage
import re


classes = {"BaseModel": BaseModel, "User": User}


class HBNBCommand(cmd.Cmd):
    """This is the entry point of our console"""
    prompt = '(hbnb) '

    def emptyline(self):
        """if is empty do nothing"""
        pass

    def do_quit(self, args):
        """Quit program"""
        return True

    def do_EOF(self):
        """End file"""
        return True

    def do_create(self, arg):
        """Create a new instance"""
        if not arg:
            print(" ** class name missing **")
        elif arg not in classes.keys():
            print("** class doesn't exist **")
        else:
            obj = classes[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """show instance"""
        if not arg:
            print(" ** class name missing **")
        elif arg.split()[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        else:
            msg = "{}.{}".format(arg.split()[0], arg.split()[1])
            objs = storage.all()
            if msg not in objs:
                print("** no instance found **")
            else:
                print(objs[msg])

    def do_destroy(self, arg):
        """Destroy a instance"""
        if not arg:
            print(" ** class name missing **")
        elif arg.split()[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        else:
            msg = "{}.{}".format(arg.split()[0], arg.split()[1])
            objs = storage.all()
            if msg not in objs:
                print("** no instance found **")
            else:
                del(objs[msg])
                storage.save()

    def do_all(self, arg):
        """Prints all string representation"""
        objs = storage.all()
        if not arg:
            my_list = []
            for key in objs:
                my_list.append(str(objs[key]))
            print(my_list)
        elif arg.split()[0] not in classes.keys():
            print("** class doesn't exist **")
        else:
            msg = arg.split()[0]
            my_list = [str(objs[key]) for key in objs if key.split(".")[0] == msg]

    def do_update(self, arg):
        """Update a instance"""
        if not arg:
            print(" ** class name missing **")
        elif arg.split()[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        else:
            msg = "{}.{}".format(arg.split()[0], arg.split()[1])
            objs = storage.all()
            if msg not in objs:
                print("** no instance found **")
            else:
                if len(arg.split()) < 3:
                    print("** attribute name missing **")
                elif len(arg.split() < 4):
                    print("** value missing **")
                else:
                    if arg.split()[3].isdecimal():
                        setattr(objs[msg], arg.split()[2], int(arg.split()[3]))
                    else:
                        try:
                            val = float(arg.split()[3])
                            setattr(objs[msg], arg.split()[2], val)
                        except ValueError:
                            val = re.split("( |\\\".*?\\\"|'.*?')", arg)
                            val = [w for w in val if w.strip()]
                            val = val[3].strip('"')
                            setattr(objs[msg], arg.split()[2], val)
                        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
