from selenium import webdriver # импортируем драйвер webdriver это и есть набор команд для управления браузером
from selenium.webdriver.common.by import By # импорт команд By для CSS_SELECTOR, XPATH
from selenium.webdriver.common.action_chains import ActionChains # Прокрутка к целевому элементу с помощью Actions

url = 'https://sbis.ru/'

try:
    driver = webdriver.Chrome()
    driver.get(url) # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
    driver.fullscreen_window() # Позволяет открывать окно на весь экран
    button_support = driver.find_element(By.XPATH, "//a[text()='Поддержка']")  # '[href="/support"]'
    button_support.click()

    # Используем прокрутку до элемента и кликаем на него
    target = driver.find_element(By.CSS_SELECTOR, '[href="/download"]')
    actions = ActionChains(driver)
    actions.move_to_element(target)
    actions.perform()
    button_download = driver.find_element(By.CSS_SELECTOR, '[href="/download"]').click()

    # получаем ссылки на этой странице
    download_links = driver.find_elements(By.XPATH, "//div[@data-for='ereport25']//a[@class='sbis_ru-DownloadNew-loadLink__link js-link']")

    # попробовать получить ссылки с помощью By.LINK_TEXT
    # download_links_2 = driver.find_elements(By.LINK_TEXT, "https://update.sbis.ru/")
    download_links_list = []
    for a in download_links:
        download_links_list.append(a.get_attribute('href'))

    # Теперь надо положить это все в файл
    file = open('download_links.txt', 'w')
    for index in download_links_list:
        file.write(index + '\n')
    file.close()



finally:
    driver.quit()
