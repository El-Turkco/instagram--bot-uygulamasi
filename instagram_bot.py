
from os import link
from selenium import webdriver
from user_info import username
from user_info import password
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    driver=webdriver.Chrome()
    
    def __init__(self,username,password):
        self.username = username
        self.password=password
        self.browser = webdriver.Chrome()

    def sigIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        usernameInput = self.browser.find_element_by_name("username")
        passwordInput = self.browser.find_element_by_name("password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)


        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)
        if  self.browser.find_element_by_class_name("cmbtv"):
             el = self.browser.find_element_by_class_name("cmbtv")
             el.find_element_by_tag_name("button").click()


        if self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click():
            self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()

    def getFollowers(self,max):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(1)
        self.browser.find_element_by_class_name("k9GMp").find_element_by_tag_name("a").click()
        time.sleep(1)

        modal = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        count = len( modal.find_elements_by_tag_name("li"))

        action = webdriver.ActionChains(self.browser)

        print(f"Number of followers: {count}")

        while count < max:
            modal.click()

            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)

            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)

            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)

            newCount = len( modal.find_elements_by_tag_name("li"))

            if count != newCount:
                count = newCount
                print(f"Takipçi sayisi: {count}")
                time.sleep(1)
            else:
                break

        i = 0
        followers= modal.find_elements_by_tag_name("li")
        for user in followers:
            i += 1
            print(i)
            link = user.find_element_by_tag_name("a").get_attribute("href")
            print(link)

    def followUser(self, username):
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(1)
        followButton = self.browser.find_element_by_class_name("_5f5mN")
        if followButton.text == "Follow":
            followButton.click()
            time.sleep(2)
        else:
            print(f"{username}follow user you are already following.")

    def followUsers(self,users):
        for user in users:
            self.followUser(user)

    def unFollowUser(self,username):
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(1)
        unfollowButton = self.browser.find_element_by_class_name("_5f5mN").click()
        if self.browser.find_element_by_class_name("_1XyCr"):
            unfollowbutton = self.browser.find_element_by_class_name("_1XyCr")
            unfollowbutton.find_element_by_tag_name("button").click()

        if self.browser.find_element_by_class_name("aOOlW -Cab_").click():
            self.browser.find_element_by_class_name("aOOlW -Cab_").click()
            print("You unfollowed the user")
       

    def __del__(self):
        time.sleep(10)
        self.browser.close()

app=Instagram(username,password)

app.sigIn()
app.getFollowers(100)
app.followUser("linkedin")
app.followUsers(["kod_evreni","python.hub"])
app.unFollowUser("username")
