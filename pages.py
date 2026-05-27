from html.parser import commentclose

from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import data
from helpers import retrieve_phone_code
import time

class UrbanRoutesPage:

        # Fluxo para chamar taxi
    TAXI_OPTION = (By.XPATH, '//button[contains(.,"Chamar") or contains(.,"chamar")]')
    COMFORT_ICON = (By.XPATH, '//img[contains(@src,"kids")]')
    CONFORT_ACTIVE = (By.XPATH, '//*[@id="root"]//div[contains(@class,"active")]')

        #Seção "De" e "Para"
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    #Metodos POM

    def _find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def _type(self, locator, text):
        element = self._find(locator)
        element.clear()
        element.send_keys(text)

    #Endereços

    def _get_text(self, locator):
        return self._find(locator).text

    def _get_value(self, locator):
        return self._find(locator).get_attribute('value')

    def enter_locations(self, from_text, to_text):
        self._type(self.from_field, from_text)
        self._type(self.to_field, to_text)

    def get_from_location(self):
        return self._get_value(self.from_field)

    def get_to_location(self):
        return self._get_value(self.to_field)


        #chamar taxi
        
    def click_taxi_option(self):
        taxi_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.TAXI_OPTION)
        )
        taxi_button.click()

    def click_comfort_icon(self):
        comfort_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.COMFORT_ICON)
        )
        comfort_icon.click()

    def click_confort_active(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//div[contains(text(),"Comfort")]/ancestor::div[contains(@class,"active")]')
                )
            )
            return element.is_displayed()
        except:
            return False

    #telefone e sms
