from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


#importante para rodar o wait(delay)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#importar tbm o keys - para poder mandar um crtl, backspace, shift etc
from selenium.webdriver.common.keys import Keys

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#Momento de abertura da página whatsap pweb
driver.get("https://web.whatsapp.com/")


#Momento de autenticação autenticação no whatsapp
wait =WebDriverWait(driver, timeout=60) #se o meu elemento posterior "barra_laterla não carregar em até 60s, ele vai dar um erro"
barra_lateral = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]')))
#Uma vez ele carregado, entra o Momento do mapeamento da barra lateral (onde constam os contatos/msg/etc)

barra_lateral = driver.find_element(by=By.XPATH, value='//*[@id="side"]')

#Adicionando uma espera global
driver.implicitly_wait(2)

#Momento de abrir janela de conversa


barra_pesquisa = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]')   #se esse xpath não funcionar, vá neste '//div[@title="Caixa de texto de pesquisa"]'

#permite limpar o campo de inserção de novo usuário
barra_pesquisa.send_keys(Keys.CONTROL + 'a')
barra_pesquisa.send_keys(Keys.DELETE)

#agora é feita a pesquisa em si do contato
nome_contato = "Cliente1" #nesse caso, demos o nome de cliente1, mas nesse campo tu altera para o nome que está salvo no teu contato
barra_pesquisa = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]')   #se esse xpath não funcionar, vá neste '//div[@title="Caixa de texto de pesquisa"]'
barra_pesquisa.send_keys(nome_contato) #key de keyboard, isto é, teclado

#pede para esperar até o servidor whatsapp te forneça o nome 
wait = WebDriverWait(driver, timeout=5)
span_buscando = '//span[@title="Cliente1"]' #span_buscando é onde está o nome do seu contato
conversa_lateral = wait.until(EC.presence_of_element_located((By.XPATH, span_buscando))) #esse campo "Cliente1 foi colocado em maiusculo porque o xpath é casesensitive"

#uma vez achado essa conversa lateral, vamos clicar  nela
conversa_lateral.click() #isso permite abrir a conversa


mensagem = "Olá"
barra_de_mensagem = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]') #se esse xpath não funcionar, vá neste  '//div[@title="Digite uma mensagem"]'
barra_de_mensagem.send_keys(mensagem)

#agora p/ enviar
barra_de_mensagem.send_keys(Keys.RETURN) #RETURN é o enter do teclado