import data
import helpers
import time

from pages import UrbanRoutesPage
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = Chrome()
        cls.driver.implicitly_wait(6)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print ("Conectado ao servidor Urban Routes")
        else:
            print ("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")
    def setup_method(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page = UrbanRoutesPage(self.driver)


    def _start_confort_flow(self):
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

    def test_set_route(self):
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        assert self.page.get_from_location() == data.ADDRESS_FROM
        assert self.page.get_to_location() == data.ADDRESS_TO

        time.sleep(5)

    def test_select_plan(self):
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        self.page.click_taxi_option()
        self.page.click_comfort_icon()

        assert self.page.click_confort_active()

        time.sleep(5)

    def test_fill_phone_number(self):
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        self.page.click_taxi_option()
        self.page.click_comfort_icon()

        assert self.page.click_confort_active()
        self.page.click_number_text(data.PHONE_NUMBER)
        assert data.PHONE_NUMBER in self.page.numero_confirmado()
        time.sleep(5)

    def test_fill_card(self):
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_taxi_option()
        self.page.click_comfort_icon()

        self.page.click_confort_active()
        self.page.click_add_cartao(data.CARD_NUMBER, data.CARD_CODE)
        assert "Cartão" in self.page.confirm_cartao()

    def test_comment_for_driver(self):
        # Adicionar em S8
        print("função criada para definir a rota")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        print("função criada para definir a rota")
        pass

    def test_order_2_ice_creams(self):
        for i in range(2):
            # Adicionar em S8
            print("função criada para adicionar a quantidade de sorvetes")
            pass

    def test_car_search_model_appears(self):
        # Adicionar em S8
        print("função criada para definir a rota")
        pass


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()