from playwright.sync_api import Page, expect

# Tests for your routes go here

""" we can render the homepage """

def test_get_homepage(page, test_web_address):
    page.goto(f"http://{test_web_address}/index")

    strong_tag = page.locator("h1")

    expect(strong_tag).to_have_text("MakersBnB")

""" we need to see a list of spaces with space name, description and price """

def test_get_space_name(page, test_web_address):
    page.goto(f"http://{test_web_address}/index")

    space_name_p = page.locator("div > p:has-text('Space Name: test space name')")

    expect(space_name_p).to_be_visible()

def test_get_space_description(page, test_web_address):
    page.goto(f"http://{test_web_address}/index")

    space_name_p = page.locator("div > p:has-text('Description: test space description')")

    expect(space_name_p).to_be_visible()


""" we want to see a button """

def test_list_a_space_button(page, test_web_address):
    page.goto(f"http://{test_web_address}/index")
    page.click("text='List a Space'")

    space_name_p = page.locator("div > h1:has-text('List a Space')")
    expect(space_name_p).to_be_visible()
