from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # 伊迪丝访问首页，不小心提交了一个空待办事项
        # 输入框中没输入内容，她就按下了回车键
        self.browser.get(self.server_url)
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)

        # 首页刷新了，显示一个错误消息
        # 提示待办事项不能为空
        error = self.browser.find_element(By.CSS_SELECTOR, '.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # 她输入一些文字，然后再次提交，这次没问题了
        self.browser.find_element(By.ID, 'id_new_item').send_keys('Buy milk\n')

        # 她有点儿调皮，又提交了一个空待办事项
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)

        # 在清单页面她看到了一个类似的错误消息
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element(By.CSS_SELECTOR, '.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # 输入文字之后就没问题了
        self.browser.find_element(By.ID, 'id_new_item').send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

        self.fail('write me!')
