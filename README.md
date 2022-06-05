Visando automatizar e agilizar a tarefa de pesquisa de preços de produtos da concorrência, idealize e desenvolvi um código em Python para realizar tal tarefa, em 3 sites diferentes.
Biblitecas utlizadas.
from requests_html import HTMLSession
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import B
from selenium.webdriver.chrome.options import Options    
