import pytest
import time
import uuid
from playwright.sync_api import Page, expect

def test_successful_registration(open_registration_page: Page):
    page = open_registration_page
    
    # 1. Заполняем Email (уникальный при каждом запуске)
    page.locator("#emailControl").fill(f"tester_node_qa+{uuid.uuid4().hex[:8]}@gmail.com")
    
    # 2. Сначала работаем с выпадающим списком (чтобы фокус не сбивал пароли)
    page.locator("mat-select[name='securityQuestion']").click(force=True)
    page.locator("mat-option").first.click(force=True)
    
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

def test_github_ci_check(page: Page):
    page.goto("https://github.com")
    assert "GitHub" in page.title()
