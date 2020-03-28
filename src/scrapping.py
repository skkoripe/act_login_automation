import requests
from bs4 import BeautifulSoup

url="https://selfcare.actcorp.in/web/hyd/home"
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')

def get_ip():
    results=soup.find(id='footer')
    ip=results.find(class_='ip')
    return ip.text.split(':')[1]

def get_pauth():
    results=soup.find(id='portlet-link')
    form=results.find('form')
    site=form['action']
    p_auth_start=site.find('p_auth')
    p_auth_end=site.find('&')
    auth_id=site[p_auth_start:p_auth_end]
    return auth_id

def get_site():
    return 'https://selfcare.actcorp.in/web/hyd/home/-/act/login?' + get_pauth()
