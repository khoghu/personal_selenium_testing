# selenium 4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


def verify_title():

    # Create ChromeOptions object
    chrome_options = Options()

    # Disable notifications
    chrome_options.add_argument("--disable-notifications")

    # Initialize the Chrome webdriver with the configured options
    driver = webdriver.Chrome(options=chrome_options)

    # Open Facebook
    driver.get("https://www.facebook.com")

    # Replace with your Facebook credentials and post text
    username = "khoghukill@gmail.com"
    password = "Kho3$prux"
    post_text = "Hello, this is a test post using Selenium!"

    # Find the username and password fields, and log in
    username_field = driver.find_element("name", "email")
    username_field.send_keys(username)

    password_field = driver.find_element("name", "pass")
    password_field.send_keys(password)

    login_button = driver.find_element("name", "login")
    login_button.click()

    # Wait for the home page to load
    time.sleep(5)

    # Get post element in home page
    post_box = driver.find_element("xpath", "//div[@aria-label='Create a post']/div[1]/div")
    post_input = post_box.find_element("xpath", "..")
    post_input.click()

    # Wait for the post box load
    time.sleep(2)

    # Get the privacy configuration
    post_privacy = driver.find_element("xpath", "//div[@role='button' and contains(@aria-label, 'Edit privacy.')]")
    privacy = post_privacy.get_attribute("aria-label")

    # If post privacy settings not on private
    if privacy != "Edit privacy. Sharing with Only me. ":
        post_privacy.click()

        # Wait for load post privacy setting tab
        time.sleep(2)

        # Change or select privacy settings to Only Me in radio selections
        only_me = driver.find_element("xpath", "//span[text()='Only me']")
        only_me_radio = only_me.find_element("xpath", "..")
        only_me_radio.click()

        # Click done after change
        done_button = driver.find_element("xpath", "//div[@role='button' and @aria-label='Done']")
        done_button.click()

        # Wait for load back to post tab
        time.sleep(2)

    # Get post textbox element in post tab
    post_text_area = driver.find_element("xpath", "//div[@role='textbox' and contains(@aria-label, 'on your mind,')]")
    post_text_area.send_keys(post_text)

    # Show or Trigger background options
    show_background_option = driver.find_element("xpath",
                                                 "//div[@role='button' and @aria-label='Show Background Options']")
    show_background_option.click()

    # Wait to load background options
    time.sleep(1)

    # Trigger or choose background options
    choose_background_option = driver.find_element("xpath",
                                                   "//div[@role='button' and @aria-label='Gradient, red blue, background']")
    choose_background_option.click()

    # Hide background options
    hide_background_option = driver.find_element("xpath",
                                                 "//div[@role='button' and @aria-label='Hide Background Options']")
    hide_background_option.click()

    # Show or Trigger emoji options
    show_hide_emoji_option = driver.find_element("xpath", "//div[@role='button' and @aria-label='Emoji']")
    show_hide_emoji_option.click()

    # Wait for load emoji options
    time.sleep(1)

    # Choose recently used first emoji
    recently_used_emoji_first = driver.find_element("xpath",
                                                    "//div[@role='rowgroup' and @aria-label='Recently Used']/div[2]/div/div[1]/div[@role='button']")
    recently_used_emoji_first.click()
    recently_used_emoji_first.click()

    # Hide or Trigger emoji options
    show_hide_emoji_option.click()

    # Get post button element in post tab
    post_button = driver.find_element("xpath", "//div[@role='button' and @aria-label='Post']")
    post_button.click()

    # Wait for the post to be published
    time.sleep(5)

    # Close the browser
    # driver.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    verify_title()
