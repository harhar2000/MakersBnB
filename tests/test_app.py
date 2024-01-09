from playwright.sync_api import Page, expect

# Tests for your routes go here

""" we can render the homepage """

def test_get_homepage(page, test_web_address):
    page.goto(f"http://{test_web_address}/index")

    strong_tag = page.locator("h1")

    expect(strong_tag).to_have_text("MakersBnB")

""" we need to see a list of spaces """

def test_get_spaces(page, test_web_address):
    page.goto(f"http://{test_web_address}/index")

    strong_tag = page.locator("p")
# 'test space name', 'test space description', 1, 1
    expect(strong_tag).toContainText("Space Name: test space name")