from prompt_toolkit.key_binding import KeyBindings
from ui.DisplayContainer import display_container, AlarmThread, buffer

kb = KeyBindings()


@kb.add('c-q')
def exit_(event):
    display_container.alarm_thread.stop()
    event.app.exit()


@kb.add('c-w')
def stop_(event):
    display_container.alarm_thread.stop()


@kb.add('c-s')
def start_(event):
    if display_container.alarm_thread.stop_flag:
        display_container.alarm_thread = AlarmThread(buffer)
        display_container.alarm_thread.start()
