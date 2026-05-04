from check50 import *

class Hello(Check):
    @check()
    def exists(self):
        """hello.py exists"""
        self.require("hello.py")

    @check("exists")
    def compiles(self):
        """hello.py runs without error"""
        self.spawn("python3 hello.py").exit(0)

    @check("compiles")
    def correct_output(self):
        """prints Hello, World!"""
        self.spawn("python3 hello.py").stdout("Hello, World!\n", "Hello, World!")
