import requests
from time import sleep
from selenium import webdriver
from requests.auth import HTTPBasicAuth

#Create Daniel Baldelomar product
data = {
    "name": "Daniel Baldelomar",
    "type": "simple",
    "regular_price": "10",
    "description": "Daniel",
    "short_description": "Baldelomar"
}

response = requests.post("http://34.205.174.166/wp-json/wc/v3/products", data, auth=('shopmanager', 'axY2 rimc SzO9 cobf AZBw NLnX'))

#Navigate to new product
browser = webdriver.Chrome(r"C:\automation_framework\python_scripts\drivers\chromedriver.exe")
browser.get("http://34.205.174.166/product/daniel-baldelomar/")
sleep(5)

#Increase quantity to 7
browser.find_element_by_name('quantity').click()
browser.find_element_by_name('quantity').clear()
quan_btn = browser.find_element_by_name('quantity')
quan_btn.send_keys("7")

browser.find_element_by_name('add-to-cart').click()

browser.find_element_by_id('site-header-cart').click()

#Validate info
browser.get("http://34.205.174.166/cart/")
assert browser.page_source.find("Daniel Baldelomar")
assert browser.page_source.find("$10.00")
assert browser.page_source.find("$70.00")
sleep(5)

#Delete product
response = requests.delete("http://34.205.174.166/wp-json/wc/v3/products/{}/".format(response.json()["id"]), auth=('shopmanager', 'axY2 rimc SzO9 cobf AZBw NLnX'))

#Go Home
browser.get("http://34.205.174.166/")
if browser.find_element_by_class_name("search-field") != None:
	print("Search Box is Present")
else:
	print("Search Box is Absent")
	
#Search Hoodie
search_btn = browser.find_element_by_class_name("search-field")
search_btn.send_keys("Hoodie")
search_btn.submit()
sleep(5)

#Select Hoodie with Pocket
browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/main/ul/li[4]/a[1]/img").click()
sleep(5)

browser.close()