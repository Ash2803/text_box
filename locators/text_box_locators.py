from selenium.webdriver.common.by import By


class TextBoxLocators:
    """
    Locators for Text Box form
    """
    full_name = (By.CSS_SELECTOR, '#userName')
    email = (By.CSS_SELECTOR, '#userEmail')
    current_address = (By.CSS_SELECTOR, '#currentAddress')
    permanent_address = (By.CSS_SELECTOR, '#permanentAddress')
    submit = (By.CSS_SELECTOR, '#submit')

    created_full_name = (By.CSS_SELECTOR, '#output #name')
    created_email = (By.CSS_SELECTOR, '#output #email')
    created_current_address = (By.CSS_SELECTOR, '#output #currentAddress')
    created_permanent_address = (By.CSS_SELECTOR, '#output #permanentAddress')
