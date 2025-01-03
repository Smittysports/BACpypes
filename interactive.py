
import cmd
import threading

from bacpypes.debugging import ModuleLogger
from bacpypes.apdu import UnconfirmedTextMessageRequest
import bacpypes.core

# some debugging
_debug = 0
_log = ModuleLogger(globals())

class Prompt(cmd.Cmd, threading.Thread):

    def __init__(self, application):
        cmd.Cmd.__init__(self)
        threading.Thread.__init__(self, name="BACpypesPrompt")

        # set the application
        self.application = application

        # Set the prompt
        self.prompt = "> "

        # start the thread
        self.start()

    def run(self):
        # run the command loop
        self.cmdloop()

    def do_quit(self, line):
        # quit this little shell...
        bacpypes.core.stop()
        return True

    def default(self, line):
        # make a text message out of the line
        apdu = UnconfirmedTextMessageRequest(
            textMessageSourceDevice=('device', 419303),
            messagePriority = 'normal',
            message = line
        )
        # have the application process it
        self.application.do_UnconfirmedTextMessageRequest(apdu)

    def postcmd(self, stop, line):
        if not bacpypes.core.running:
            return True

        return stop

    def emptyline(self):
        pass


