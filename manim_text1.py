from manim import *

class HelloWorld(Scene):
    def construct(self):
        print("Hello from Binder!")
        text = Text("Hello world", font_size=144)
        self.add(text)
