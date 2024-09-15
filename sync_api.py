from playwright.sync_api import sync_playwright

with sync_playwright() as sync_p:
    browser = sync_p.firefox.launch(headless=False, slow_mo=500)

    page = browser.new_page()
    page.goto("https://www.hackerrank.com/")
    assert 'HackerRank - Online Coding Tests and Technical Interviews' == page.title()
    browser.close()




