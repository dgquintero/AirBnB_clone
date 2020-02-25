#!/usr/bin/python3
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.
        If this method is not overridden, it repeats the last nonempty
        command entered."""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_EOF(self, line):
        """End of the file function"""
        return True

    def do_quit(self, line):
        """command that quit the program"""
        return True

    def do_create(self, line):
        """command that creates a new instance of BaseModel """
        if len((shlex.split(line))) == 0:
            print("** class name missing **")
            return False
        elif shlex.split(line)[0] in classes:
            instance = classes[shlex.split(line)[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id."""
        if len((shlex.split(line))) == 0:
            print("** class name missing **")
            return False
        elif shlex.split(line)[0] in classes:
            if len((shlex.split(line))) > 1:
                key = shlex.split(line)[0] + "." + shlex.split(line)[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if len((shlex.split(line))) == 0:
            print("** class name missing **")
            return False
        elif shlex.split(line)[0] in classes:
            if len((shlex.split(line))) > 1:
                key = shlex.split(line)[0] + "." + shlex.split(line)[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name."""
        obj = []
        if len((shlex.split(line))) == 0:
            for i in models.storage.all().values():
                obj.append(str(i))
            print("[\"" + ", ".join(obj) + "\"]")
        elif shlex.split(line)[0] in classes:
            for key in models.storage.all():
                if shlex.split(line)[0] in key:
                    obj.append(str(models.storage.all()[key]))
            print("[\"" + ", ".join(obj) + "\"]")
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ Updates an instance based on the class name
        and id by adding or updating attribute(save into the json_f)"""
        argu = shlex.split(line)
        if len(argu) == 0:
            print("** class name missing **")
        elif argu[0] in classes:
            if len(argu) > 1:
                ky = argu[0] + "." + argu[1]
                if ky in models.storage.all():
                    if len(argu) > 2:
                        if len(argu) > 3:
                            if type(argu[2]) is int:
                                try:
                                    argu[3] = int(argu[3])
                                except:
                                    argu[3] = 0
                            elif type(argu[2]) is float:
                                try:
                                    argu[3] = float(argu[3])
                                except:
                                    argu[3] = 0.0
                            setattr(models.storage.all()[ky], argu[2], argu[3])
                            models.storage.all()[ky].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
