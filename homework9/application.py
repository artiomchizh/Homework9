from homework9.pages.left_panel import LeftPanel
from homework9.pages.registration_page import RegistrationPage


class Application:
    def __init__(self):
        self.registration_page = RegistrationPage()
        self.left_panel = LeftPanel()

app = Application()