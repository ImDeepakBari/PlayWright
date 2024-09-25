from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # initiate a browser context
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()

    # adding page object to browser context
    page = context.new_page()

    # navigating to website
    page.goto('https://chatgpt.com/')

    # search for phrase in search input field
    page.locator(".placeholder").fill("Tell me about SpaceX program in 100 words.")
    page.get_by_label('Send prompt', exact=True).click()

    context.close()






