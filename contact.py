__author__ = '1'


class Contact:
    def __init__(self, first_name, middle_name, last_name, nickname, photo, title, company, address, phones, emails,
                 homepage, birthday, anniversary, group, secondary):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.phones = phones
        self.emails = emails
        self.homepage = homepage
        self.birthday = birthday
        self.anniversary = anniversary
        self.group = group
        self.secondary = secondary


class PhoneSection:
    def __init__(self, home, mobile, work, fax):
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax

    def fill(self, wd):
        wd.find_element_by_name("home").send_keys(self.home)
        wd.find_element_by_name("mobile").send_keys(self.mobile)
        wd.find_element_by_name("work").send_keys(self.work)
        wd.find_element_by_name("fax").send_keys(self.fax)


class EmailsSection:
    def __init__(self, email1, email2, email3):
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3

    def fill(self, wd):
        wd.find_element_by_name("email").send_keys(self.email1)
        wd.find_element_by_name("email2").send_keys(self.email2)
        wd.find_element_by_name("email3").send_keys(self.email3)


class SecondarySection:
    def __init__(self, address, home, notes):
        self.address = address
        self.home = home
        self.notes = notes

    def fill(self, wd):
        wd.find_element_by_name("address2").send_keys(self.address)
        wd.find_element_by_name("phone2").send_keys(self.home)
        wd.find_element_by_name("notes").send_keys(self.notes)
