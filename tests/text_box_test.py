from pages.text_box_page import TextBoxPage


class TestBoxPage:

    def test_text_box(self, driver):
        test_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        test_box_page.open_page()
        full_name, email, current_address, perm_address = test_box_page.fill_fields()
        output_full_name, output_email, output_current_address, output_perm_address = test_box_page.check_output()
        assert full_name == output_full_name
        assert email == output_email
        assert current_address == output_current_address
        assert perm_address == output_perm_address
            