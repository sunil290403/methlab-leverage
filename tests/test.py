#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utils.selenium_utils import SeleniumUtils

tnc_checkbox = "//div[contains(@class,'items-start gap-3')]/div[1]"
wallet_close_button = "//div[@class='relative']/following::button[contains(@class,'cursor-pointer')]"
v1_leverage = "//div[contains(@class, 'relative grid')][1]//span[1]"
v2_leverage = "//div[contains(@class, 'relative grid')][2]//span[1]"
v3_leverage = "//div[contains(@class, 'relative grid')][3]//span[1]"
v1_leverage_liquidity = "//div[contains(@class, 'relative grid')][1]//div[7]//span"
v2_leverage_liquidity = "//div[contains(@class, 'relative grid')][2]//div[7]//span"
v3_leverage_liquidity = "//div[contains(@class, 'relative grid')][3]//div[7]//span"
v1_leverage_text = "//span[contains(@class, 'text-variant-primary bg-variant-primary-15')]//span"
margin_field = "//input[@name='collateralTokenAmount']"
position_field = "//input[@name='leverageCollateralAmount']"
spot_price_xpath = "//div[contains(text(),'1mETH')]"
exceeding_liquidity_error = "//input[@name='leverageCollateralAmount']/preceding::div[1]"
margin_error = "//input[@name='collateralTokenAmount']/preceding::div[1]"
leverage_pair = "//h2[text()='mETH  -  USDT']"
leverage_canvas = "//canvas"
connect_wallet_button = "//input[@name='collateralTokenAmount']/following::span[text()='Connect Wallet']"
total_repayment_option = "//div[text()='Total Repayment']"
fixed_borrow_fee = "//button[text()='Fixed Borrow Fee']"
open_orders = "//div[text()='Open Orders']"
transaction_history = "//div[text()='Transaction History']"


