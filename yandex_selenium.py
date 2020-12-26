import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestYandexPassport(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://passport.yandex.ru/auth/')

    def test_1_is_yandex_authorization(self):
        self.assertIn('Авторизация', self.driver.title)

    def test_2_yandex_wrong_login(self):
        login = self.driver.find_element_by_name('login')
        login.send_keys('abdhksds')
        login.send_keys(Keys.RETURN)
        time.sleep(10)
        self.assertIn('Такого аккаунта нет', self.driver.page_source)

    def test_3_yandex_wrong_password(self):
        login = self.driver.find_element_by_name('login')
        login.send_keys('kio99')
        login.send_keys(Keys.RETURN)
        time.sleep(10)
        password = self.driver.find_element_by_name('passwd')
        password.send_keys('kioooooo')
        password.send_keys(Keys.RETURN)
        time.sleep(10)
        self.assertIn('Неверный пароль', self.driver.page_source)

    def test_4_login_forbidden_symbols(self):
        login = self.driver.find_element_by_name('login')
        login.send_keys('a[b[d*h]]k+s=d][s')
        login.send_keys(Keys.RETURN)
        time.sleep(10)
        self.assertIn('Такой логин не&nbsp;подойдет', self.driver.page_source)

    def test_5_blank_login(self):
        login = self.driver.find_element_by_name('login')
        login.send_keys('')
        login.send_keys(Keys.RETURN)
        time.sleep(10)
        self.assertIn('Логин не&nbsp;указан', self.driver.page_source)

    def test_6_blank_password(self):
        login = self.driver.find_element_by_name('login')
        login.send_keys('kio99')
        login.send_keys(Keys.RETURN)
        time.sleep(10)
        password = self.driver.find_element_by_name('passwd')
        password.send_keys('')
        password.send_keys(Keys.RETURN)
        time.sleep(10)
        self.assertIn('Пароль не&nbsp;указан', self.driver.page_source)

    def tearDown(self):
        self.driver.close()
