from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#para não precisar ficar mandando todo o caminho do arquivo, usa o pathlib
from pathlib import Path

#importante para rodar o wait(delay)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#importar tbm o keys - para poder mandar um crtl, backspace, shift etc
from selenium.webdriver.common.keys import Keys


#se quiser ver como cada passo é executado, use o sleep>
from time import sleep

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#Momento de abertura da página whatsap pweb
def abrir_janela_whatsapp():
    driver.get("https://web.whatsapp.com/")
    #Momento de autenticação autenticação no whatsapp
    wait =WebDriverWait(driver, timeout=60) #se o meu elemento posterior "barra_laterla não carregar em até 60s, ele vai dar um erro"
    barra_lateral = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]')))
    #Uma vez ele carregado, entra o Momento do mapeamento da barra lateral (onde constam os contatos/msg/etc)
    barra_lateral = driver.find_element(by=By.XPATH, value='//*[@id="side"]')
    #Adicionando uma espera global
    driver.implicitly_wait(2)


#Momento de abrir janela de conversa
def abrir_janela_de_conversa(nome_contato): #nesse caso, demos o nome de cliente1, mas nesse campo tu altera para o nome que está salvo no teu contato
    barra_pesquisa = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]')   #se esse xpath não funcionar, vá neste '//div[@title="Caixa de texto de pesquisa"]' #permite limpar o campo de inserção de novo usuário
    barra_pesquisa.send_keys(Keys.CONTROL + 'a')
    barra_pesquisa.send_keys(Keys.DELETE)
    
    barra_pesquisa = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]')    #agora é feita a pesquisa em si do contato #se esse xpath não funcionar, vá neste '//div[@title="Caixa de texto de pesquisa"]'
    barra_pesquisa.send_keys(nome_contato) #key de keyboard, isto é, teclado
    
    wait = WebDriverWait(driver, timeout=5)     #pede para esperar até o servidor whatsapp te forneça o nome 
    span_buscando = f'//span[@title="{nome_contato}"]' #span_buscando é onde está o nome do seu contato
    conversa_lateral = wait.until(EC.presence_of_element_located((By.XPATH, span_buscando))) #esse campo "Cliente1 foi colocado em maiusculo porque o xpath é casesensitive"
    conversa_lateral.click() #isso permite abrir a conversa   #uma vez achado essa conversa lateral, vamos clicar  nela

def sai_das_conversas():
    barra_pesquisa = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]')
    barra_pesquisa.send_keys(Keys.CONTROL + 'a')
    barra_pesquisa.send_keys(Keys.DELETE)
    barra_pesquisa.send_keys(Keys.ESCAPE) #escape = ESC


def envia_mensagem(mensagem): 
    barra_de_mensagem = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]') #se esse xpath não funcionar, vá neste  '//div[@title="Digite uma mensagem"]'
    barra_de_mensagem.send_keys(mensagem)
    barra_de_mensagem.send_keys(Keys.RETURN) #agora p/ enviar #RETURN é o enter do teclado


def envia_documentos(caminho_documento): # '' ->  #mapeie o endereço local do seu doc  #endeço do documento ex 'C:/user/meusuario/Documentos/meudocumento.pdf'

    botao_anexos = driver.find_element(By.XPATH, '//div[@title="Attach" or @title="Anexar"]') #procura o botão attach "+" 
    botao_anexos.click()

    botao_documentos = driver.find_element(By.XPATH, '//input[@accept="*" and @type="file"]') #enviar o documento
    botao_documentos.send_keys(caminho_documento)

    botao_enviar = driver.find_element(By.XPATH, '//div[@aria-label="Enviar"]')
    botao_enviar.click() #clicar no botao de enviar

def envia_imagem(caminho_imagem ): #'' endeço do documento ex 'C:/user/meusuario/Documentos/passaro.jpeg'
    botao_anexos = driver.find_element(By.XPATH, '//div[@title="Attach" or @title="Anexar"]') #procura o botão attach "+" #se não funcionar "attach", pode testar "anexar"
    botao_anexos.click()

    botao_fotos = driver.find_element(By.XPATH, '//span[text()="Fotos e vídeos"]/../input')
    botao_fotos.send_keys(caminho_imagem) #enviar a imagem

    botao_enviar = driver.find_element(By.XPATH, '//div[@aria-label="Enviar"]')
    botao_enviar.click() #clicar no botao de enviar

if __name__=='__main__':

    contatos = ['Cliente1', 'Cliente2', 'Cliente3']
    caminho_catalogo = str(Path(__file__).parent.parent / 'catalogo.pdf')    #__file__ é o arquivo que eu estou agora, já o parent -> é o caminho para a pasta dele, aqui dentro do visual studio code
    mensagem = """"
    Olá, {}!
    foi um prazer conhecê-lo.
    Envio um catalogo dos produtos, para que você posso explorá-lo.
    Um abraço!
    """

    abrir_janela_whatsapp()

    for contato in contatos:
        abrir_janela_de_conversa(contato)
        sleep(1)
        envia_mensagem(mensagem.format(contato))
        sleep(1)
        envia_documentos(caminho_catalogo)
        sleep(1)
        sai_das_conversas()
        sleep(1)
    
    sleep(200)


    #para rodar -> no cmd, digite python3 e o caminho até o arquivo  