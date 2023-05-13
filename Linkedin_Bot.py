# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 01:32:05 2021

@author: Somaskandan
"""
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import pyautogui as pag
import time
import logging
#from logging.config import dictConfig
#logging.basicConfig(filename='C:\Users\Vignesh\OneDrive\Documents\LinkedIn_Bot\Linkedin_bot_log.log',level=logging.debug,format='%(levelname)s %(asctime)s ::%(message)s',)
network_url = ""
Total_request =[]
def main():
    url =  "https://linkedin.com/"    
    driver = webdriver.Chrome("C:\Program Files\Webdriver\chromedriver.exe")
    no_of_request = int(input("No. of Request : "))
    email_ID = input("Enter the email ID : ")
    passwords = input("Enter the password : ")
    start_bot(driver, url, no_of_request, email_ID, passwords)
    
def  start_bot(driver,url,no_of_request,email_ID, passwords):
    driver.get(url)
    login_to_linkedin(driver, email_ID, passwords)
    #no_of_request = int(input("No. of Request : "))
    n = int(no_of_request / 10)      
    connection_type = int(input("Which Connection type : "))
    for i in range(1, 100):
        if connection_type == 2:
            network_url = f'https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page={i}'
        elif connection_type == 3:
            network_url = f'https://www.linkedin.com/search/results/people/?network=%5B%22O%22%5D&origin=FACETED_SEARCH&page={i}'
        goto_network_page(driver, network_url)
        send_requests(driver, no_of_request)
        #print(send_requests.Total)
    
def login_to_linkedin(driver, email_ID, passwords):
    username = driver.find_element(By.ID, "session_key")
    username.send_keys(email_ID)
    password = driver.find_element(By.ID, "session_password")
    password.send_keys(passwords)
    driver.find_element(By.CLASS_NAME , "sign-in-form__submit-button").click()
    logging.info('Successfully logged in to the account')
        
def  goto_network_page(driver, network_url):
    driver.get(network_url)    
    time.sleep(2)
    
    
def send_requests(driver, no_of_request):
    all_buttons = driver.find_elements(By.TAG_NAME, 'button')    
    time.sleep(2)
    connect_buttons = [btn for btn in all_buttons if btn.text == "Connect" ]    
    connect_button_count = len(connect_buttons)
    print("connect_button_count: " , connect_button_count)
    #Total_request =  []
    Total_request.append(connect_button_count)
    print(Total_request)
    Total = sum(i for i in Total_request)
        #print(type(Total_request))
    print("Total_request: " , Total)
    if Total <=  no_of_request :
       for btn in connect_buttons:        
            time.sleep(5)        
            try:    
                driver.execute_script('arguments[0].click();', btn)            
                time.sleep(2)
                send = driver.find_element(By.XPATH,"//button[@aria-label='Send now']")            
                driver.execute_script('arguments[0].click();', send)           
                time.sleep(2)            
            except StaleElementReferenceException as Exception:
                logging.error('StaleElementReferenceException while trying to click the button')
                driver.execute_script('arguments[0].click();', btn)
                time.sleep(2)
                send = driver.find_element(By.XPATH,"//button[@aria-label='Send now']")            
                driver.execute_script('arguments[0].click();', send)            
                time.sleep(2)
    else:
        print("Quit!!")
        driver.quit()
        driver.close()

main()


print("Success!!")

