from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address, db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f"http://{test_web_address}/index")

    # login_tag = page.locator(".t-login")
    # expect(login_tag).to_have_text("Login | About")

    h1_tag = page.locator("h1")

    expect(h1_tag).to_have_text("This is the homepage.")

    sign_up_tag = page.locator("h2")
    expect(sign_up_tag).to_have_text("Sign up to MakersBnb!")


"""
We can render the signup page
"""

def test_get_signup(page, test_web_address, db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f"http://{test_web_address}/index")
    page.click("text='Sign up to MakersBnb!'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Sign up to MakersBnb!")


def test_get_about(page, test_web_address, db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f"http://{test_web_address}/index")
    page.click("text='| About'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("About MakersBnB")


def test_visit_sign_up_page_go_back(page, test_web_address):
    page.goto(f"http://{test_web_address}/index")
    page.click("text='Sign up to MakersBnb!'")
    page.click("text='Back to Homepage!'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("This is the homepage.")



"""
We can create a new user from the signup page
"""
def test_create_new_user(page, test_web_address, db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f"http://{test_web_address}/index")
    page.click("text='Sign up to MakersBnb!'")

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Sign up to MakersBnb!")

    page.fill("input[name=user_name]", "test user name")
    page.fill("input[name=email]", "test email")
    page.fill("input[name=user_password]", "test user password")

    page.click("text='Submit'")

