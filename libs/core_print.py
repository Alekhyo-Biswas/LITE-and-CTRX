def register(vm):
    """
    Register the print command into the VM.
    Usage: print varName OR print "Hello world"
    """

    def cmd_print(args):
        if not args:
            print()
            return

        for arg in args:
            # if arg is a defined variable, print its value
            if arg in vm.vars:
                print(vm.vars[arg], end=" ")
            else:
                # otherwise treat as literal
                print(arg, end=" ")
        print()  # newline at end

    vm.register_command('print', cmd_print)


