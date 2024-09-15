from playwright.sync_api import sync_playwright

with sync_playwright() as sync_p:
    # assigning browser
    browser = sync_p.firefox.launch(headless=False, slow_mo=500)

    page = browser.new_page()  # creating a page for browser context
    page.goto("https://www.hackerrank.com/")  # navigating to url
    assert 'HackerRank - Online Coding Tests and Technical Interviews' == page.title()
    browser.close()




