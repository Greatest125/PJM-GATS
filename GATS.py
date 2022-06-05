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


driver.get(url)
count_state = len(driver.find_elements(By.XPATH, '//table[@id="SelectedState0_DDD_L_LBT"]//tr'))
for i in range(1, count_state + 1):
    wait.until(EC.element_to_be_clickable((By.XPATH, '(//*[@class="dxEditors_edtDropDown_GATS2"])[1]'))).click()  # Clicking on Dropdown Arrow Down Icon
    wait.until(EC.element_to_be_clickable((By.XPATH, '(//table[@id="SelectedState0_DDD_L_LBT"]//tr)[' + str(i) + ']'))).click()
    state_name = driver.find_element(By.XPATH, '(//table[@id="SelectedState0_DDD_L_LBT"]//tr/td)[' + str(i) + ']').get_attribute("textContent")
    count_period = len(driver.find_elements(By.XPATH, '//table[@id="ReportingYear0_DDD_L_LBT"]//tr'))
    for j in range(1, count_period + 1):
        wait.until(EC.element_to_be_clickable((By.XPATH, '(//*[@class="dxEditors_edtDropDown_GATS2"])[2]'))).click()  # Clicking on Dropdown Arrow Down Icon
        wait.until(EC.element_to_be_clickable((By.XPATH, '(//table[@id="ReportingYear0_DDD_L_LBT"]//tr)[' + str(j) + ']'))).click()
        driver.find_element(By.XPATH, '//*[text()="Submit"]').click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="CSV0Img"]'))).click()
        compliance_period_name = driver.find_element(By.XPATH, '(//table[@id="ReportingYear0_DDD_L_LBT"]//tr/td)[' + str(j) + ']').get_attribute("textContent")
        print("Successfully Downloaded for State:", state_name, "  and   compliance Period: ", str(compliance_period_name))
    print("\n")

time.sleep(10)
driver.quit()
