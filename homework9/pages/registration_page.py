from selene import have, be
from selene.support.shared import browser
from homework9.data.users import User

class RegistrationPage:
    def should_be_opened(self):
        browser.element('#userName').should(be.visible)
        return self

    def fill_data(self, user: User):
        browser.element('#userName').type(user.full_name)
        browser.element('#userEmail').type(user.email)
        browser.element('#currentAddress').type(user.current_address)
        browser.element('#permanentAddress').type(user.permanent_address)
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def should_display_submitted_data(self, user: User):
        result = browser.element('.border')
        result.should(have.text(user.full_name))
        result.should(have.text(user.email))
        result.should(have.text(user.current_address))
        result.should(have.text(user.permanent_address))
        return self

