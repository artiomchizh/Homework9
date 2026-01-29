from homework9.application import app
from homework9.data.users import User


def test_fill_text_box():
    user = User(
        full_name='Artiom',
        email='artiom@example.com',
        current_address='Saint-Petersburg',
        permanent_address='Moscow'
        )
    app.left_panel.open_simple_registration_form()
    app.registration_page \
        .should_be_opened() \
        .fill_data(user) \
        .submit() \
        .should_display_submitted_data(user)


