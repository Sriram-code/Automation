from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the URL
driver.get("https://nestle.service-now.com/now/nav/ui/classic/params/target/%24pa_dashboard.do")
time.sleep(3)

# Login flow (replace with your credentials)
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("email")
driver.find_element(By.ID, "idSIButton9").click()

time.sleep(2)  # Let password field load
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("password")
time.sleep(3)

driver.find_element(By.ID, "idSIButton9").click()  # After password
time.sleep(3)

driver.find_element(By.ID, "idSIButton9").click()  # For "Stay signed in?" prompt
time.sleep(20)  # Wait for dashboard to load fully

# Extract catalog task count
count = driver.find_element(By.XPATH, "//a[contains(text(),'Unassigned Catalog Tasks')]//parent::td/following::td[1]/a").text
print(count + " ***************************************")

# Close browser (optional)
# driver.quit()
