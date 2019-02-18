from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout import Window, HSplit
from Alarm import get_formatted_alarm
import threading
import time
from prompt_toolkit.layout.controls import BufferControl

buffer = Buffer(read_only=False, enable_history_search=True)
clock_buffer = Buffer(read_only=False, enable_history_search=True)
clock = []


class DisplayContainer:
    def __init__(self):
        self.alarm_thread = AlarmThread(buffer)
        self.border_window = None
        self.time_window = None
        self.clock_window = None

    def create(self):
        window = Window(content=BufferControl(buffer=buffer), height=6)
        self.border_window = Window(char='─', height=1)
        self.time_window = window
        self.clock_window = Window(content=BufferControl(buffer=clock_buffer), height=10)
        return HSplit([self.time_window, self.border_window, self.clock_window])


def reload_display_layout_clock():
    clock_buffer.reset()
    clock_buffer.text = "\n".join(clock)


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
