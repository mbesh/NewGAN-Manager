"""
Yield Test
"""
import toga
import time


class NewGANManager(toga.App):

    def startup(self):
        self.main_window = toga.MainWindow(self.name)
        self.output = toga.Label("")
        self.btn = toga.Button(label="Run", on_press=self.calc)
        self.main_box = toga.Box()
        self.main_box.add(self.output)
        self.main_box.add(self.btn)
        self.main_window.content = self.main_box
        self.main_window.show()
    def calc(self, widget):
        self.output.text = "RUN1"
        yield 0.1
        time.sleep(3)
        self.output.text = "RUN2"
        yield 0.1

def main():
    return NewGANManager('Toga Demo', 'org.beeware.toga-demo')
