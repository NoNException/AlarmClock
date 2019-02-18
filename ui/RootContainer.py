from prompt_toolkit.layout import HSplit, FloatContainer, Float, CompletionsMenu, Window
from prompt_toolkit.layout import Layout
from ui.DisplayContainer import display_container


class RootLayout:
    def __init__(self):
        self.display_layout = None
        self.float_container = None

    def create(self):
        self.display_layout = display_container.create()
        completions = Float(xcursor=True, ycursor=True, content=CompletionsMenu(max_height=16, scroll_offset=1))
        self.float_container = FloatContainer(content=self.display_layout, floats=[completions])

        return Layout(HSplit([self.float_container]), focused_element=self.display_layout)


root_container = RootLayout()
