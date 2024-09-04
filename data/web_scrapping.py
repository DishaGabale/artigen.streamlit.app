# Scrapping MySchemes Website
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class MySchemeScraper:
    def __init__(self):
        self.myscheme_url = 'https://rules.myscheme.in/'

    def SchemeLinks(self):
        driver = webdriver.Chrome()
        driver.get(self.myscheme_url)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "__next")))
        
        rows = driver.find_element(By.ID, '__next').find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        
        scheme_links = []
        for row in rows:
            table_rows = row.find_elements(By.TAG_NAME, 'td')
            table_data = {}
            table_data['sr_no'] = table_rows[0].text
            table_data['scheme_name'] = table_rows[1].text.replace('\nCheck Eligibility', '')
            table_data['scheme_link'] = table_rows[2].find_element(By.TAG_NAME, 'a').get_attribute('href')
            scheme_links.append(table_data)
        
        driver.close()
        return scheme_links

    def SchemeDetails(self, scheme_links, start_index=0, batch_size=5):
        for index, scheme in enumerate(scheme_links[start_index:], start=start_index):
            print(f"Scraping details for: {scheme['scheme_name']}")
            driver = webdriver.Chrome()
            driver.get(scheme['scheme_link'])
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "__next")))
            
            try:
                scheme['details'] = driver.find_element(By.ID, 'details').text
            except NoSuchElementException:
                scheme['details'] = 'N/A'
                print("Details not found for:", scheme['scheme_name'])
                continue
            
            try:
                scheme['benefits'] = driver.find_element(By.ID, 'benefits').text
            except NoSuchElementException:
                scheme['benefits'] = 'N/A'
                print("Benefits not found for:", scheme['scheme_name'])
                continue
            
            try:
                scheme['eligibility'] = driver.find_element(By.ID, 'eligibility').text
            except NoSuchElementException:
                scheme['eligibility'] = 'N/A'
                print("Eligibility not found for:", scheme['scheme_name'])
                continue
            
            try:
                scheme['application_process'] = driver.find_element(By.ID, 'application-process').text
            except NoSuchElementException:
                scheme['application_process'] = 'N/A'
                print("Application process not found for:", scheme['scheme_name'])
                continue
            
            try:
                scheme['documents_required'] = driver.find_element(By.ID, 'documents-required').text
            except NoSuchElementException:
                scheme['documents_required'] = 'N/A'
                print("Documents required not found for:", scheme['scheme_name'])
                continue
            
            driver.close()
            
            if index % batch_size == 0:
                self.save_data(scheme_links, index)
                
        self.save_data(scheme_links, len(scheme_links) - 1)
            
    def save_data(self, data, index):
        with open('scraped_data.json', 'w') as file:
            json.dump(data,file)
        with open('checkpoint.txt', 'w') as checkpoint_file:
            checkpoint_file.write(str(index))

    def download(self):
        scheme_links = self.SchemeLinks()
        
        # Check for the last successfully scraped index
        start_index = 0
        if os.path.exists('checkpoint.txt'):
            with open('checkpoint.txt', 'r') as checkpoint_file:
                start_index = int(checkpoint_file.read())
        
        self.SchemeDetails(scheme_links, start_index)
        return scheme_links


if __name__ == '__main__':
    download_path = os.path.join(os.path.dirname(__file__), 'myschemes_scraped.json')
    scraper = MySchemeScraper()
    scraped_scheme_details = scraper.download()
    json.dump(scraped_scheme_details, open(download_path, 'w'))