from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_get_index(page, test_web_address, db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f"http://{test_web_address}/index")

    h1_tag = page.locator("h1")

    expect(h1_tag).to_have_text("This is the homepage.")

    sign_up_tag = page.locator("h2")
    expect(sign_up_tag).to_have_text("Sign up to MakersBnb!")

    
    
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



def test_post_login(page, test_web_address, db_connection):
    page.set_default_timeout(1000)  
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/login")
    page.fill('input[name=user_name]', "User Name")
    page.fill('input[name=user_password]', "Password")
    page.click('text="Login"')
    user_tag = page.locator(".t-user")
    assert user_tag.inner_text().strip() == "User Name"
    pass_tag = page.locator(".t-password")
    assert pass_tag.inner_text().strip() == "Password"
    login_element = page.locator(".t-login")
    assert login_element.is_visible()
    login_button = login_element.locator('input[type="submit"][value="Login"]')
    assert login_button.is_visible()


def test_get_list_of_spaces(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces")

    strong_tag = page.locator("h1")

    expect(strong_tag).to_have_text("MakersBnB")

""" we need to see a list of spaces with space name, description and price """

def test_get_space_name(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces")

    space_name_p = page.locator("div > p:has-text('Space Name: test space name')")

    expect(space_name_p).to_be_visible()

def test_get_space_description(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces")

    space_name_p = page.locator("div > p:has-text('Description: test space description')")

    expect(space_name_p).to_be_visible()


""" we want to see a button """

def test_list_a_space_button(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces")
    page.click("text='List a Space'")
    #page.screenshot(path="screenshot.png", full_page = True)

    space_name_p = page.locator("body > h1:has-text('List a Space')")
    
    expect(space_name_p).to_be_visible()


""" List a space form adds data to the spaces database"""

def test_list_a_space_adds_a_space(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f"http://{test_web_address}/list_a_space")

    page.fill('input[name=space_name]', "My House")
    page.fill('input[name=space_description]', "Spacious Room")
    page.fill('input[name=price]', "20")
    page.click("text='Create Space'")
    page.goto(f"http://{test_web_address}/spaces")

    page.screenshot(path="screenshot_2.png", full_page=True)

    space_name_p = page.locator("div > p:has-text('Space Name: My House')")

    expect(space_name_p).to_be_visible()



