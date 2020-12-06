from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from random import randint

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

sleep(2)

username_input = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
username_input.send_keys("checkmyinstabot")
password_input = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
password_input.send_keys("ryuga123!")

login_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
login_button.click()

not_now = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
not_now.click()

not_now2 = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
not_now2.click()

comments=['Hello !!!','Nice Pic','Hii Dosto']
while 1:
    browser.get("https://www.instagram.com/neha_rajput___143/")
    post_links = []
    soup = BeautifulSoup(browser.page_source,'html.parser')
    posts = soup.findAll('a')
    for post in posts:
        if '/p/' in post['href']:
            post_links.append(post['href'])
    sleep(1.5)
    browser.get("https://www.instagram.com/"+post_links[0])

    soup2 = BeautifulSoup(browser.page_source,'html.parser')
    so = soup2.find('div',class_="k_Q0X NnvRN")
    timer = so.find('time',class_="_1o9PC Nzb55").text

    if "second" in timer :
        comment=browser.find_element_by_class_name('X7cDz').click()
        sleep(1)
        browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").send_keys(comments[randint(0,2)])
        sleep(1)
        cmt_btn=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button")
        cmt_btn.click()

    sleep(30)

browser.close()
