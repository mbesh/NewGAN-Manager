import unittest
from newganmanager.app import NewGANManager
import asyncio


def async_test(f):
    def wrapper(*args, **kwargs):
        coro = asyncio.coroutine(f)
        future = coro(*args, **kwargs)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(future)
    return wrapper


class Test_App(unittest.TestCase):
    def test_calc(self):
        app = NewGANManager('Toga Demo', 'org.beeware.toga-demo')
        app.startup()
        res = [i for i in app.calc(None)]
        self.assertEqual(res, [1, 2])
        self.assertEqual("RUN2", app.output.text)

    @async_test
    def test_button_press(self):
        self.app = NewGANManager('Toga Demo', 'org.beeware.toga-demo')
        self.app.startup()
        self.app.btn.on_press(self.app.btn)
        print(self.app.btn.on_press)
        print(self.app.btn.on_press._raw)
        print(self.app.output.text)


if __name__ == '__main__':
    unittest.main()
