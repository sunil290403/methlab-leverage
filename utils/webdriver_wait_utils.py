from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class WebDriverWaitUtils:
    def __init__(self, timeout=10):
        """
        Initialize the WebDriverWaitUtils with a timeout.

        :param timeout: Time to wait before timing out (default is 10 seconds)
        """
        self.timeout = timeout

    def wait_for_element_to_be_visible(self, driver, xpath):
        """
        Wait for an element specified by XPath to be visible on the page.

        :param driver: WebDriver instance
        :param xpath: XPath locator for the element
        :return: WebElement if found, raises TimeoutException otherwise
        """
        wait = WebDriverWait(driver, self.timeout)
        try:
            return wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print(f"Timeout waiting for element to be visible: {xpath}")
            raise

    def wait_for_element_to_be_clickable(self, driver, xpath):
        """
        Wait for an element specified by XPath to be clickable.

        :param driver: WebDriver instance
        :param xpath: XPath locator for the element
        :return: WebElement if found, raises TimeoutException otherwise
        """
        wait = WebDriverWait(driver, self.timeout)
        try:
            return wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            print(f"Timeout waiting for element to be clickable: {xpath}")
            raise

    def wait_for_element_to_be_present(self, driver, xpath):
        """
        Wait for an element specified by XPath to be present in the DOM.

        :param driver: WebDriver instance
        :param xpath: XPath locator for the element
        :return: WebElement if found, raises TimeoutException otherwise
        """
        wait = WebDriverWait(driver, self.timeout)
        try:
            return wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print(f"Timeout waiting for element to be present: {xpath}")
            raise

    def wait_for_alert_to_be_present(self, driver):
        """
        Wait for an alert to be present.

        :param driver: WebDriver instance
        :return: Alert if found, raises TimeoutException otherwise
        """
        wait = WebDriverWait(driver, self.timeout)
        try:
            return wait.until(EC.alert_is_present())
        except TimeoutException:
            print("Timeout waiting for alert to be present")
            raise

    def wait_for_text_to_be_present_in_element(self, driver, xpath, text):
        """
        Wait for a specific text to be present in an element specified by XPath.

        :param driver: WebDriver instance
        :param xpath: XPath locator for the element
        :param text: Text to be present in the element
        :return: WebElement if text is found, raises TimeoutException otherwise
        """
        wait = WebDriverWait(driver, self.timeout)
        try:
            return wait.until(EC.text_to_be_present_in_element((By.XPATH, xpath), text))
        except TimeoutException:
            print(f"Timeout waiting for text to be present in element: {xpath}, text: {text}")
            raise
