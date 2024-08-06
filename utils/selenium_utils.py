from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class SeleniumUtils:
    def __init__(self, driver, timeout=10):
        """
        Initialize the SeleniumUtils with a timeout.

        :param driver: WebDriver instance
        :param timeout: Time to wait before timing out (default is 10 seconds)
        """
        self.driver = driver
        self.timeout = timeout

    def click_element(self, xpath):
        """
        Click an element specified by XPath.

        :param xpath: XPath locator for the element
        """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
        except TimeoutException:
            print(f"Timeout waiting for element to be clickable: {xpath}")
            raise
        except NoSuchElementException:
            print(f"Element not found: {xpath}")
            raise

    def send_keys_to_element(self, xpath, keys):
        """
        Send keys to an element specified by XPath.

        :param xpath: XPath locator for the element
        :param keys: Keys to send to the element
        """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            element.send_keys(keys)
        except TimeoutException:
            print(f"Timeout waiting for element to be present: {xpath}")
            raise
        except NoSuchElementException:
            print(f"Element not found: {xpath}")
            raise

    def get_element_text(self, xpath):
        """
        Get the text of an element specified by XPath.

        :param xpath: XPath locator for the element
        :return: Text of the element
        """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element.text
        except TimeoutException:
            print(f"Timeout waiting for element to be present: {xpath}")
            raise
        except NoSuchElementException:
            print(f"Element not found: {xpath}")
            raise

    def element_exists(self, xpath):
        """
        Check if an element specified by XPath exists.

        :param xpath: XPath locator for the element
        :return: True if element exists, False otherwise
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return True
        except TimeoutException:
            return False

    def element_is_visible(self, xpath):
        """
        Check if an element specified by XPath is visible.

        :param xpath: XPath locator for the element
        :return: True if element is visible, False otherwise
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return True
        except TimeoutException:
            return False

    def fetch_elements(self, xpath):
        """
        Fetch elements specified by XPath.

        :param xpath: XPath locator for the elements
        :return: List of web elements
        """
        try:
            elements = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_all_elements_located((By.XPATH, xpath))
            )
            return elements
        except TimeoutException:
            print(f"Timeout waiting for elements to be present: {xpath}")
            raise
        except NoSuchElementException:
            print(f"Elements not found: {xpath}")
            raise

    def clear_element(self, xpath):
        """
        Clear the content of an element specified by XPath.

        :param xpath: XPath locator for the element
        """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.clear()
        except TimeoutException:
            print(f"Timeout waiting for element to be clearable: {xpath}")
            raise
        except NoSuchElementException:
            print(f"Element not found: {xpath}")
            raise

    def get_attribute_value(self, xpath, attribute):
        """
        Get the attribute value of an element specified by XPath.

        :param xpath: XPath locator for the element
        :param attribute: Name of the attribute
        :return: Value of the attribute
        """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element.get_attribute(attribute)
        except TimeoutException:
            print(f"Timeout waiting for element to be present: {xpath}")
            raise
        except NoSuchElementException:
            print(f"Element not found: {xpath}")
            raise
