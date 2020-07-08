from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    """Тест нового посетителя"""

    def setUp(self):
        """установка"""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """демонтаж"""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """тест: можно начать список и получить его позже"""

        # Пользователь видит домашнюю страницу
        self.browser.get('http://localhost:8000')

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
        time.sleep(1)
        table = self.browser.find_elements_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Купить павлиньи перья' for row in rows)
        )

        #  Текстовое поле по-прежнему предлагает добавить элемент списка.
        # Пользователь вводит "Сделать мушку из павлиньих перьев"
        self.fail('Закончить тест!')
        # Страница вновь обновляется, и теперь показывает оба элемента списка

        # Сайт запоминает этот список. Сгенерирован уникальный URL, и об этом выводится текст с объснением

        # При посещении полученного URL-адреса - там действительно хранится список.

        # Пользователь покидает сайт


if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main(warnings='ignore')
