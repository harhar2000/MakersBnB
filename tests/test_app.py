from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    
    page.goto(f"http://{test_web_address}/index")

    
    strong_tag = page.locator("p")

    
    expect(strong_tag).to_have_text("This is the homepage.")

def test_get_login(page, test_web_address):
    
    page.goto(f"http://{test_web_address}/login")

    
    strong_tag = page.locator("p")

    
    expect(strong_tag).to_have_text("user")
    expect(strong_tag).to_have_text("password")
    expect(strong_tag).to_have_text("Login")
    