import importlib

class LiteVM:
    def __init__(self):
        self.commands = {}
        self.vars = {}

        # only built-in command is 'use'
        self.register_command('use', self.cmd_use)

    def register_command(self, name, func):
        self.commands[name] = func

    def cmd_use(self, args):
        """Dynamically load a library."""
        if not args:
            print("Usage: use <library>")
            return

        libname = args[0]
        try:
            lib = importlib.import_module(f'libs.{libname}')
            lib.register(self)
            # silently load library (no print)
        except ModuleNotFoundError:
            print(f"Library not found: {libname}")
        except Exception as e:
            print(f"Error loading library '{libname}': {e}")

    def execute(self, cmdname, args):
        if cmdname in self.commands:
            self.commands[cmdname](args)
        else:
            print(f"Unknown command: {cmdname}")
