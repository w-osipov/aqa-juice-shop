import pytest
from playwright.sync_api import Page

@pytest.fixture
def open_registration_page(page: Page):
    # Открываем страницу
    page.goto("http://localhost:3000/#/register")
    
    # Ждем появления кнопки закрытия баннера и кликаем. Если баннера нет — идем дальше.
    try:
        page.get_by_label("Close Welcome Banner").click(timeout=2000)
    except:
        pass
        
    return page
