"""
Yield Test
"""
import toga
import time


class NewGANManager(toga.App):

    def startup(self):
        self.output = toga.Label("")
        self.btn = toga.Button(label="Run", on_press=self.calc)

    def calc(self, widget):
        self.output.text = "RUN1"
        yield 0.1
        time.sleep(3)
        self.output.text = "RUN2"
        yield 0.1
