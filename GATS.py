from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
chromeOptions = webdriver.ChromeOptions()
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

url = "https://gats.pjm-eis.com/GATS2/PublicReports/RPSRetiredCertificatesReportingYear"

state = 'DC'  # Enter State Name Here
compliance_period = 'Jan 2020 - Dec 2020'   # Enter Compliance Period Here

driver.get(url)
wait.until(EC.element_to_be_clickable((By.XPATH, '(//*[@class="dxEditors_edtDropDown_GATS2"])[1]'))).click()  # Clicking on Dropdown Arrow Down Icon
wait.until(EC.element_to_be_clickable((By.XPATH, '//tr[@class="dxeListBoxItemRow_GATS2"]//td[text()="' + state + '"]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '(//*[@class="dxEditors_edtDropDown_GATS2"])[2]'))).click()  # Clicking on Dropdown Arrow Down Icon
wait.until(EC.element_to_be_clickable((By.XPATH, '//tr[@class="dxeListBoxItemRow_GATS2"]//td[text()="' + compliance_period + '"]'))).click()
driver.find_element(By.XPATH, '//*[text()="Submit"]').click()
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="CSV0Img"]'))).click()
print("Successfully Downloaded!")

time.sleep(10)
driver.quit()
