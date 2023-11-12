#!/usr/bin/python3
"""
creating the command line interpreter
"""
import sys
import cmd
from models import storage
from models.engine.known_objects import console_methods, classes


class HBNBCommand(cmd.Cmd):
    """
    Uses cmd methods to control the command interpreter
    """
    # The custom command interpreter prompt
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command for exiting the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command for exiting the program
        """
        self.non_interactive_check()
        return True

    @staticmethod
    def non_interactive_check():
        if sys.stdin.isatty() is False:
            print("")

    def emptyline(self):
        """
        Does nothing, re-prompts
        """
        self.non_interactive_check()
        pass

    def do_create(self, arguments):
        """
        creates a new instance of a class
        saves it (to the JSON file)
        and prints the id
        """
        self.non_interactive_check()
        args = self.arg_string_parse(arguments)
        if self.not_a_class(args["cls_name"]):
            return
        cls = classes[args["cls_name"]]
        new_obj = cls()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arguments):
        """
        prints the string representation of an instance
        based on the class name and id.
        """
        self.non_interactive_check()
        args = self.arg_string_parse(arguments)
        if self.not_a_class(args["cls_name"]):
            return
        if self.not_an_instance(args["cls_name"], args["inst_id"]):
            return
        key = "{}.{}".format(args["cls_name"], args["inst_id"])
        __objects = storage.all()
        print(__objects[key])

    def do_destroy(self, arguments):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        self.non_interactive_check()
        args = self.arg_string_parse(arguments)
        if self.not_a_class(args["cls_name"]):
            return
        if self.not_an_instance(args["cls_name"], args["inst_id"]):
            return
        key = "{}.{}".format(args["cls_name"], args["inst_id"])
        __objects = storage.all()
        del __objects[key]
        storage.save()

    def do_all(self, arguments):
        """
        prints all string representation of all instances
        based on the class name or not.
        """
        self.non_interactive_check()
        args = self.arg_string_parse(arguments)
        __objects = storage.all()
        print_list = []
        if args["cls_name"] is None:
            for obj in __objects:
                print_string = "{}".format(__objects[obj].__str__())
                print_list.append(print_string)

        else:
            if self.not_a_class(args["cls_name"]):
                return
            for obj in __objects:
                if obj.split(".")[0] == args["cls_name"]:
                    print_string = "{}".format(__objects[obj].__str__())
                    print_list.append(print_string)
            print(print_list)

    def do_update(self, arguments):
        """
        Update an instance based on the class name and id
        adds or updates attribute and saves the change into the JSON file
        """
        self.non_interactive_check()
        args = self.arg_string_parse(arguments)
        if self.not_a_class(args["cls_name"]):
            return
        if self.not_an_instance(args["cls_name"], args["inst_id"]):
            return
        if self.not_an_attribute(args["attr_name"]):
            return
        if self.not_a_value(args["attr_value"]):
            return
        key = "{}.{}".format(args["cls_name"], args["inst_id"])
        __objects = storage.all()
        setattr(__objects[key], args["attr_name"], args["attr_value"])

    @staticmethod
    def arg_string_parse(arguments):
        """
        splits input string of arguments
        """
        arg_list = arguments.split()
        args = {}
        if len(arg_list) >= 1:
            args["cls_name"] = arg_list[0]
        else:
            args["cls_name"] = None
        if len(arg_list) >= 2:
            args["inst_id"] = arg_list[1]
        else:
            args["inst_id"] = None
        if len(arg_list) >= 3:
            args["attr_name"] = arg_list[2]
        else:
            args["attr_name"] = None
        if len(arg_list) >= 4:
            args["attr_value"] = arg_list[3]
        else:
            args["attr_value"] = None
        return args

    @staticmethod
    def not_a_class(cls_name):
        """
        checks if the given class name argument
        prints error message if invalid or missing
        """
        if cls_name is None:
            print("** class name missing **")
            return True
        if cls_name not in classes:
            print("** class doesn't exist **")
            return True
        return False

    @staticmethod
    def not_an_instance(cls_name, inst_id):
        """
        checks if the given instance id argument
        prints error message if invalid or missing
        """
        if inst_id is None:
            print("** instance id missing **")
            return True
        key = "{}.{}".format(cls_name, inst_id)
        __objects = storage.all()
        if key not in __objects:
            print("** no instance found **")
            return True
        return False

    @staticmethod
    def not_an_attribute(attr_name):
        """
        checks if the given attribute name argument
        prints error message if misssing
        """
        if attr_name is None:
            print("** attribute name missing **")
            return True
        return False

    @staticmethod
    def not_a_value(attr_value):
        """
        checks if the given attrubute value argument
        prints error message if missing
        """
        if attr_value is None:
            print("** value missing **")
            return True
        return False

    def default(self, line):
        """
        The default behavior for unknown commands
        """

        try:
            # split input string based on the first . character
            arg_list = line.split('.', 1)
            # store the cls_name in a dictionary
            args = {}
            args["cls_name"] = arg_list[0]
            # split the remaining string based on the first ( character
            arg_list = arg_list[1].split('(', 1)
            args["method"] = arg_list[0]
            # split arguments such as attr_value, attr_name,
            # and instance id, when given
            if arg_list[1] == ")":
                arg_list = []
            else:
                # split off inst id and check whether arguments are dictionary
                arg_check = arg_list[1].split(', ', 1)
                if len(arg_check) > 1:
                    # send to special parsing method, if it's dictionary
                    if arg_check[1][0] == '{' and args["method"] == "update":
                        arg_string = args["cls_name"]
                        arg_string += " " + arg_check[0] + " " + arg_check[1]
                        self.update_dictionary(arg_string)
                        return
                    # keep parsing if not a dictionary
                    arg_string = arg_check[0]
                    if len(arg_check) > 1:
                        arg_string += ", " + arg_check[1]
                    arg_list = arg_string.split(', ')
                    # cuts off last ) character
                    arg_list[-1] = arg_list[-1][:-1]
                    # splicing first and last "" characters
                    if len(arg_list) >= 1:
                        args["inst_id"] = arg_list[0][1:-1]
                    else:
                        args["inst_id"] = None
                    if len(args_list) >= 2:
                        args["attr_name"] = arg_list[2][1:-1]
                    else:
                        args["attr_value"] = None

        except Exception as err:
            self.non_interactive_check()
            print("** Unknown syntax: " + line)
            return

        # verify method validity
        if args["method"] not in console_methods:
            print("** Unsupported method: " + args["method"] + " **")
            return
        if args["method"] == "count":
            method = getattr(self, args["method"])
            self.non_interactive_check()
            method(args["cls_name"])
            return

        method_str = "do_" + args["method"]
        method = getattr(self, method_str)

        arguments = args["cls_name"]
        if args["inst_id"] is not None:
            arguments += " " + args["inst_id"]
        if args["attr_name"] is not None:
            arguments += " " + args["attr_name"]
        if args["attr_value"] is not None:
            arguments += " " + args["attr_value"]

        method(arguments)

    @staticmethod
    def count(cls_name):
        """
        Returns the number of instances of cls_name
        """
        count = 0
        for id, instance in storage.all().items():
            if id.split('.')[0] == cls_name:
                count += 1
        print(count)

    def update_dictionary(self, arguments):
        """
        runs and parse update method for dictionary arguments
        """
        # spliting off the class name and instance id
        arg_list = arguments.split(" ", 2)
        args = {}
        args["ls_name"] = arg_list[0]
        args["inst_id"] = arg_list[1][1:-1]
        # chopping off dictionary {} and closing ) characters
        dict_string = arg_list[2][1: -2]
        # spliting the key/value pairs into list of strings
        dictionary = dict_string.split(", ")
        method = getattr(self, "do_update")
        # loop through each key/value pair
        for i in range(len(dictionary)):
            arguments = args["cls_name"] + " " + args["inst_id"] + " "
            dict_kv = dictionary[i].split(": ")
            args["attr_name"] = dict_kv[0][1:-1]
            if dict_kv[1][0] == "'" and dict_kv[1][-1] == "'":
                dict_kv[1] = dict_kv[1][1:-1]
            args["attr_value"] = dict_kv[1]
            arguments += args["attr_name"] + " " + args["attr_value"]
            # passing arguments to the update method
            method(arguments)
        return

if __name__ == "__main__":
    HBNBCommand().cmdloop()
