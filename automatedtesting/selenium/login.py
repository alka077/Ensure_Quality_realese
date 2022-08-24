from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
# --uncomment when running in Azure DevOps.
options = ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
# Start the browser and login with standard_user
def login (user, password):
    print ('Starting the browser...')
    driver.get('https://www.saucedemo.com/')
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.find_element_by_css_selector("input[id = 'user-name']").send_keys(user)
    print ('user name is entered in the user text field.')
    driver.find_element_by_css_selector("input[id = 'password']").send_keys(password)
    print ('password is entered in the password text fields')

    driver.find_element_by_css_selector("input[id= 'login-button']").click()
    print ('user is successfully logged in as ' +user)

def add_to_cart():
    print ('adding all the items to cart....')
    items = driver.find_elements_by_css_selector("button[class='btn btn_primary btn_small btn_inventory']")
    #print (items)
    for item in items:
        product = item.get_property('name')
        item.click()
        print (product + ' added to cart')
        
def remove_from_cart():
    print('remove all item from the cart...')
    items = driver.find_elements_by_css_selector("button[class='btn btn_secondary btn_small btn_inventory']")
    #print (items.count())
    for item in items:
        product = item.get_property('name')
        item.click()
        print(product + ' removed from the cart')

login('standard_user', 'secret_sauce')
add_to_cart()
remove_from_cart()