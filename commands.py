#!/usr/bin/python3
from cmd import Cmd

class MyPrompt(Cmd):
    prompt = 'shell> '
    intro = 'Welcome to shell! Type ? to list commands'
    
    def do_exit(self, input):
        '''Exit the command interpreter. Shorthand type x or q'''
        print('Goodbye from the shell');
        return True

    def default(self, input):
        if input == 'x' or input == 'q':
            return self.do_exit(input)

        print('Default: {}'.format(input))

    def help_EOF(self):
        print('Exit the command interpreter using CTRL-D')

    do_EOF = do_exit

    def do_add(self, type, value):
        '''....................'''
        self.type = type
        self.value = value

    def __str__(self):
        pass

    


if __name__ == '__main__':
    MyPrompt().cmdloop()