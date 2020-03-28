import requests
import scrapping as scrap
from Credentials import *

headers={
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'https://selfcare.actcorp.in',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Sec-Fetch-Dest': 'document',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Referer': 'https://selfcare.actcorp.in/web/hyd/home',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}
with requests.Session() as s:
    login_data = {
        'userIP': scrap.get_ip(),
        '_login_WAR_BeamPromotionalNDownloadsportlet_uname': user_name,
        'pword': password
    }
    url=scrap.get_site()
    post_res=s.post(url,data=login_data,headers=headers)
    print(post_res.status_code)


    
