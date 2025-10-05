def register(vm):
    def parse_value(token):
        if token.startswith('"') and token.endswith('"'):
            return token[1:-1]
        try:
            if '.' in token:
                return float(token)
            return int(token)
        except ValueError:
            return token

    def cmd_var(args):
        if len(args) < 3 or args[1] != "=":
            print("Usage: var <name> = <value>")
            return
        name = args[0]
        value = parse_value(args[2])
        vm.vars[name] = value

    def cmd_temp(args):
        if len(args) < 4 or args[0] != "var" or args[2] != "=":
            print("Usage: temp var <name> = <value>")
            return
        name = args[1]
        value = parse_value(args[3])
        vm.temp_vars[name] = value

    def cmd_inst(args):
        if len(args) < 4 or args[0] != "var" or args[2] != "=":
            print("Usage: inst var <name> = <value>")
            return
        name = args[1]
        value = parse_value(args[3])
        vm.inst_vars[name] = value

    def cmd_delete(args):
        if not args:
            print("Usage: delete <var>")
            return
        name = args[0]
        if name in vm.temp_vars:
            del vm.temp_vars[name]
        else:
            print(f"Cannot delete: {name} is not a temp var")

    # register commands
    vm.register_command("var", cmd_var)
    vm.register_command("temp", cmd_temp)
    vm.register_command("inst", cmd_inst)
    vm.register_command("delete", cmd_delete)
