#!/usr/bin/python3
"""
Command interpreter for AirBnB project

"""
import cmd
import json
import re
import models
# Import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    '''The class for cmd'''
    prompt = '(hbnb)'
    instances = ['BaseModel', 'User', 'State', 'City',
                 'Amenity', 'Place', 'Review']
    
    def do_quit(self, input):
        '''Exit the command interpreter. Shorthand type x or q'''
        print('Goodbye from the AirBnB CLI');
        return True

    def emptyline(self):
        '''This method is called when hitting enter so that previous command does not occur'''
        pass

    def default(self, input):
        if input == 'x' or input == 'q':
            return self.do_exit(input)
        else:
            print('"{}" : Unknown command. Type "help" or "?" for more information'.format(input))


    def do_EOF(self, line):
         '''Exit the command interpreter.'''
         print('Goodbye from the AirBnB CLI')
         return True

    
    def do_create(self, args):
        '''Creates a new instance of BaseModel'''
        args = arg.split()

        if len(args) < 1:
            print('** class name missing **')
        elif arg in self.instances:
            new_obj = eval(arg + '()')
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

            
    def do_show(self, args):
        '''Prints the string representation of
        an instnace based on the class name
        '''
        args = arg.split()
        if len(args) < 1:
            print*('** Missing class name **')
        elif args[0] not in self.instances:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            all_objects = sotrage.all()
            if key in all_objects:
                print(all_objects[key])
            else:
                print('** no instance found **')
            

    def do_update(self, args):
        '''Updates an instance based on the class name
        and id by adding or updating an attribute
        
        Args:
            line(args): receives the coomands:
            <class name> <id> <attribute name> "<attribute value>"
            Example: 'update User 1234-1234-1234 my_name "Jon"'
        '''
    
        args = line.split()
        all_objects = storage.all()

        if len(args) == 0:
            print('**Missing class name**')
        elif args[0] not in self.instances:
            print("** class doesn't exist**")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            if key in all_objects:
                if len(args) < 3:
                    print('** attribute name missing **')
                elif len(args) < 4:
                    print('** value missing **')
                else:
                    obj_dict = all_objects[key].to_dict()
                    my_obj = all_objects[key]
                    if args[2] in obj_dict:
                        cast = type(my_obj.args[3])
                        cast(args[3])
                    setattr(my_obj, args[2], args[3])
                    my_obj.save()
            else:
                print('** no instance found **')
    def do_destroy(self, args):
        '''Deletes an instance based on the class name and id'''
        args = args.split()
        all_objects = storage.all()

        if len(args) < 1:
            print('** Missing class name **')
        elif args[0] not in self.instances:
            print("** classs doesn't exist**")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            if key in all_objects:
                del all_objects[key]
                storage.save()
            else:
                print('** no instance found **')
                
    def do_all(self, args):
        '''
        Prints all representation of all instances
        based on the class name
        '''
        list_instan = []
        args = arg.split()
        all_objects = storage.all()
        if len(args) == 0:
            for key in all_objects:
                list_instan.append(all_objects[key].__str__())
            print(list_instan)
        else:
            if args[0] in self.instances:
                for key in all_objects:
                    if args[0] in key:
                        list_instan.append(all_objects[key].__str__())
                        print(list_instan)
            else:
                print("** class doesn't exist**") 



    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
