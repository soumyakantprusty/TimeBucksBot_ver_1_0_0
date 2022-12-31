import random
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException, StaleElementReferenceException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from multiprocessing import Process
import time
import webbrowser
import pyautogui
import time

class TimeBucksBots:
    def __init__(self):
        super(TimeBucksBots, self).__init__()
        self.clicktoplay_url = "https://timebucks.com/publishers/index.php?pg=earn&tab=view_content_ads"
        self.slidetoplay_url = "https://timebucks.com/publishers/index.php?pg=earn&tab=view_content_timecave_slideshows"
        self.username = " "
        self.password = " "
        self.taskregister=pd.DataFrame()
        self.taskname=[]
        self.taskcost=[]
        self.engagedhits_pic_path_list=["C:\\Users\\sam\\Documents\\grocerycomparatorrobot\\ext_btn.png",
                                        "C:\\Users\\sam\\Documents\\grocerycomparatorrobot\\engagedhits.png",
                                        "C:\\Users\\sam\\Documents\\grocerycomparatorrobot\\ggle_login_btn.png",
                                        "C:\\Users\\sam\\Documents\\grocerycomparatorrobot\\googleact_btn.png",
                                        "C:\\Users\\sam\\Documents\\grocerycomparatorrobot\\ext_btn.png",
                                        "C:\\Users\\sam\\Documents\\grocerycomparatorrobot\\engagedhits.png",
                                        "C:\\Users\\sam\\Documents\\grocerycomparatorrobot\\earnmoney_btn.png"
                                        ]
        print("Initiating selenenium webdriver Options")
        self.options = webdriver.ChromeOptions()
        self.prefs = {"credentials_enable_service": False,
                 "profile.password_manager_enabled": False}

    def startwebdriver(self):
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-notifications")
        self.options.add_argument('--ignore-ssl-errors=yes')
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument("user-data-dir=C:\\Users\\sam\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\")
        self.options.add_experimental_option("useAutomationExtension", False)
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("prefs", self.prefs)
        self.driver_timesbuck = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                                 chrome_options=self.options)
        print("Successfully Initiated selenenium webdriver Options")
        time.sleep(1)
        print("Starting the Supervisor Bot")
        credentials = pd.read_csv("C:\\Users\\sam\\Documents\\grocerycomparatorrobot\\timebuckscredentials.csv")
        for index, row in credentials.iterrows():
            print("username:" + row['username'])
            self.username = row['username']
            print("password:" + row['password'])
            self.password = row['password']

        self.driver_timesbuck.get("https://timebucks.com/")
        self.driver_timesbuck.maximize_window()
        time.sleep(5)
        try:
            username = WebDriverWait(self.driver_timesbuck, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="username_box"]')))
            time.sleep(5)
            username.send_keys(self.username)
            time.sleep(5)
            password = WebDriverWait(self.driver_timesbuck, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="password_box"]')))
            password.send_keys(self.password)
            time.sleep(10)
            WebDriverWait(self.driver_timesbuck, 20).until(
                    EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='reCAPTCHA']")))
            WebDriverWait(self.driver_timesbuck, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()
            time.sleep(30)
            self.driver_timesbuck.switch_to.parent_frame()
            WebDriverWait(self.driver_timesbuck, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div[1]/form/input[5]'))).click()
        except TimeoutException:
            try:
                WebDriverWait(self.driver_timesbuck, 20).until(
                        EC.frame_to_be_available_and_switch_to_it((By.ID, "ifrmCookieBanner")))
                time.sleep(8)
                WebDriverWait(self.driver_timesbuck, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="grouped-pageload-Banner"]/div/div/div/div[3]/button[2]'))).click()
                time.sleep(5)
                self.driver_timesbuck.switch_to.parent_frame()
            except TimeoutException:
                print("ClickToPay Bot:No Cookie Banner")
        print("Successfully initiated Supervisor Bot")
        executor_url = self.driver_timesbuck.command_executor._url
        session_id = self.driver_timesbuck.session_id
        return self.engagedhits_pic_path_list,self.taskcost,self.taskname,self.taskregister,self.driver_timesbuck ,executor_url,session_id
def engagedhits(picpaths,confidence):
    buttonlocation = pyautogui.locateOnScreen(
        picpaths, confidence=confidence)
    buttonlocation_center = pyautogui.center(buttonlocation)
    button_x, button_y = buttonlocation_center
    pyautogui.click(button_x, button_y)



def bot(executor_url, session_id,taskcost,taskname,taskregister,engagedhits_pic_path_list):
    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("--enable-file-cookies")
    capabilities = options.to_capabilities()
    bot_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=capabilities)
    bot_driver.close()
    bot_driver.session_id = session_id
    initiatebotcounter=0
    while 0 < 1:
        if(initiatebotcounter==0):
            random_int = 2
            initiatebotcounter=initiatebotcounter+1
        else:
            random_int = random.randint(0, 4)
        random_sleeptime=random.randint(8, 17)
        random_sleeptime2 = random.randint(5, 8)

        if random_int == 0:
            try:
                bot_driver.get('https://timebucks.com/publishers/index.php?pg=earn&tab=view_content_ads')
                time.sleep(random_sleeptime)
                numberofclicksavailable = WebDriverWait(bot_driver, 10).until(EC.visibility_of_element_located(
                                                                        (By.ID, 'clicksTotalOffers'))).text
                print("No of Ads available:{adsavailable}".format(adsavailable=numberofclicksavailable,))
                for ads in range(int(numberofclicksavailable)):
                    try:
                        advmsg = WebDriverWait(bot_driver, 10).until(EC.visibility_of_element_located(
                                (By.XPATH, '//*[@id="viewAdsTOffers1"]/tbody/tr/td[2]/p[1]'))).text
                        print(advmsg)
                    except TimeoutException:
                        time.sleep(2)
                    try:
                        clickprice = WebDriverWait(bot_driver, 10).until(EC.visibility_of_element_located(
                                        (By.XPATH, '//*[@id="viewAdsTOffers1"]/tbody/tr/td[3]'))).text
                        print("click price:" + clickprice)
                    except TimeoutException:
                        print("unable to fetch click price")

                    clickwait_msg = WebDriverWait(bot_driver, 10).until(
                                        EC.visibility_of_element_located(
                                            (By.XPATH, '//*[@id="viewAdsTOffers1"]/tbody/tr/td[2]/span/span')))
                    clickwaittime_msg_splits = clickwait_msg.text.split()
                    viewclick = WebDriverWait(bot_driver, 10).until(EC.visibility_of_element_located(
                                    (By.XPATH, '//*[@id="viewAdsTOffers1"]/tbody/tr/td[4]/div/a[1]/span/input')))
                    viewclick.click()

                    time.sleep(random_sleeptime)
                    adactivetime = 0
                    for items in clickwaittime_msg_splits:
                        if (items.isnumeric()):
                            adactivetime = items
                    time.sleep(int(adactivetime) + 5)

                    initiatebotcounter = initiatebotcounter + 1
                    parent = bot_driver.window_handles[0]
                    child = bot_driver.window_handles[1]
                    bot_driver.switch_to.window(child)
                    bot_driver.close()
                    bot_driver.switch_to.window(parent)
                    try:
                        WebDriverWait(bot_driver, 5).until(
                            EC.alert_is_present())  # this will wait 5 seconds for alert to appear
                        alert = bot_driver.switch_to.alert  # or self.driver.switch_to_alert() depends on your selenium version
                        alert.accept()
                        print("Ad Expired.")
                    except TimeoutException:
                        taskname.append("Ad Click")
                        taskcost.append(clickprice)
            except TimeoutException:
                print("The Click Button not found")
                initiatebotcounter = initiatebotcounter + 1
            except UnexpectedAlertPresentException:
                print("click ad expired")
                initiatebotcounter = initiatebotcounter + 1
                if len(bot_driver.window_handles) > 1:
                    parent = bot_driver.window_handles[0]
                    child = bot_driver.window_handles[1]
                    bot_driver.switch_to.window(child)
                    bot_driver.close()
                    bot_driver.switch_to.window(parent)
                else:
                    bot_driver.refresh()


        elif random_int == 1:
            try:
                bot_driver.get("https://timebucks.com/redirects/PushClicks.php")
                bodymsg = bot_driver.find_element(By.TAG_NAME, value="body")
                sleeptime = int(bodymsg.text.split(" ")[10])
                print("The next push to click will come at {sleeptime}".format(sleeptime=sleeptime,))

            except (ValueError, TimeoutException,UnexpectedAlertPresentException):
                time.sleep(random_sleeptime)
                WebDriverWait(bot_driver, 20).until(
                    EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='reCAPTCHA']")))
                WebDriverWait(bot_driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()
                time.sleep(30)
                print("Successfully clicked")
                taskname.append("PushClick")
                taskcost.append("0.001")


        elif random_int == 2:
            bot_driver.get('https://timebucks.com/publishers/index.php?pg=earn&tab=view_content_timecave_slideshows')
            time.sleep(random_sleeptime)
            try:
                noofslideavailable = WebDriverWait(bot_driver, 10).until(EC.visibility_of_element_located(
                            (By.ID, 'totalOffersRemainingToday'))).text
                if noofslideavailable == '':
                    noofslideavailable=0
            except:
                noofslideavailable=0

            if int(noofslideavailable)==0:
                print("No slide left to watch")
            else:
                randomsleep_internal=random.randint(8, 12)
                print("Number of slide left:{slidecount}".format(slidecount=noofslideavailable,))
                try:
                    viewbutton = WebDriverWait(bot_driver, 10).until(EC.visibility_of_element_located(
                        (By.XPATH, '//*[@id="viewTimecaveTOffers"]/tbody/tr/td[5]/div/a/span/input')))
                    viewbutton.click()
                    parent = bot_driver.window_handles[0]
                    # obtain browser tab window
                    child = bot_driver.window_handles[1]
                    time.sleep(randomsleep_internal)
                    bot_driver.switch_to.window(child)
                    time.sleep(randomsleep_internal)
                    try:
                        WebDriverWait(bot_driver, 20).until(
                            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='reCAPTCHA']")))
                        WebDriverWait(bot_driver, 20).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()
                        time.sleep(30)
                    except TimeoutException:
                        print(bot_driver.title)
                        for slidecounter in range(7):
                            print("Page No:{pagenumber}".format(pagenumber=slidecounter,))
                            time.sleep(20)
                            nextslidebtn = WebDriverWait(bot_driver, 25).until(
                                EC.presence_of_all_elements_located((By.ID, 'next_slide')))
                            for item in nextslidebtn:
                                try:
                                    item.click()
                                except:
                                    time.sleep(5)
                        taskname.append("Slide")
                        taskcost.append("0.001")
                    bot_driver.close()
                    bot_driver.switch_to.window(parent)
                    bot_driver.refresh()
                except Exception as e:
                    timeleftfornextslide=WebDriverWait(bot_driver, 10).until(EC.visibility_of_element_located(
                                            (By.ID, 'totalTimeRemaining'))).text
                    print("Time left for next slide to be available is :{timeleftfornextslide}".format(timeleftfornextslide=timeleftfornextslide,))
        elif random_int == 3:
            url = 'google.com'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new(url)
            for links in engagedhits_pic_path_list:
                engagedhits(links,0.9)
                time.sleep(20)

















if __name__ == '__main__':
    print ("Bot program started")
    webdriverclass=TimeBucksBots()
    engagedhits_pic_path_list,taskcost,taskname,taskregister,chrome_driver,executor_url,session_id=webdriverclass.startwebdriver()
    #executor_url = chrome_driver.command_executor._url
    #session_id = chrome_driver.session_id
    print("The url is  {url} and sessionid is {session_id}".format(url=executor_url,session_id=session_id))
    bot(executor_url,session_id,taskcost,taskname,taskregister,engagedhits_pic_path_list)





