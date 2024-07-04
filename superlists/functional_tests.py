import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        # tell browser if needed, wait for 3 seconds
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请她输入一个待办事项
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # 她在一个文本框中输入了“Buy peacock feathers”（购买孔雀羽毛）
        # 伊迪丝的爱好是使用假蝇做鱼饵钓鱼
        inputbox.send_keys('Buy peacock feathers')

        # 她按回车键后，页面更新了
        # 待办事项表格中显示了“1: Buy peacock feathers”
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = self.browser.find_elements(By.TAG_NAME, 'tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # 页面中还有一个文本框，可以输入其他的待办事项
        # 她输入了“Use peacock feathers to make a fly”（使用孔雀羽毛做假蝇）
        # 伊迪丝做事很有条理
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        import time
        time.sleep(0.5)
        # rows = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'tr')))
        rows = self.browser.find_elements(By.TAG_NAME, 'tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])

        # 伊迪丝想知道这个网站是否会记住她的清单
        # 她看到网站为她生成了一个唯一的URL
        # 页面中有一些文字解说这个功能
        self.fail('Finish the test!')  # The test will fail anyway, use this way to inform that the test is complete


if __name__ == '__main__':
    unittest.main()
