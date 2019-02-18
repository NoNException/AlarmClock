from prompt_toolkit.document import Document
from prompt_toolkit.layout import Float, HSplit
from prompt_toolkit.widgets import Dialog, Label, Button, TextArea
from ui.DisplayContainer import clock, reload_display_layout_clock
from Alarm import get_current_alarm
from ui.RootContainer import root_container


class SetAlarmDialog:
    def __init__(self, event):
        input_clock = get_current_alarm()

        def button_handler():
            root_container.float_container.floats.pop()
            event.app.layout.focus(root_container.display_layout)
            clock.append(self.clock.text)
            reload_display_layout_clock()

        self.clock = TextArea(multiline=False, text=input_clock)
        self.clock.buffer.document = Document(input_clock, len(input_clock))
        self.dialog = Dialog(
            title="Set New Alarm",
            body=HSplit([Label(text="you can set a new alarm clock here:\n", dont_extend_height=True),
                         self.clock]),
            buttons=[Button(text="OK", handler=button_handler)]
        )
        root_container.float_container.floats.append(Float(content=self.dialog))
        event.app.layout.focus(self.dialog)
