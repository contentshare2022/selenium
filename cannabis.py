from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_strain_data(strains):
    strain_list=[]
    
    for strain in strains:
        driver = webdriver.Chrome(executable_path=r'D:\Ferramentas\chromedriver_win32\chromedriver.exe')

        driver.get(strain)
        canabinoides=driver.find_element(By.XPATH, r'//*[@id="tab-title-awp-cannabinoids"]/a')
        time.sleep(1)
        canabinoides.click()

        strain=driver.find_element(By.CLASS_NAME, "product-title")
        label=driver.find_elements(By.CLASS_NAME, "pie_progress__label")
        number=driver.find_elements(By.CLASS_NAME, "pie_progress__number")

        registro={
            'Strain':f'{strain.text}'
        }       

        for l,n in zip(label,number):
            registro[f'{l.text}']=n.text
        
        strain_list.append(registro)

        registro={}

        driver.close()
    
    return strain_list


def get_strain_links():
    links_list=[]
    driver = webdriver.Chrome(executable_path=r'D:\Ferramentas\chromedriver_win32\chromedriver.exe')
    
    driver.get("https://www.seedbank.com/collections/feminized-seeds/")
    
    page_numbers=driver.find_elements(By.CLASS_NAME, 'page-number')
    tamanho=len(page_numbers)
    
    for p in range(tamanho+1):
        
        driver.get(f"https://www.seedbank.com/collections/feminized-seeds/page/{p+1}/")
    
        links=driver.find_elements(By.CLASS_NAME, 'woocommerce-LoopProduct-link')
        
        for l in links:
            links_list.append(l.get_attribute('href'))

    return links_list

strains=get_strain_links()

print(get_strain_data(['https://www.seedbank.com/products/chocolope-seeds/']))


