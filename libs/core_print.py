def register(vm):
    """
    Register the print command into the VM.
    Usage in .ltx:  print varName  OR  print "hello"
    """

    def cmd_print(args):
        if not args:
            print()
            return

        token = args[0]

        # If token is a string literal in quotes
        if token.startswith('"') and token.endswith('"'):
            # strip quotes and print
            print(token[1:-1])
        else:
            # variable reference
            if token in vm.vars:
                print(vm.vars[token])
            else:
                print(f"(undefined var: {token})")

    vm.register_command('print', cmd_print)

