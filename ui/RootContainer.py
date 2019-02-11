from prompt_toolkit.layout import HSplit
from prompt_toolkit.layout import Layout
from ui.DisplayContainer import display_container


class RootLayout:
    def create(self):
        display_layout = display_container.create()
        return Layout(HSplit([display_layout]), focused_element=display_layout)


root_container = RootLayout()
