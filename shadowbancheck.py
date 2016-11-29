import logging
import time, re, random, datetime, random
from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys
from subprocess import call
import urllib, urllib2
from bs4 import BeautifulSoup, Comment

driver = webdriver.Firefox()
usernames=rawinput()

def NullProgram():
	driver.get('http://nullprogram.com/am-i-shadowbanned/')
	print ('Opened Reddit')

def Startup():
	print ("Entering Username")
	username = driver.find_element_by_xpath('/html/body/form/input[1]')
	time.sleep(1)
	print ('Inputting Username')
	username.send_keys(usernames)
	username.send_keys(Keys.RETURN)
	time.sleep(1)



	
NullProgram()
Startup()
