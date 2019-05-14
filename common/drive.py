from selenium import webdriver
from common.readconfig import ReadConfig
from selenium.webdriver.common.action_chains import ActionChains


class Drive:
    def __init__(self):
        self.readconfig = ReadConfig()
        self.driver = webdriver.Chrome()
        self.action = ActionChains(self.driver)

    def open_browser(self, url):
        self.driver.maximize_window()
        self.driver.get(url)
        return self.driver

    def close_brwser(self):
        self.driver.quit()

    def find_element(self, name):
        pathType = self.readconfig.getPathType(name)
        pathValue = self.readconfig.getPathValue(name)
        if pathType == 'id':
            return self.driver.find_element_by_id(pathValue)
        elif pathType == 'class_name':
            return self.driver.find_element_by_class_name(pathValue)
        elif pathType == 'name':
            return self.driver.find_element_by_name(pathValue)
        elif pathType == 'css_selector':
            return self.driver.find_element_by_css_selector(pathValue)
        elif pathType == 'xpath':
            return self.driver.find_element_by_xpath(pathValue)
        elif pathType == 'link_text':
            return self.driver.find_element_by_link_text(pathValue)
        elif pathType == 'tag_name':
            return self.driver.find_element_by_tag_name(pathValue)
        elif pathType == 'partial_link_text':
            return self.driver.find_element_by_partial_link_text(pathValue)

    def right_click(self, element_name=None):
        ac = ActionChains(self.driver)
        return ac.context_click(self.find_element(element_name)).perform()

    def switch_to_iframe(self):
        self.driver.switch_to.frame()


if __name__ == '__main__':
    dr = Drive()
    dr.open_browser('http://www.baidu.com/')

    dr.right_click('login_link')

    dr.close_brwser()




