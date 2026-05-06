from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание появления элемента {locator}")
    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
    
    @allure.step("Ожидание появления списка элементов {locator}")
    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Клик по элементу {locator} FAQ")
    def click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)
        
    @allure.step("Клик по элементу {locator} формы бронирования")
    def click_order(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    @allure.step("Скролл до элемента {locator}")
    def scroll_to(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    
    
    @allure.step("Переключение на новую вкладку")
    def switch_to_new_tab(self):
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)

    @allure.step("Ожидание появления в URL текста: {text}")
    def wait_for_url_contains(self, text, time=5):
        return WebDriverWait(self.driver, time).until(EC.url_contains(text))
    
    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Открытие URL: {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Ввод текста '{text}' в элемент {locator}")
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)
