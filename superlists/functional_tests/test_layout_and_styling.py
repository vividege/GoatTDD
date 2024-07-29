import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # 伊迪丝访问首页
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # 她看到输入框完美地居中显示
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys("testing")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(0.2)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )
