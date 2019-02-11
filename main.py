from ui.RootContainer import root_container
from ui.DisplayContainer import display_container
from prompt_toolkit import Application
from KeyBinding import *

if __name__ == '__main__':
    root_layout = root_container.create()
    app = Application(layout=root_layout, key_bindings=kb, full_screen=True)
    display_container.alarm_thread.start()
    app.run()
