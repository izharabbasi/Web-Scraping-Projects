import requests
from lxml import html
import csv 

def write_to_csv(data):
    headers = ['name', 'address','price','number']
    with open('data.csv', 'w', encoding='utf-8')as f:
        writer = csv.DictWriter(f,headers)
        writer.writeheader()
        writer.writerows(data)

scraped_data = []


for x in range(1,8):
    resp = requests.get(url=f'https://www.newhomesource.com/mls_com/homes/ny/new-york-area/page-{x}', headers={
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.64'
    })
    
    tree = html.fromstring(html=resp.content)

    main_homes = tree.xpath("//div[@id='nhs_homeTabAreaContent']/div[@class='result result--home']")

    for home in main_homes:
        h = {
            'name' : home.xpath(".//div[@class='info info--1']/h3/a/text()")[0],
            'address' : home.xpath(".//div[@class='info info--1']/p/span/text()")[0],
            'price' : home.xpath(".//div[@class='info info--2']/p/strong/text()")[0],
            'number' : home.xpath(".//div[@class='info info--1']/p[4]/text()")[0]
        }
        scraped_data.append(h)
    

print(len(scraped_data)) 

write_to_csv(scraped_data)

