__author__ = '1'


class DatePicker:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def fill_date(self, wd, label):
        if not wd.find_element_by_xpath("//label[text()='{0}']/following-sibling::*[1]//option[{1}]".format(label, self.day)).is_selected():
            wd.find_element_by_xpath("//label[text()='{0}']/following-sibling::*[1]//option[{1}]".format(label, self.day)).click()
        if not wd.find_element_by_xpath("//label[text()='{0}']/following-sibling::*[2]//option[{1}]".format(label, self.month)).is_selected():
            wd.find_element_by_xpath("//label[text()='{0}']/following-sibling::*[2]//option[{1}]".format(label, self.month)).click()
        wd.find_element_by_xpath("//label[text()='{0}']/following-sibling::*[3]".format(label)).send_keys(self.year)
