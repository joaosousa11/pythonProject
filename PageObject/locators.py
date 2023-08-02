from selenium.webdriver.common.by import By


class Locator(object):

    # LOGIN
    credentials_card = (By.CLASS_NAME, "page__heading")
    user = (By.NAME, "user[email]")
    password = (By.NAME, "user[password]")
    login_btn = (By.XPATH, "//button[normalize-space()='Sign in']")

    new_account_btn = (By.XPATH, '//a[contains(@href,"/users/sign_up")]')
    create_account_card = (By.ID, "create-account")
    inp_fname = (By.NAME, "user[first_name]")
    inp_lname = (By.NAME, "user[last_name]")
    inp_email = (By.NAME, "user[email]")
    inp_password = (By.NAME, "user[password]")
    chk_terms = (By.ID, "user[terms]")
    sign_up_btn = (By.XPATH, "//button[normalize-space()='Sign up']")

    # Login - Alerts
    email_error = (By.ID, "user[email]-error")
    password_error = (By.ID, "user[password]-error")
    invalid_login = (By.CLASS_NAME, "message-text")

    # HOME
    sign_in_message = (By.CLASS_NAME, "message-text")
    my_dash_title = (By.XPATH, '//a[contains(@href,"/enrollments")]')

    user_dropdown = (By.CLASS_NAME, "dropdown__toggle-button")
    log_out_opt = (By.XPATH, '//a[contains(@href,"/users/sign_out")]')

    main_page = (By.CLASS_NAME, "section__headings")

