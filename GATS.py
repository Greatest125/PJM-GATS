from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller
import glob
import pandas as pd
import os

chromedriver_autoinstaller.install()
chromeOptions = webdriver.ChromeOptions()
driver = webdriver.Chrome()
#change the directory to the whatever you want
prefs = {"download.default_directory" : '/home/leeld/Downloads/gats'}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=chromeOptions)

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

#Merge all of the spreadsheets (one for each facility) into one master spreadsheet 
os.chdir("/home/leeld/Downloads/gats")
extensions = ("*csv")
filenames = []  # made 'filename' plural to indicate it's a list

# building list of filenames moved to separate loop
for files in extensions: 
    filenames.extend(glob.glob(files)) 
# getting csv files to be merged
print('File names:', filenames)

# empty data frame for the new output csv file with the merged csv files
outputxlsx = pd.DataFrame()

# for loop to iterate all csv files
for file in filenames:
   # using concat for csv files
   # after reading them with read_csv()
   df = pd.concat(pd.read_csv( file, sheet_name=None), ignore_index=True, sort=False)
   outputxlsx = outputxlsx.append( df, ignore_index=True)
print('All spreadsheets merged into one file ("RPS Retired Certificates (GATS).xlsx"')
outputxlsx.to_csv("/home/leeld/Downloads/gats/RPS Retired Certificates (GATS).xlsx", index=False)
#Delete data files for each county
for filename in glob.glob("/home/leeld/Downloads/gats*"):
    os.remove(filename) 
print('Deleting data spreadsheets')
