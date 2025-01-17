from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
import manager as mg

ACCOUNT_EMAIL = mg.ACCOUNT_EMAIL
ACCOUNT_PASSWORD = mg.ACCOUNT_PASSWORD
PHONE = mg.PHONE


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


# Optional - Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3586148395&f_LF=f_AL&geoId=101356765&"
           "keywords=python&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")

# Click Reject Cookies Button
time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()

# Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# CAPTCHA - Solve Puzzle Manually
input("Press Enter when you have solved the Captcha")

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()

















# MAIL = "dhonikohli0718at@gmail.com"
# PASSWORD = "dhonikohli0718"
# PHONE = "6374250988"
#
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3823155509&f_LF=f_AL&geoId=102257491&keywords=python'
#            '%20developer&location=London%2C%20England%2C%20United%20Kingdom')
#
# # Click Reject Cookies Button
# # time.sleep(2)
# # reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
# # reject_button.click()
#
# # Click Sign in Button
# time.sleep(2)
# sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
# sign_in_button.click()
#
# # getting the entry and login feilds
# user_name = driver.find_element(By.NAME, value="session_key")
# password = driver.find_element(By.NAME, value="session_password")
# # sign_in = driver.find_element(By.XPATH, value='//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
#
# # entering the values to sign up
#
# user_name.send_keys(MAIL)
# password.send_keys(PASSWORD, Keys.ENTER)
# # sign_in.click()
#
# easy_apply = driver.find_element(By.ID, value="ember395")
# easy_apply.click()
# # //*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3831057871-112756579-phoneNumber-nationalNumber"]
#
# ph_no = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs'
#                                             '-applyformcommon-easyApplyFormElement-3823155509-111429186-phoneNumber'
#                                             '-nationalNumber"]')
# ph_no.send_keys(PHONE)
#
# # clicking next Button
# next = driver.find_element(By.ID, value="ember709")
# next.click()
# next.click()
# # experience
#
# exp = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs'
#                                           '-applyformcommon-easyApplyFormElement-3823155509-111429234-numeric"]')
# exp.send_keys("1")
#
# # clicking review button
#
# review = driver.find_element(By.ID, value="ember762")
# review.click()
#
# # submitting the application
#
# submit = driver.find_element(By.ID, value="ember772")
# submit.click()