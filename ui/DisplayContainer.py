from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout import Window
from Alarm import get_formatted_alarm
from prompt_toolkit.filters.utils import to_filter
import threading
import time
from prompt_toolkit.layout.controls import BufferControl

buffer = Buffer(read_only=False, enable_history_search=True)


class DisplayContainer:
    def __init__(self):
        self.alarm_thread = AlarmThread(buffer)
        self.window = None

    def create(self):
        window = Window(content=BufferControl(buffer=buffer), height=10)
        self.window = window
        return window


class AlarmThread(threading.Thread):
    def __init__(self, text_buffer: Buffer):
        threading.Thread.__init__(self)
        self.text_buffer = text_buffer
        self.stop_flag = False

    def run(self):
        if self.stop_flag:
            self.stop_flag = False
        while not self.stop_flag:
            self.text_buffer.reset()
            string = get_formatted_alarm()
            self.text_buffer.text = str(string)

            time.sleep(1)

    def stop(self):
        self.stop_flag = True


display_container = DisplayContainer()