class TestWebsite:
    @classmethod
    def setup_class(cls):
        """Setup for the entire test class."""
        cls.browser = webdriver.Chrome()
        cls.browser.maximize_window()
        cls.browser.implicitly_wait(10)
        cls.browser.get("https://www.methlab.xyz/leverage")
        cls.selenium_utils = SeleniumUtils(driver=cls.browser, timeout=20)

        # Performing initial setup actions
        cls.selenium_utils.click_element(tnc_checkbox)
        cls.selenium_utils.click_element(wallet_close_button)

    @classmethod
    def teardown_class(cls):
        """Teardown for the entire test class."""
        cls.browser.close()
        cls.browser.quit()

    def test_landing_leverage(self):
        """This test checks the landing page of leverage & UI elements"""
        assert self.selenium_utils.element_exists(v1_leverage), "Leverage page option is missing"
        assert self.selenium_utils.element_exists(leverage_pair), "leverage pair dropdown missing"
        assert self.selenium_utils.element_exists(leverage_canvas), "leverage canvas is absent"
        assert self.selenium_utils.element_exists(connect_wallet_button), "Leverage page landing failed"
        assert self.selenium_utils.element_exists(total_repayment_option), "Leverage page landing failed"
        assert self.selenium_utils.element_exists(fixed_borrow_fee), "Leverage page landing failed"
        assert self.selenium_utils.element_exists(open_orders), "Leverage page landing failed"
        assert self.selenium_utils.element_exists(transaction_history), "Leverage page landing failed"
        '''
        Rest of the UI elements are covered through following testcases
        '''

    def test_invalid_margin(self):
        """This test error message thrown when invalid margin entered"""
        self.selenium_utils.click_element(margin_field)
        self.selenium_utils.clear_element(margin_field)
        self.selenium_utils.send_keys_to_element(margin_field, 0)
        assert self.selenium_utils.get_element_text(margin_error) == "Invalid Amount", "User entered accepted value"

    @pytest.mark.parametrize("leverage_xpath, expected_value", [
        (v1_leverage, "1.97x"),
        (v2_leverage, "3.15x"),
        (v3_leverage, "4.29x")
    ])
    def test_validate_different_leverage_options(self, leverage_xpath, expected_value):
        """This test checks the leverage options."""
        self.browser.refresh()
        self.selenium_utils.click_element(leverage_xpath)

        time.sleep(2)
        elements = self.selenium_utils.fetch_elements(v1_leverage_text)

        # Concatenate the text values from each span element to form the final value
        value = ''.join([element.text for element in elements])

        print(f"Extracted Value: {value}")

        assert value == expected_value, f"Leverage mismatch: expected {expected_value}, got {value}"

    @pytest.mark.parametrize("margin, leverage, leverage_xpath, liquidity_xpath",
                             [
                                 (1, 1.97, v1_leverage, v1_leverage_liquidity),
                                 (0.001, 1.97, v1_leverage, v1_leverage_liquidity),
                                 (0.05, 1.97, v1_leverage, v1_leverage_liquidity),
                                 (1, 3.15, v2_leverage, v2_leverage_liquidity),
                                 (0.001, 3.15, v2_leverage, v2_leverage_liquidity),
                                 (0.05, 3.15, v2_leverage, v2_leverage_liquidity),
                                 (1, 4.29, v3_leverage, v3_leverage_liquidity),
                                 (0.001, 4.29, v3_leverage, v3_leverage_liquidity),
                                 (0.05, 4.29, v3_leverage, v3_leverage_liquidity),
                                 # Add more test cases as needed
                             ]
                             )  # Test different leverage values
    def test_verify_leverage_calculation(self, margin, leverage, leverage_xpath, liquidity_xpath):
        """Test to verify leverage calculation"""
        print("leverage xpath :" + leverage_xpath)
        self.selenium_utils.click_element(leverage_xpath)

        self.selenium_utils.click_element(margin_field)
        self.selenium_utils.clear_element(margin_field)
        print("margin entered :" + str(margin))
        self.selenium_utils.send_keys_to_element(margin_field, margin)

        # Add wait to ensure the input is processed
        WebDriverWait(self.browser, 10).until(
            lambda driver: driver.find_element(By.XPATH, margin_field).get_attribute("value") == str(margin)
        )

        # Retrieve the spot price
        spot_price_element = self.selenium_utils.get_element_text(spot_price_xpath)
        spot_price = float(re.search(r'\d+\.\d+', spot_price_element).group())

        # Retrieve the liquidity for the selected leverage
        liquidity_elements = self.selenium_utils.fetch_elements(liquidity_xpath)
        value = ''.join([element.text for element in liquidity_elements])
        liquidity = float(re.search(r'\d+\.\d+', value).group())

        # Calculate the position size
        position_size = margin * leverage * spot_price

        # Check if the calculated position size exceeds the available liquidity
        exceeds_liquidity = position_size > liquidity

        if exceeds_liquidity:
            # Check if the UI shows "Exceeds Liquidity" error
            error_displayed = self.selenium_utils.element_is_visible(exceeding_liquidity_error)
            assert error_displayed, "Expected 'Exceeds Liquidity' error not displayed"
        else:
            # Extract the displayed leverage value
            displayed_leverage_element = self.selenium_utils.get_attribute_value(position_field, "value")
            try:
                displayed_leverage = float(displayed_leverage_element)
            except ValueError:
                print(f"Error converting displayed leverage to float: {displayed_leverage_element}")
                raise

            # Calculate the strike price
            strike_price = (spot_price / leverage) + spot_price

            # Calculate the expected leverage
            expected_leverage = spot_price / (strike_price - spot_price)

            # Use a tolerance for comparison
            tolerance = 0.01
            assert abs(displayed_leverage - (expected_leverage * margin)) < tolerance, (
                f"Leverage mismatch: expected {expected_leverage:.2f}, got {displayed_leverage:.2f}"
            )
            print(f"Expected Leverage: {expected_leverage:.20f}")
            print(f"Displayed Leverage: {displayed_leverage:.20f}")

        # Print results for debugging
        print(f"Chosen Leverage: {leverage}")
        print(f"Spot Price: {spot_price:.20f}")
