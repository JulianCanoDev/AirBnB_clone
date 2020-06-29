#!/usr/bin/python3
"""
This is the main console command interpeter
"""
import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
