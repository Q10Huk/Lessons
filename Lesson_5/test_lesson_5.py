import time
from selenium import webdriver # импортируем драйвер webdriver это и есть набор команд для управления браузером
from selenium.webdriver.chrome.options import Options as chrome_options # импотрируем опции браузера - надо узнать как запустить браузер на весь экран
from selenium.webdriver.common.by import By # импорт команд By для CSS_SELECTOR, XPATH
from selenium.webdriver.common.action_chains import ActionChains # Прокрутка к целевому элементу с помощью Actions

driver = webdriver.Chrome()
from selenium.webdriver.common.by import By # импорт команд By для CSS_SELECTOR
time.sleep(1) # команда time.sleep устанавливает паузу в n секунд, чтобы мы успели увидеть, что происходит в браузере
driver.get('https://sbis.ru/') # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
time.sleep(2)

button_support = driver.find_element(By.XPATH, "//a[text()='Поддержка']") # '[href="/support"]'
button_support.click()
time.sleep(2)

# Используем прокрутку до элемента и кликаем на него
target = driver.find_element(By.CSS_SELECTOR, '[href="/download"]')
actions = ActionChains(driver)
actions.move_to_element(target)
actions.perform()
time.sleep(1)
button_download = driver.find_element(By.CSS_SELECTOR, '[href="/download"]') .click()
time.sleep(2)

# получаем ссылки на этой странице
download_links = driver.find_elements(By.XPATH, "//div[@data-for='ereport25']//a[@class='sbis_ru-DownloadNew-loadLink__link js-link']")
# download_links = driver.find_elements(By.TAG_NAME, "//div[@data-for='ereport25']").__getattribute__('href')
# download_links = download_links.__getattribute__('href')
# print(download_links)
download_links_list = []
for a in download_links:
    download_links_list.append(a.get_attribute('href'))
#print(download_links_list)
#for a in download_links_list:
    #print(a+'\n')
result_download_links_list = ['https://update.sbis.ru/version25/sbis-setup-eo-inst.exe', 'https://update.sbis.ru/version25/sbis-update-eo.exe', 'https://update.sbis.ru/version25/jinneeupdate.exe', 'https://update.sbis.ru/download/pdf417/print_pdf417.msi', 'https://update.sbis.ru/download/shabl/shabl.zip']
assert download_links_list == result_download_links_list

# Теперь надо положить это все в файл
file = open('download_links.txt', 'w')
for index in download_links_list:
    file.write(index + '\n')
file.close()

time.sleep(2)
driver.quit()
