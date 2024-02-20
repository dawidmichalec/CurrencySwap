from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from window_manager import WindowManager

Window.size = (414,736)

class CurrencySwapApp(MDApp):

    def build(self):
        Builder.load_file("currencyswap.kv")

if __name__ == '__main__':
    CurrencySwapApp().run()