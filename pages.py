from html.parser import commentclose

from selenium.webdriver import Keys
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

    # Numero de telefone
    number_text_locator = (By.CSS_SELECTOR, '.np-button')
    number_enter = (By.ID, 'phone')
    number_confirm = (By.CSS_SELECTOR, '.button.full')
    number_code = (By.ID, 'code')
    code_confirm = (By.XPATH, '//button[contains(text(),"Confirmar")]')
    number_finish = (By.CSS_SELECTOR, '.np-text')

    # Metodos de pagamento(cartao)
    add_metodo_pagamento = (By.CSS_SELECTOR, '.pp-button.filled')
    add_card = (By.CSS_SELECTOR, '.pp-plus')
    number_card = (By.ID, 'number')
    code_card = (By.CSS_SELECTOR, 'input.card-imput#code')
    add_finish_card = (By.XPATH, '//button[contains(text(),"Adicionar")]')
    close_button_card = (By.CSS_SELECTOR, '.payment-picker.open .close-button')
    comfirm_card = (By.CSS_SELECTOR, '.pp-value-text')

    # Seção "De" e "Para"
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


    def click_number_text(self, telefone):
        self.driver.find_element(*self.number_text_locator).click()

        self.driver.find_element(*self.number_enter).send_keys(telefone)

        self.driver.find_element(*self.number_confirm).click()

        code = retrieve_phone_code(self.driver)

        code_input = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.number_code)
    )

        code_input.clear()
        code_input.send_keys(code)

        self.driver.find_element(*self.code_confirm).click()

    def numero_confirmado(self):
        numero = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.number_finish))
        return numero.text

    def _press_tab(self):
        self.driver.switch_to.active_element.send.keys(Keys.TAB)

    def click_add_cartao(self,cartao,code):
        self.driver.find_element(*self.add_metodo_pagamento).click()
        self.driver.find_element(*self.add_card).click()
        time.sleep(2)
        self.driver.find_element(*self.number_card).send_keys(cartao)
        time.sleep(2)
        self.driver.find_element(*self.code_card).send_keys(code)
        time.sleep(2)
        self._press_tab()
        time.sleep(10)
        self.driver.find_element(*self.add_finish_card).click()
        self.driver.find_element(*self.close_button_card).click()

    def confirm_cartao(self):
        return self.driver.find_element(*self.comfirm_card).text

