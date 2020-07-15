from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException


MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):
    """Тест нового посетителя"""

    def setUp(self):
        """установка"""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """демонтаж"""
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        """ожидание строки в конце списка"""
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        """тест: можно начать список и получить его позже"""

        # Пользователь видит домашнюю страницу
        self.browser.get(self.live_server_url)

        # Заголовок и шапка страницы говорят о списке неотложных дел
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Предложение ввести элемент списка
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Ввод пользователем текста "Купить павлиньи перья"
        inputbox.send_keys('Купить павлиньи перья')

        # После нажатия ENTER страница обновляется, и теперь страница содержит:
        # "1. Купить павлиньи перья" в качестве элемента списка
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)
        self.wait_for_row_in_list_table('1: Купить павлиньи перья')

        #  Текстовое поле по-прежнему предлагает добавить элемент списка.
        # Пользователь вводит "Сделать мушку из павлиньих перьев"
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)

        # Страница вновь обновляется, и теперь показывает оба элемента списка
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.wait_for_row_in_list_table('1: Купить павлиньи перья')
        self.wait_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')

        # Сайт запоминает этот список. Сгенерирован уникальный URL, и об этом выводится текст с объснением
        self.fail('Закончить тест!')
        # При посещении полученного URL-адреса - там действительно хранится список.

        # Пользователь покидает сайт

