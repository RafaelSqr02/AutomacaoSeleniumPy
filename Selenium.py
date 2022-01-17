import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class bot():
    def __init__(self):
        self.nome = input ('Digite o nome:')
        self.cargo = input ('Digite o cargo:')
        self.pretensao = input ('Digite o pretensao:')
        self.email = input ('Digite o email:')
        self.telefone = input ('Digite o tel:')
        self.endereco = input ('Digite o end:')
        self.estado = input ('Digite o uf:')
        self.cidade = input ('Digite o cidade:')
        self.bairro = input ('Digite o bairro:')
        self.rua = input ('Digite o rua:')
        self.cep = input ('Digite o cep:')
        self.resumo = input ('Digite o resumo:')
        
        self.drive = webdriver.Chrome(executable_path=r'C:\Users\pc gamer\Desktop\Chrome\chromedriver.exe')
    
    def preencherForms(self):
        drive = self.drive
        drive.get('https://jobs.quickin.io/primecontrol/apply?src=website')

        time.sleep(3)

        nome = drive.find_element_by_xpath('//*[@id="name"]')
        cargo = drive.find_element_by_xpath('//*[@id="headline"]')
        pretensao = drive.find_element_by_xpath('//*[@id="salary"]')
        email = drive.find_element_by_xpath('//*[@id="email"]')
        telefone = drive.find_element_by_xpath('//*[@id="phone-0"]')
        endereco = drive.find_element_by_xpath('//*[@id="country"]')
        estado = drive.find_element_by_xpath('//*[@id="region"]')
        cidade = drive.find_element_by_xpath('//*[@id="city"]')
        bairro = drive.find_element_by_xpath('//*[@id="neighborhood"]')
        rua = drive.find_element_by_xpath('//*[@id="address"]')
        cep = drive.find_element_by_xpath('//*[@id="zipcode"]')
        resumo = drive.find_element_by_xpath('//*[@id="summary"]')

        botao = drive.find_element_by_xpath('//*[@id="__layout"]/div/div/section/div/div/form/button/span')

        nome.send_keys(self.nome)
        cargo.send_keys(self.cargo)
        pretensao.send_keys(self.pretensao)
        email.send_keys(self.email)
        telefone.send_keys(self.telefone)
        endereco.send_keys(self.endereco)
        estado.send_keys(self.estado)
        cidade.send_keys(self.cidade)
        bairro.send_keys(self.bairro)
        rua.send_keys(self.rua)
        cep.send_keys(self.cep)
        resumo.send_keys(self.resumo)

        botao.click()
    



bot = bot ()
bot.preencherForms()