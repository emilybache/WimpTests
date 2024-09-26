import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

from page_objects import OrderPage
from wimp import Order, Customer, Delivery


@pytest.fixture
def driver():
    return webdriver.Chrome()


def test_order(driver):
    driver.get("http://test.wimp.com")
    time.sleep(2)
    element = driver.find_element(By.NAME, 'search')
    element.send_keys("Margherita")
    search = driver.find_element(By.NAME, 'do_search')
    search.click()
    results = driver.find_element(By.NAME, 'search_results')
    assert "Margherita" in results.text
    driver.find_element(By.XPATH,
                        "//input[@type='radio' and @value='Medium']").click()
    add_to_basket = driver.find_element(By.NAME, "add_to_basket")
    add_to_basket.click()
    time.sleep(2)
    checkout = driver.find_element(By.NAME, "checkout")
    checkout.click()
    driver.find_element(By.XPATH,
                        "//input[@type='radio' and @value='Collection']").click()
    payment = driver.find_element(By.NAME, "proceed_to_payment")
    payment.click()
    driver.find_element(By.XPATH,
                        "//input[@type='radio' and @value='Pay On Collection']")


def test_customer_pays_on_collection(driver):
    marvin = Customer.with_name("Marvin")
    order = Order.from_data(pizza_type="Margherita",
                            size="Medium",
                            customer=marvin,
                            delivery=Delivery.Collection)
    order_id = order.create()
    driver.get(f"http://test.wimp.com/payment/{order_id}")
    payment_options = driver.find_element(By.XPATH,
        "//input[@type='radio' and @name='PaymentOptions']")
    assert "On Collection" in payment_options.text


def open_order_page(driver, order):
    return OrderPage()


def test_pay_on_collection(driver):
    marvin = Customer.with_name("Marvin")
    order = Order.from_data(pizza_type="Margherita",
                            size="Medium",
                            customer=marvin,
                            delivery=Delivery.Collection)
    order_page = open_order_page(driver, order)
    payment_page = order_page.proceed_to_payment()
    assert "Pay on Collection" in payment_page.payment_options()
