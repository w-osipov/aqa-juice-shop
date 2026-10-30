import pytest
from playwright.sync_api import Page

def test_juice_shop_title_local(page: Page):
    page.goto("http://localhost:3000")
    assert "Juice Shop" in page.title()

def test_github_ci_check(page: Page):
    page.goto("https://github.com")
    assert "GitHub" in page.title()
