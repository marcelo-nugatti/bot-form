#!/usr/bin/python3
# -*- coding: utf-8 -*-
# BotForm

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class BotForm():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def setUp(self):
        self.driver.get("https://ibo.pe/contacto")
        time.sleep(5)

    def bot_form(self):
        self.name = self.driver.find_element_by_xpath('//*[@id="contacto"]/div/div[2]/div[2]/div/form/div[1]/div[1]/div/input')
        self.name.send_keys("Arnold")

        self.phone = self.driver.find_element_by_xpath('//*[@id="contacto"]/div/div[2]/div[2]/div/form/div[1]/div[2]/div/input')
        self.phone.send_keys("987654321")

        self.email = self.driver.find_element_by_xpath('//*[@id="contacto"]/div/div[2]/div[2]/div/form/div[2]/div[1]/div/input')
        self.email.send_keys("terminator@gmail.com")
        
        self.message = self.driver.find_element_by_xpath('//*[@id="contacto"]/div/div[2]/div[2]/div/form/div[2]/div[2]/div/textarea')
        self.message.send_keys("Hasta la vista, baby")

        self.button = self.driver.find_element_by_xpath('//*[@id="contacto"]/div/div[2]/div[2]/div/form/div[4]/div/div/button')
        self.button.click()

        time.sleep(5)

    def bot_loop(self):
        while True:
            self.setUp()
            self.bot_form()

if __name__ == '__main__':
    bot = BotForm()
    bot.bot_loop()
