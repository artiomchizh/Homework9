from selene import have, be
from selene.support.shared import browser


class LeftPanel:
    def open(self, category: str, subcategory: str):
        browser.config.timeout = 10
        browser.driver.set_window_size(1920, 1080)
        browser.open('/')
        browser.all('div') \
            .element_by(have.exact_text(category)) \
            .should(be.visible) \
            .click()
        browser.element('#item-0').click()
        return self

    def open_simple_registration_form(self):
        return self.open('Elements', 'Text Box')