import pytest
import time
import uuid
from playwright.sync_api import Page, expect

def test_successful_registration(open_registration_page: Page):
    page = open_registration_page
    
    # 1. Заполняем Email (уникальный при каждом запуске)
    page.locator("#emailControl").fill(f"tester_node_qa+{uuid.uuid4().hex[:8]}@gmail.com")
    
    # 2. Сначала работаем с выпадающим списком (чтобы фокус не сбивал пароли)
    page.get_by_role("combobox", name="Selection list for the security question").click()
    page.get_by_role("option").first.click()

    # 3. Заполняем ответ на вопрос
    page.locator("#securityAnswerControl").fill("My Answer")
    
    # 4. Заполняем пароли в самый последний момент перед кликом
    page.locator("#passwordControl").fill("P@ssword12345")
    page.locator("#repeatPasswordControl").fill("P@ssword12345")
    
    # 5. Нажимаем кнопку регистрации
    page.locator("#registerButton").click()
    
    # 6. Проверяем результат регистрации
    expect(page.get_by_text("Registration completed successfully")).to_be_visible()
    expect(page).to_have_url("http://localhost:3000/#/login")

def test_registration_password_mismatch(open_registration_page: Page):
    page = open_registration_page

    # 1. Email и два РАЗНЫХ пароля
    page.locator("#emailControl").fill(f"tester_node_qa+{uuid.uuid4().hex[:8]}@gmail.com")
    page.locator("#passwordControl").fill("Password123!")
    page.locator("#repeatPasswordControl").fill("Password456@")
    
    # 2 Уводим фокус, чтобы форма посчитала поле заполненным
    page.locator("#repeatPasswordControl").blur()
    
    # 3. Форма подсветила ошибку
    expect(page.get_by_text("Passwords do not match")).to_be_visible()

    # 4. Кнопка заблокирована
    expect(page.get_by_role("button", name="Button to complete the registration")).to_be_disabled()