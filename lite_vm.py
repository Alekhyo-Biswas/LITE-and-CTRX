import importlib

class LiteVM:
    def __init__(self):
        self.commands = {}
        self.vars = {}       # code-based vars
        self.temp_vars = {}  # temp vars
        self.inst_vars = {}  # instance vars

        # built-in commands
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
            # silently load library
        except ModuleNotFoundError:
            print(f"Library not found: {libname}")
        except Exception as e:
            print(f"Error loading library '{libname}': {e}")

    def execute(self, cmdname, args):
        if cmdname in self.commands:
            self.commands[cmdname](args)
        else:
            print(f"Unknown command: {cmdname}")

    def clear_inst_vars(self):
        self.inst_vars = {}
