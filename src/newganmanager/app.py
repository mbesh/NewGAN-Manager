"""
Yield Test
"""
import toga
import time
from toga.style.pack import Pack

class NewGANManager(toga.App):

    def startup(self):
        self.main_window = toga.MainWindow(self.name)
        self.output = toga.Label("INITIALTEXT", style=Pack(width=100))
        self.btn = toga.Button(label="Run", on_press=self.calc)
        self.main_box = toga.Box()
        self.main_box.add(self.output)
        self.main_box.add(self.btn)
        self.main_window.content = self.main_box
        self.main_window.show()
    def calc(self, widget):
        self.output.text = "RUN1"
        self.output._impl.rehint()
        time.sleep(3)
        self.output.text = "RUN2"
        self.output._impl.rehint()


def main():
    return NewGANManager('Toga Demo', 'org.beeware.toga-demo')
