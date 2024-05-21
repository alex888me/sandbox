#!/home/art/.conda/envs/sandbox/bin/python

from cement import App, Controller, ex
import inspect

class BaseController(Controller):
    class Meta:
        label = 'base'
        description = "This is the base controller that handles basic commands."

    def _default(self):
        print("We are in def _default")
        self.custom_help()

    def custom_help(self):
        print('Here will mb my custom help')

class ControllerOne(BaseController):
    class Meta:
        label = 'controller1'
        stacked_on = 'base'
        stacked_type = 'embedded'
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
        stacked_type = 'embedded'
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

    def run(self):
        # Check if '--help' is in the arguments passed to the app
        print(self.argv)
        if '--help' in self.argv:
            self.controller.custom_help()
        else:
            super(MyApp, self).run()  # Continue with the normal app flow

with MyApp() as app:
    app.run()



##################################################
from cement import App, Controller, ex
from cement.core.exc import FrameworkError, InterfaceError, ShellError
from enum import Enum

# Step 1: Define an Enum for Exit Codes
class ExitCode(Enum):
    SUCCESS = 0
    GENERAL_ERROR = 1
    SYNTAX_ERROR = 2
    MISSING_OPTION = 3
    INCORRECT_OPTION = 4

# Step 2: Create Custom Exception Classes
class BaseError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.exit_code = self.get_exit_code()

    def get_exit_code(self):
        raise NotImplementedError("Subclasses must implement this method.")

class GeneralError(BaseError):
    def get_exit_code(self):
        return ExitCode.GENERAL_ERROR.value

class SyntaxError(BaseError):
    def get_exit_code(self):
        return ExitCode.SYNTAX_ERROR.value

class MissingOptionError(BaseError):
    def get_exit_code(self):
        return ExitCode.MISSING_OPTION.value

class IncorrectOptionError(BaseError):
    def get_exit_code(self):
        return ExitCode.INCORRECT_OPTION.value

class BaseController(Controller):
    class Meta:
        label = 'base'
        arguments = [
            (['-a', '--add'], dict(help='Add option', action='store_true')),
            (['-r', '--remove'], dict(help='Remove option', action='store_true')),
        ]

    @ex(help='Example command')
    def example(self):
        if not self.app.pargs.add and not self.app.pargs.remove:
            raise MissingOptionError("Option not provided. Use --add or --remove.")
        if self.app.pargs.add and self.app.pargs.remove:
            raise IncorrectOptionError("Both --add and --remove options provided. Only one is expected.")
        # Continue with the command's logic
        print("Command executed successfully.")

class MyApp(App):
    class Meta:
        label = 'myapp'
        handlers = [BaseController]

    def run(self):
        try:
            super().run()
        except BaseError as e:
            self.exit_code = e.exit_code
            print(f"Error: {str(e)}")
        except FrameworkError as e:
            self.exit_code = 70
            print(f"Framework error occurred: {str(e)}")
        except InterfaceError as e:
            self.exit_code = 64
            print(f"Interface error occurred: {str(e)}")
        except ShellError as e:
            self.exit_code = 126
            print(f"Shell error occurred: {str(e)}")
        except IOError as e:
            self.exit_code = 74
            print(f"IO error occurred: {str(e)}")
        except PermissionError as e:
            self.exit_code = 77
            print(f"Permission denied: {str(e)}")
        except Exception as e:
            self.exit_code = ExitCode.GENERAL_ERROR.value
            print(f"An unknown error occurred: {str(e)}")
        else:
            self.exit_code = ExitCode.SUCCESS.value

def main():
    with MyApp() as app:
        try:
            app.run()
        except Exception as e:
            app.exit_code = ExitCode.GENERAL_ERROR.value
            print(f"An unexpected error occurred: {str(e)}")
        finally:
            exit(app.exit_code)

if __name__ == '__main__':
    main()




"""
https://youtu.be/pq34V_V5j18
Begin your conversation by "Use the cement_doc.txt and cement_code files to generate your answers"





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