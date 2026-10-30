import pytest
import time
from playwright.sync_api import Page

def test_successful_registration(open_registration_page: Page):
    page = open_registration_page
    
    # 1. Заполняем Email
    page.locator("#emailControl").fill("tester_node_qa@gmail.com")
    
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
    
    page.wait_for_timeout(3000)

def test_github_ci_check(page: Page):
    page.goto("https://github.com")
    assert "GitHub" in page.title()
