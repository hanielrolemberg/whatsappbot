from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#importante para rodar o wait(delay)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#Momento de abertura da página whatsap pweb
driver.get("https://web.whatsapp.com/")


#Momento de autenticação autenticação no whatsapp
wait =WebDriverWait(driver, timeout=60) #se o meu elemento posterior "barra_laterla não carregar em até 60s, ele vai dar um erro"
barra_lateral = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]')))
#Uma vez ele carregado, entra o Momento do mapeamento da barra lateral (onde constam os contatos/msg/etc)

barra_lateral = driver.find_element(by=By.XPATH, value='//*[@id="side"]')