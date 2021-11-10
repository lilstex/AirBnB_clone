#!/usr/bin/python3
"""
Command interpreter for AirBnB project

"""
from cmd import Cmd
import argparse

class MyPrompt(Cmd):
    prompt = '>>> '
    intro = ' Welcome to AirBnB CLI!\n Type "?" or "help" to list commands \n Type "exit" or "x" or "q" to exit the CLI'
    
    def do_exit(self, input):
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
        '''....................'''
        pass

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
    MyPrompt().cmdloop()