from cement import App, Controller, ex
import inspect

class BaseController(Controller):
    class Meta:
        label = 'base'
        description = "This is the base controller that handles basic commands."

    def _default(self):
        self.custom_help()

    def custom_help(self):
        print("usage: myapp [-h] {controller1,controller2,default} ...\n")
        print("This is the base controller that handles basic commands.\n")
        print("sub-commands:")
        controllers = [ControllerOne, ControllerTwo]
        for controller_cls in controllers:
            controller = controller_cls()
            controller._setup(self.app)
            print(f"  {controller.Meta.label:<12} {controller.Meta.description}")
            for name, method in inspect.getmembers(controller, predicate=inspect.ismethod):
                print(name, method)
                ex_meta = getattr(method, '_cement_meta', None)
                if ex_meta:
                    print(f"      {name:<12} {ex_meta.help}")


class ControllerOne(BaseController):
    class Meta:
        label = 'controller1'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = "Controller one managing specific tasks."

    @ex(help='Handle cmd1')
    def cmd1(self):
        print("Executing cmd1")

    @ex(help='Handle cmd2')
    def cmd2(self):
        print("Executing cmd2")

class ControllerTwo(BaseController):
    class Meta:
        label = 'controller2'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = "Controller two managing other specific tasks."

    @ex(help='Handle cmd3')
    def cmd3(self):
        print("Executing cmd3")

    @ex(help='Handle cmd4')
    def cmd4(self):
        print("Executing cmd4")

class MyApp(App):
    class Meta:
        label = 'myapp'
        base_controller = 'base'
        handlers = [BaseController, ControllerOne, ControllerTwo]

with MyApp() as app:
    app.run()















"""
please use cement_doc.txt, cement_code1.txt, cement_code2.txt, cement_code3.txt, cement_code4.txt
Document to generate your answer


from cement import App, Controller, ex

class BaseController(Controller):
    class Meta:
        label = 'base'
        description = "This is the base controller that handles basic commands."

    @ex(help='default command', hide=True)
    def default(self):
        self.app.args.print_help()

class ControllerOne(BaseController):
    class Meta:
        label = 'controller1'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = "Controller one managing specific tasks."
        help = "Use this controller to manage cmd1 and cmd2."

    @ex(help='Handle cmd1')
    def cmd1(self):
        print("Executing cmd1")

    @ex(help='Handle cmd2')
    def cmd2(self):
        print("Executing cmd2")

class ControllerTwo(BaseController):
    class Meta:
        label = 'controller2'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = "Controller two managing other specific tasks."
        help = "Use this controller to manage cmd3 and cmd4."

    @ex(help='Handle cmd3')
    def cmd3(self):
        print("Executing cmd3")

    @ex(help='Handle cmd4')
    def cmd4(self):
        print("Executing cmd4")

class MyApp(App):
    class Meta:
        label = 'myapp'
        base_controller = 'base'
        handlers = [BaseController, ControllerOne, ControllerTwo]

with MyApp() as app:
    app.run()
















sub-commands:
  {controller2,controller1,default}
    controller2         Use this controller to manage cmd3 and cmd4.
        cmd3               Handle cmd3
        cmd4               Handle cmd4
    controller1         Use this controller to manage cmd1 and cmd2.
        cmd1               Handle cmd1
        cmd2               Handle cmd2
art@fedora:~/sandbox$ /home/art/.conda/envs/sandbox/bin/python ./cement_sandbox.py controller1 --help
usage: myapp controller1 [-h] {cmd1,cmd2,default} ...

Controller one managing specific tasks.

options:
  -h, --help           show this help message and exit

sub-commands:
  {cmd1,cmd2,default}
    cmd1               Handle cmd1
    cmd2               Handle cmd2
art@fedora:~/sandbox$ /home/art/.conda/envs/sandbox/bin/python ./cement_sandbox.py controller2 --help
usage: myapp controller2 [-h] {cmd3,cmd4,default} ...

Controller two managing other specific tasks.

options:
  -h, --help           show this help message and exit

sub-commands:
  {cmd3,cmd4,default}
    cmd3               Handle cmd3
    cmd4               Handle cmd4

"""