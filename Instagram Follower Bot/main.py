from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


FOLLOW = "newslifetvkenya"

class InstagramFollower:

    def __init__(self):
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.follow_account = FOLLOW

    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(5)
        phone_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        phone_input.send_keys(os.environ['Phone'])
        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(os.environ['PASS'])
        press_login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        press_login.click()

    def search_follow(self):
        sleep(15)
        try:
            not_now = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
            not_now.click()
        except NoSuchElementException:
            print("Not Now Button Not Found")
        finally:
            sleep(10)
            try:
                no_notification = self.driver.find_element(By.CSS_SELECTOR, 'button._a9--._a9_0')
                no_notification.click()
            except NoSuchElementException:
                print("No Notification Button Found")
            finally:
                sleep(10)
                search = self.driver.find_element(By.CSS_SELECTOR, 'input._aauy')
                search.send_keys(FOLLOW)
                sleep(5)
                search.send_keys(Keys.ENTER)
                sleep(2)
                search.send_keys(Keys.ENTER)
                sleep(2)
                click_followers = self.driver.find_element(By.CSS_SELECTOR, 'a.qi72231t.nu7423ey.n3hqoq4p.r86q59rh.b3qcqh3k.fq87ekyn.bdao358l.fsf7x5fv.'
                                                                            'rse6dlih.s5oniofx.m8h3af8h.l7ghb35v.'
                                                                            'kjdc1dyq.kmwttqpk.srn514ro.oxkhqvkx.rl78xhln.nch0832m.cr00lzj9.rn8ck1ys.s3jn8y49.icdlwmnq._a6hd')
                try:
                    click_followers.click()
                except StaleElementReferenceException:
                    click_followers = self.driver.find_element(By.CSS_SELECTOR,
                                                               'a.qi72231t.nu7423ey.n3hqoq4p.r86q59rh.b3qcqh3k.fq87ekyn.bdao358l.fsf7x5fv.'
                                                               'rse6dlih.s5oniofx.m8h3af8h.l7ghb35v.'
                                                               'kjdc1dyq.kmwttqpk.srn514ro.oxkhqvkx.rl78xhln.nch0832m.cr00lzj9.rn8ck1ys.s3jn8y49.icdlwmnq._a6hd')
                    click_followers.click()
                sleep(5)
                follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button._acan._acap.acas")
                print(len(follow_buttons))
                followable = [button for button in follow_buttons if button.find_element(By.TAG_NAME, 'div').find_element(By.TAG_NAME, 'div').text == 'Follow']
                print(len(followable))
                for items in followable:
                    print(items)


bot = InstagramFollower()
bot.login()
bot.search_follow()