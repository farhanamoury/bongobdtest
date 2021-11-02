from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Windows\\System32\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://bongobd.com/")
driver.implicitly_wait(100000)
pageTitle = driver.title
print(pageTitle)
assert "Watch Live Tv, Bangla Movies, Natoks Anytime Anywhere" in pageTitle

#clickmovies
driver.find_element(By.XPATH,"//div[@id='root']//div//div//div//div//header//div//div//div//div//a//div//span[contains(text(),'Movies')]").click()
assert "movies" in driver.current_url
driver.implicitly_wait(2000)

#search
driver.find_element(By.XPATH,"//input[@aria-label='search']").send_keys("Panther")
driver.implicitly_wait(20)

#searchbutton
driver.find_element(By.XPATH,"//input[@aria-label='search']").click()
driver.find_element(By.XPATH,"//input[@aria-label='search']").send_keys(Keys.ENTER)
driver.implicitly_wait(20)


driver.find_element(By.XPATH,"//h4[contains(text(),'Panther')]").click()
assert "Panther" in driver.find_element(By.XPATH,"//h5[contains(text(),'Panther')]").text
driver.implicitly_wait(200)

#playbutton
#WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Play']"))).click()
driver.execute_script("document.getElementById('vod_html5_api').play()")

#pausebutton
#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@title='Pause']")))

driver.quit()