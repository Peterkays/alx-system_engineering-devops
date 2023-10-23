#!/usr/bin/python3
"""This file defines the functioning of the HBnB console.
It controls all databases (create, modify and delete instances)
"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexa = split(arg[:brackets.span()[0]])
            lili = [i.strip(",") for i in lexa]
            lili.append(brackets.group())
            return lili
    else:
        lexa = split(arg[:curly_braces.span()[0]])
        lili = [i.strip(",") for i in lexa]
        lili.append(curly_braces.group())
        return lili


class HBNBCommand(cmd.Cmd):
    """This class defines the AirBnB command interpreter.

    Attributes:
        prompt (str): Prompts the command.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """When the line is empty, do nothing"""
        pass

    def default(self, arg):
        """When input is invalid, this becomes the default behavior of the cmd module."""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arrglyn = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arrglyn[1])
            if match is not None:
                command = [arrglyn[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(arrglyn[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        arrglyn = parse(arg)
        if len(arrglyn) == 0:
            print("** class name missing **")
        elif arrglyn[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arrglyn[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        arrglyn = parse(arg)
        obdct = storage.all()
        if len(arrglyn) == 0:
            print("** class name missing **")
        elif arrglyn[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arrglyn) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arrglyn[0], arrglyn[1]) not in obdct:
            print("** no instance found **")
        else:
            print(obdct["{}.{}".format(arrglyn[0], arrglyn[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        arrglyn = parse(arg)
        obdct = storage.all()
        if len(arrglyn) == 0:
            print("** class name missing **")
        elif arrglyn[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arrglyn) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arrglyn[0], arrglyn[1]) not in obdct.keys():
            print("** no instance found **")
        else:
            del obdct["{}.{}".format(arrglyn[0], arrglyn[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        arrglyn = parse(arg)
        if len(arrglyn) > 0 and arrglyn[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objlyn = []
            for obj in storage.all().values():
                if len(arrglyn) > 0 and arrglyn[0] == obj.__class__.__name__:
                    objlyn.append(obj.__str__())
                elif len(arrglyn) == 0:
                    objlyn.append(obj.__str__())
            print(objlyn)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        arrglyn = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arrglyn[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        arrglyn = parse(arg)
        obdct = storage.all()

        if len(arrglyn) == 0:
            print("** class name missing **")
            return False
        if arrglyn[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arrglyn) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arrglyn[0], arrglyn[1]) not in obdct.keys():
            print("** no instance found **")
            return False
        if len(arrglyn) == 2:
            print("** attribute name missing **")
            return False
        if len(arrglyn) == 3:
            try:
                type(eval(arrglyn[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arrglyn) == 4:
            obj = obdct["{}.{}".format(arrglyn[0], arrglyn[1])]
            if arrglyn[2] in obj.__class__.__dict__.keys():
                voltyp = type(obj.__class__.__dict__[arrglyn[2]])
                obj.__dict__[arrglyn[2]] = voltyp(arrglyn[3])
            else:
                obj.__dict__[arrglyn[2]] = arrglyn[3]
        elif type(eval(arrglyn[2])) == dict:
            obj = obdct["{}.{}".format(arrglyn[0], arrglyn[1])]
            for k, v in eval(arrglyn[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    voltyp = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = voltyp(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

