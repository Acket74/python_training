# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group
from common import *


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_add_group(self):
        wd = self.wd
        open_home_page(wd)
        login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.fill_group_form(wd, Group(name="aaa", header="bbb", footer="ccc"))
        self.submit_group_creation(wd)
        self.go_to_groups_page(wd)
        logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        open_home_page(wd)
        login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.fill_group_form(wd, Group(name="", header="", footer=""))
        self.submit_group_creation(wd)
        self.go_to_groups_page(wd)
        logout(wd)

    def go_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def submit_group_creation(self, wd):
        wd.find_element_by_name("submit").click()

    def fill_group_form(self, wd, group):
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def open_groups_page(self, wd):
        wd.find_element_by_name("new").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
