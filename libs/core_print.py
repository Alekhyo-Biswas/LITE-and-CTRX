def register(vm):
    def cmd_print(args):
        if not args:
            print()
            return
        text = " ".join(args)
        if text.startswith('"') and text.endswith('"'):
            # literal string
            print(text[1:-1])
        else:
            # variable lookup in inst -> temp -> var
            if text in vm.inst_vars:
                print(vm.inst_vars[text])
            elif text in vm.temp_vars:
                print(vm.temp_vars[text])
            elif text in vm.vars:
                print(vm.vars[text])
            else:
                print(f"(undefined var: {text})")
    vm.register_command('print', cmd_print)
