from abstract_factory import Button, Checkbox, GuiFactory

# factories
class WindowsFactory(GuiFactory):
    def create_button(self):
        return WindowsButton()
    
    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory(GuiFactory):
    def create_button(self):
        return MacButton()
    
    def create_checkbox(self):
        return MacCheckbox()

## buttons
class WindowsButton(Button):
    def paint(self):
        return 'Painting a windows button'
    
class MacButton(Button):
    def paint(self):
        return 'Painting a macos button'

# Checkboxes
class WindowsCheckbox(Checkbox):
    def paint(self):
        return super().paint()
        
class MacCheckbox(Checkbox):
    def paint(self):
        return super().paint()

class App:
    def __init__(self, factory : GuiFactory):
        self.factory = factory
        self.button : Button
        self.checkbox : Checkbox

    def create_UI(self):
        self.button = self.factory.create_button()

    def paint(self):
        return self.button.paint()

    def create_checkbox(self):
        self.checkbox = self.factory.create_checkbox()


def create_app(**config_file):

    factory : GuiFactory
    if config_file.get('OS', '').lower() == "windows":
        factory = WindowsFactory()
    elif config_file.get('OS', '').lower() == "mac":
        factory = MacFactory()
    else:
        raise NotImplementedError('No factory implemented for OS ', config_file.get('OS', 'no OS passed'))
    
    return App(factory=factory)
    