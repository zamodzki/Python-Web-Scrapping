#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pywebio.input import *
from pywebio.output import put_text



# In[2]:


from requests_html import HTMLSession
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import re
from bs4 import BeautifulSoup
import time 
from datetime import date
import requests


# In[3]:


def check_password(p):
    if p != 123456:
        return 'SENHA INCORRETA'
password = input("PASSWORD", type=NUMBER, placeholder= 'Digite aqui sua senha', validate=check_password)


# In[4]:


def bmi():
    txt_N_Produtos = file_upload(label='Insira aqui o arquivo com o nome dos produtos', accept ='text/plain', name=None, placeholder='Choose file',
    multiple=False, max_size='5M', max_total_size=0, required=None, help_text='Arquivo .txt')
    
    txt_P_Menos= file_upload(label='Insira aqui o arquivo .txt com os links do xxx', accept ='text/plain', name=None, placeholder='Choose file',
    multiple=False, max_size='5M', max_total_size=0, required=None, help_text='Ex do arquivo: achocolatado-liquido-nescau-200ml  NaN = quando não existir o produto no site')
    
    txt_P_Acuca= file_upload(label='Insira aqui o arquivo .txt com os links do xxx', accept ='text/plain', name=None, placeholder='Choose file',
    multiple=False, max_size='5M', max_total_size=0, required=None, help_text='Ex do arquivo: https://www.paodeacucar.com/produto/95800/bebida-lactea-nescau-prontinho-200ml  NaN = quando não existir o produto no site',) 
    
    txt_Dalben= file_upload(label='Insira aqui o arquivo .txt com os links do xxx', accept ='text/plain', name=None, placeholder='Choose file',
    multiple=False, max_size='5M', max_total_size=0, required=None, help_text='Ex do arquivo: 1195/bebida-lactea-nestle-200ml-nescau  NaN = quando não existir o produto no site',)

    
    df = pd.DataFrame(columns = ['Produto' , 'Preço_xxx', 'Preço_xxx', 'Preço_xxx'])
    i=1
    
    decoded = txt_N_Produtos['content'].decode("UTF-8")
    asins = decoded.splitlines()
    
    for asin in asins: 
        df.loc[i,["Produto"]] = [asin]
        i = i + 1
        
    
    
    s = HTMLSession()
    asins = []
    i = 1
    
    decoded = txt_P_Menos['content'].decode("UTF-8")
    asins = decoded.splitlines()
    
    for asin in asins:
        if asin == "NaN":
            df.loc[i,["Preço_xxx"]]="NaN"
            i = i + 1
        else:
            r = s.get(f'https://www.xxx.com.br/{asin}/p')
            try:        
                price = r.html.find('.sale_price', first=True).text.split("\n")[0]
                preço = price.split(" ")
                df.loc[i,["Preço_xxx"]]=[preço[1]]
            except:
                df.loc[i,["Preço_xxx"]]="NaN"
        i = i + 1  
        
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}')
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    asins=[]
    i=1
    
    decoded = txt_P_Acuca['content'].decode("UTF-8")
    asins = decoded.splitlines()
    for asin in asins:
        if asin == "NaN":
            df.loc[i,["Preço_Dalben"]]= "NaN"
            i = i + 1
        else:
            driver = webdriver.Chrome(options=options)
            url = (f'https://www.xxxx.com.br/produtos/detalhe/{asin}')
            driver.get(url)
            driver.implicitly_wait(20)
            try:
                preço = driver.find_element(By.XPATH, './/*[@id="product"]/div/app-tag-preco/div/div[2]').text.split(" ")
                df.loc[i,["Preço_xxx"]]= (preço[1])
           
            except:
                df.loc[i,["Preço_xxx"]]= "NaN"
        i = i + 1   
        
        
    i=1
    asins = []
    decoded = txt_Dalben['content'].decode("UTF-8")
    asins = decoded.splitlines()
    for asin in asins:
        if asin == "NaN":
            df.loc[i,["Preço_Pao_de_Açucar"]]="NaN"
            i = i+1
        else:
            url = (f"{asin}")
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            try:
                item = soup.find('div', class_ = 'current-pricesectionstyles__CurrentPrice-sc-17j9p6i-0 drikI').text.split(" ")
                df.loc[i,["Preço_xxx"]]= (item[1])
            except:
                df.loc[i,["Preço_xxx"]]="NaN"
            i= i+1
    df.head()
    show()
  
    
    #'content'：content of the file (in bytes),
    
    
if __name__ == '__main__':
    bmi()    


# In[ ]:




