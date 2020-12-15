from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class gmailSignIn:
    def signInVerification(self):
        url = "http://gmail.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(7)
        email_Id = driver.find_element(By.NAME, "identifier")      # Signing in on Gmail
        email_Id.send_keys("smritishreyanshi@gmail.com")
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-RLmnJb")
        next_button.click()
        passwd = driver.find_element(By.NAME, "password")
        passwd.send_keys("Smriti@123")
        nxt_btn = driver.find_element(By.CLASS_NAME, "VfPpkd-RLmnJb")
        nxt_btn.click()
        fe = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
                                                                             ElementNotVisibleException,
                                                                             ElementNotSelectableException])
        element = fe.until(EC.element_to_be_clickable((By.XPATH, '//div[@class = "T-I T-I-KE L3"]')))
        element.click()

#Composing mail

        toRecipients = driver.find_element(By.ID, ":d4")
        toRecipients.send_keys("aparnachaurasia123@gmail.com")
        subj = driver.find_element(By.NAME, "subjectbox")
        subj.send_keys("Testing mail")
        body = driver.find_element(By.ID, ":dy")
        body.send_keys("Sending a trial mail. Pls ignore.")
        sendMsg = driver.find_element(By.ID, ":cj")
        sendMsg.click()                                        # Message sent successfully.


obj1 = gmailSignIn()
obj1.signInVerification()