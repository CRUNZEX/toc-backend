import requests
import re
import csv

from config import *

class Crawler:
    def __init__(self, url) -> None:
        self.url = url
        self.province = {}
    
    def get(self):
        self.response = requests.get(self.url)
        return self

    def province_get(self):
        extracted = re.findall(r'(?<=<li><a href=").*?(?=</a></li>)', self.response.text)

        for index in extracted:
            # assign regex
            extracted_province = re.sub(r'(" title="รายชื่อวัดในจังหวัด|(">รายชื่อวัดในจังหวัด).*$)', '|', index)
            province = re.split(r'(\|)', extracted_province)

            # check header and footer
            if len(province) > 3:
                self.province[province[2]] = province[0]

        return self.province

    def province_url(self, list_province: list):
        obj_province = {}
        for name_province in list_province:
            obj_province[name_province] = self.province[name_province]

        return obj_province

    def temple_get(self, obj: dict):
        for key in obj.keys():
            req = requests.get(f'{ HOST_URL }{ obj[key] }')

            # crawl <li> to list of temples
            lst_temple = re.findall(r'(?=\<li\>).*?(?=</li>)', req.text.split('title="วัดไทย"')[0])

            # Remove index not 'วัด' inside
            lst_temple = [index for index in lst_temple if 'วัด' in index]
            
            # Regex: only temple name
            lst_tample_final = []
            for index in lst_temple:
                temple = re.findall(r'(?=\>วัด).*?(?=\<\/a\> |\<a |\<\/a\>|\<a|&#160;|ตำ)', index)
                lst_tample_final.append(temple[0][1:])
            
            # write to file
            with open(f'{ key }.csv', 'w+', encoding = 'utf-8') as file:
                for temple in lst_tample_final:
                    file.write(f'{ temple }\n')