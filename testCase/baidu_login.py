import unittest
from common.drive import Drive
from common.log import Log
from common.screen import Screen
import time


class BaiDuLogin(unittest.TestCase):

    def setUp(self):
        self.log = Log()
        self.log.info("测试开始")
        self.dr = Drive()
        self.url = "http://www.baidu.com"
        self.input_name = '百度搜索输入框'
        self.click_name = '百度一下按钮'
        self.serach_name = 'haha'

    def test_search(self):
        self.log.info('打开浏览器，进入百度')
        self.dr.open_browser(self.url)
        self.dr.find_element(self.input_name).send_keys(self.serach_name)
        self.dr.find_element(self.click_name).click()
        self.log.info('点击搜索，对比结果')
        self.assertIn('百度', self.dr.driver.title)

    def tearDown(self):
        self.log.info('结束测试')
        time.sleep(2)
        self.dr.close_brwser()


if __name__ == '__main__':
    unittest.main()
