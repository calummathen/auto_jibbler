from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from random import randint
import os

username = os.getenv('MY_USERNAME')
password = os.getenv('MY_PASSWORD')
driver = webdriver.Chrome()

def close_popups(driver):
    try:
        # Try finding common close button selectors
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="close"], .close, .popup-close'))
        )
        close_button.click()
        print("Closed a pop-up.")
    except Exception:
        print("No pop-up found.")
        
# Open the jibble page
driver.get("https://web.jibble.io/dashboard")

# Locate the username and password input fields
username_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Email or Phone number"]'))
    )
password_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Password"]'))
    )

# Send the username and password
username_input.send_keys(username)  
password_input.send_keys(password) 
password_input.send_keys(Keys.RETURN)  


# Attempt to close any pop-ups before moving to the next step
close_popups(driver)

# Locate and click clock in button
clock_in_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="button-clock-in"]'))
    )
clock_in_button.click()

# Locate time input section
time_in_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="h:mm a"]'))
    )
time_in_input.click()

WebDriverWait(driver, 10).until(
    EC.visibility_of(time_in_input)
)

actions = ActionChains(driver)
actions.send_keys(Keys.BACKSPACE).perform()

# Enter check in time
time_in_input.send_keys("9")
random_log_in_time = randint(1, 30)
actions.send_keys(Keys.ARROW_RIGHT).perform()
time_in_input.send_keys(str(random_log_in_time))
actions.send_keys(Keys.ARROW_RIGHT).perform()
time_in_input.send_keys("am")

# Select correct cohort
cohort_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="select-activity"]'))
    )

actions.click()

foundations_ra = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid=\"Foundations RA Sept '24\"]"))
    )
foundations_ra.click()

# Save button
save_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="right-sidebar-confirm-btn"]'))
    )

save_button.click()
time.sleep(2)

# Exit
driver.quit()

print("Successfully Jibbled In")

