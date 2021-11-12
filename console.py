#!/usr/bin/python3
"""
Command interpreter for AirBnB project

"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    class_types = ['Basemodel', 'User', 'Amenity', 'Place', 'Review', 'State', 'City']
    intro = ' Welcome to AirBnB CLI!\n Type "?" or "help" to list commands \n Type "quit" or "x" or "q" to exit the CLI'
    
    def do_quit(self, input):
        '''Exit the command interpreter. Shorthand type x or q'''
        print('Goodbye from the AirBnB CLI');
        return True

    def emptyline(self):
        '''This method is called when an empty line + ENTER is pressed, to prevent execution of previous commands'''
        pass

    def default(self, input):
        '''This method is called when an unknown command is sent'''
        if input == 'x' or input == 'q':
            return self.do_quit(input)
        else:
            print('"{}" : Unknown command. Type "help" or "?" for more information'.format(input))


    def do_EOF(self, line):
         '''Exit the command interpreter.'''
         print('Goodbye from the AirBnB CLI')
         return True


    def do_create(self, args):
        ''' This method creates an instance of a specified class, and stores
            the dictionary representation of the JSON in a file
        '''
        command = args.split(" ")
        if not command:
            print('** class name missing **')
        elif command[0] == HBNBCommand.class_types:
            print('** class doesn\'t exist **')
        else:
            # Looping through the class_types available in HBNBCommand class
            for cls in HBNBCommand.class_types:
                # Checkig if the class_type matches the !st command argument
                if cls == command[0]:
                   new_instance = '{}()'.format(command[0])
            new_instance.save()
            print(new_instance.id)


    def do_show(self, args):
        '''.............'''
        pass

    def do_update(self, args):
        '''............'''
        pass

    def do_destroy(self, args):
        '''...............'''
        pass

    def do_all(self, args):
        '''................'''
        pass



    


if __name__ == '__main__':
    HBNBCommand().cmdloop()