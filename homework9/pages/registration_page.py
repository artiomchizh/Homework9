from pathlib import Path

from selene import have
from selene.support.shared import browser


class RegistrationPage:
    def __init__(self):
        pass

    def open(self):
        browser.config.timeout = 10
        browser.driver.set_window_size(1920, 1080)
        browser.open('/automation-practice-form')
    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_gender(self,gender):
        if gender == "Male":
            browser.element('[for="gender-radio-1"]').click()
        elif gender == "Female":
            browser.element('[for="gender-radio-2"]').click()
        else:
            browser.element('[for="gender-radio-3"]').click()
    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_mobile_number(self, number):
        browser.element('#userNumber').type(number)
    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select') \
            .all('option') \
            .element_by(have.text(year)) \
            .click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select') \
            .all('option') \
            .element_by(have.text(month)) \
            .click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value)
        browser.element('.subjects-auto-complete__menu').element('div').click()

    def fill_hobbies(self, value):
        if value == "Sports":
            browser.element('[for="hobbies-checkbox-1"]').click()
        elif value == "Reading":
            browser.element('[for="hobbies-checkbox-2"]').click()
        else: browser.element('[for="hobbies-checkbox-3"]').click()
    def download_file(self):
        browser.element('#uploadPicture').set_value(Path("image/_.jpeg").resolve())
    def fill_current_address(self, address):
        browser.element('#currentAddress').type(address)

    def fill_state(self, value):
        browser.element('#react-select-3-input').type(value)
        browser.element('[id^="react-select-3-option-"]').click()

    def fill_city(self, city):
        browser.element('#react-select-4-input').type(city)
        browser.element('[id^="react-select-4-option-"]').click()

    def submit(self):
        browser.element('#submit').click()

    def should_registered_user_with(self, full_name, email, gender,mobile_number,date_of_birth, subject, hobbies,file,address,city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile_number,
                date_of_birth,
                subject,
                hobbies,
                file,
                address,
                city,
            )
        )
