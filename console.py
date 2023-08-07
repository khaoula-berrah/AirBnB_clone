#!/usr/bin/env python3

import cmd


"""
    Module of console.

    console is an interpreter tool used to manage data of the project.

    USE:
    ----
        >>> ./console
        (hbnb)
"""


class console(cmd.Cmd):
    """
        Class of console.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
            emptyline - function that prints an empty line.
        """
        return super().emptyline()

    def do_quit(self, line):
        """
            do_quit - function that quits the interpreter.
        """
        return True


if __name__ == '__main__':
    interpreter = console()
    interpreter.cmdloop()
