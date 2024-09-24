# This entire line of code can be handled using pytest plugins
"""
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
"""
from playwright.sync_api import Page, expect


def test_basic_duckduckgo_search(page: Page):
    # Given the duckduckgo search page displayed
    page.goto("https://www.duckduckgo.com", )
    # When the user search for phrase
    page.locator('id=searchbox_input').fill('panda')
    # page.fill('id=searchbox_input', 'panda')  # alternative to add input text

    page.get_by_label('Search', exact=True).click()

    # Then search result contains phrase
    expect(page.locator('input.search__input--adv')).to_have_value('panda')
    # And the search result links also contains searched phrase
    page.locator('data-testid=result-title-a').nth(4).wait_for()  # explicit wait
    titles = page.locator('data-testid=result-title-a').all_text_contents()
    matches = [title for title in titles if 'panda' in title.lower()]
    assert len(matches) == 10, 'Invalid no of links'

    # And the search result title contain searched phrase
    expect(page).to_have_title("panda at DuckDuckGo")
