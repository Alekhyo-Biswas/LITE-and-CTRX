def register(vm):
    """
    Register the print command into the VM.
    Usage in .ltx:  print varName  OR  print "hello world"
    """
    def cmd_print(args):
        if not args:
            print()
            return

        out_parts = []
        for arg in args:
            # string literal in quotes
            if arg.startswith('"') and arg.endswith('"'):
                out_parts.append(arg[1:-1])  # strip quotes
            # variable reference
            elif arg in vm.vars:
                out_parts.append(str(vm.vars[arg]))
            else:
                # raw literal (numbers, bools, etc.)
                out_parts.append(arg)

        print(" ".join(out_parts))

    vm.register_command('print', cmd_print)
