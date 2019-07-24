import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://clutch.co/in/developers/internet-of-things?sort_by=field_pp_page_sponsor&field_pp_min_project_size=All&field_pp_hrly_rate_range=All&field_pp_size_people=All&field_pp_cs_small_biz=&field_pp_cs_midmarket=&field_pp_cs_enterprise=&client_focus=&field_pp_if_advertising=&field_pp_if_automotive=&field_pp_if_arts=&field_pp_if_bizservices=&field_pp_if_conproducts=&field_pp_if_education=&field_pp_if_natural_resources=&field_pp_if_finservices=&field_pp_if_gambling=&field_pp_if_gaming=&field_pp_if_government=&field_pp_if_healthcare=&field_pp_if_hospitality=&field_pp_if_it=&field_pp_if_legal=&field_pp_if_manufacturing=&field_pp_if_media=&field_pp_if_nonprofit=&field_pp_if_realestate=&field_pp_if_retail=&field_pp_if_telecom=&field_pp_if_transportation=&field_pp_if_utilities=&field_pp_if_other=&industry_focus=&field_pp_location_country_select=in&field_pp_location_province=&field_pp_location_latlon_1%5Bpostal_code%5D=&field_pp_location_latlon_1%5Bsearch_distance%5D=100&field_pp_location_latlon_1%5Bsearch_units%5D=mile')
#print(page)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

week = soup.find(id='block-system-main')
items = soup.find_all(class_='col-xs-12 col-md-10 bordered-right provider-base-info')
names = [item.find(class_='field-content').get_text() for item in items]
rank=[item.find(class_='rating').get_text() for item in items]
tag=[item.find(class_='tagline').get_text() for item in items]
rate= [item.find(class_='employees').get_text() for item in items]
ra=[item.find(class_='list-item').get_text() for item in items]
test = []
for li in soup.find_all(class_="website-link website-link-a"):
    t = [li.a.get('href')]
    test.append(t[0])

details = pd.DataFrame(
    {
        'company': names,
        'rating':rank,
        'tagline':tag,
        'employees': rate,
        'minimum project rate': ra,
        'website': test,

    }
)
print(details)
details.to_csv('iot.csv')
