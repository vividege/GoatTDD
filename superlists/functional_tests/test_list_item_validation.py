import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # 伊迪丝访问首页，不小心提交了一个空待办事项
        # 输入框中没输入内容，她就按下了回车键
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # 首页刷新了，显示一个错误消息
        # 提示待办事项不能为空
        error = self.browser.find_element(By.CSS_SELECTOR, '.form-group.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # 她输入一些文字，然后再次提交，这次没问题了
        self.get_item_input_box().send_keys('Buy milk{0}'.format(Keys.ENTER))
        time.sleep(1)
        # 她有点儿调皮，又提交了一个空待办事项
        self.get_item_input_box().send_keys(Keys.ENTER)

        # 在清单页面她看到了一个类似的错误消息
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element(By.CSS_SELECTOR, '.form-group.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # 输入文字之后就没问题了
        self.get_item_input_box().send_keys('Make tea{0}'.format(Keys.ENTER))
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        # 伊迪丝访问首页，新建一个清单
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies{0}'.format(Keys.ENTER))
        self.check_for_row_in_list_table('1: Buy wellies')

        # 她不小心输入了一个重复的待办事项
        self.get_item_input_box().send_keys('Buy wellies{0}'.format(Keys.ENTER))

        # 她看到一条有帮助的错误消息
        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.browser.find_element(By.CSS_SELECTOR, '.has-error')
        self.assertEqual(error.text, "You've already got this in your list")