import time
import threading

def register(vm):
    """
    Add event commands to the VM:
      - on <condition>
      - when <condition>
      - every <milliseconds>
      - listen_for <eventName>
      - trigger <eventName>
    """

    # storage for events
    if not hasattr(vm, "events"):
        vm.events = {}  # event_name -> list of command sequences

    # store a sequence under an event name
    def cmd_on(args):
        if not args:
            print("Usage: on <eventName>")
            return
        event_name = " ".join(args)
        if event_name not in vm.events:
            vm.events[event_name] = []
        # sequences will be added by main.py when parsing
        print(f"(event registered: {event_name})")

    def cmd_when(args):
        # alias for 'on'
        cmd_on(args)

    def cmd_listen_for(args):
        if not args:
            print("Usage: listen_for <eventName>")
            return
        event_name = " ".join(args)
        if event_name not in vm.events:
            vm.events[event_name] = []
        print(f"(listener registered: {event_name})")

    def cmd_trigger(args):
        if not args:
            print("Usage: trigger <eventName>")
            return
        event_name = " ".join(args)
        if event_name not in vm.events:
            print(f"(no such event: {event_name})")
            return
        # execute all sequences associated with this event
        for seq in vm.events[event_name]:
            for cmd, cmd_args in seq:
                vm.execute(cmd, cmd_args)
            vm.clear_inst()  # clear inst vars after sequence

    def cmd_every(args):
        if not args or not args[0].isdigit():
            print("Usage: every <milliseconds>")
            return
        interval = int(args[0]) / 1000.0  # convert to seconds

        def loop():
            while True:
                for seq in getattr(vm, "every_sequences", []):
                    for cmd, cmd_args in seq:
                        vm.execute(cmd, cmd_args)
                    vm.clear_inst()
                time.sleep(interval)

        # run in background thread
        t = threading.Thread(target=loop, daemon=True)
        t.start()

    vm.register_command("on", cmd_on)
    vm.register_command("when", cmd_when)
    vm.register_command("listen_for", cmd_listen_for)
    vm.register_command("trigger", cmd_trigger)
    vm.register_command("every", cmd_every)
