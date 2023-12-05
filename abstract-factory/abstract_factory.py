import abc 


class GuiFactory(metaclass=abc.ABCMeta):
    def create_button(self):
        pass

    def create_checkbox(self):
        pass

class Button(metaclass=abc.ABCMeta):
    def paint(self):
        pass

class Checkbox(metaclass=abc.ABCMeta):
    def paint(self):
        pass

