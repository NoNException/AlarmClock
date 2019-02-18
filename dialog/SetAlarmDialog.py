from prompt_toolkit.layout import Float
from prompt_toolkit.widgets import Dialog, Label, Button

from ui.RootContainer import root_container


def button_handler():
    pass


class SetAlarmDialog:
    def __init__(self, event):

        self.dialog = Dialog(
            title="Set New Alarm",
            body=Label(text="you can set a new alarm clock here", dont_extend_height=True),
            buttons=[Button(text="OK", handler=button_handler)]
        )
        root_container.float_container.floats.pop()
        root_container.float_container.floats.append(Float(content=self.dialog))
        event.app.layout.focus(self.dialog)
