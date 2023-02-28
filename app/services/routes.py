from app import app
from flask import Blueprint, request
import re

from app.crawler import Crawler
from app.utils import temple_dict
from config import *

@app.route('/temple', methods = ['GET'])
def get_temple():
    try: 
        res = dict()
        data = []

        for province_th, province_en in zip(LIST_PROVINCE_TH, LIST_PROVINCE_EN):
            data.append({
                'province': province_en,
                'temples': temple_dict(province_th)
            })

        res['status'] = 200
        res['data'] = data

        return res, 200
    
    except Exception as err:
        return { 'error': err }, 400
    
# Post payload
# {
#     province: <string>
# }
@app.route('/province-to-temple', methods = ['POST'])
def post_province_to_temple():
    try:
        res = dict()
        data = dict()

        for province_th, province_en in zip(LIST_PROVINCE_TH, LIST_PROVINCE_EN):
            if request.json['province'].lower() == province_en.lower():
                data = {
                    'province': province_en,
                    'temples': temple_dict(province_th)
                }

        res['status'] = 200
        res['data'] = data
        return res, 200

    except Exception as err:
        return { 'error': err }, 400

# Post payload
# {
#     temple: <string>
# }
@app.route('/temple-to-province', methods = ['POST'])
def post_temple_to_province():
    try:
        res = dict()
        data = dict()

        for province_th, province_en in zip(LIST_PROVINCE_TH, LIST_PROVINCE_EN):
            lst_temple = temple_dict(province_th)
            if request.json['temple'] in lst_temple:
                data = {
                    'province': province_en
                }

        res['status'] = 200
        res['data'] = data
        return res, 200

    except Exception as err:
        return { 'error': err }, 400

# Post payload
# {
#     temple: <string>
# }
@app.route('/search', methods = ['POST'])
def post_search():
    try:
        res = dict()
        data = dict()

        # merge temple
        lst_temple = []
        for province_th, province_en in zip(LIST_PROVINCE_TH, LIST_PROVINCE_EN):
            lst_temple += temple_dict(province_th)

        temple = request.json['temple']

        if not re.search(r'^(วัด)', temple):
            temple = f'วัด{ temple }'

        find_temple = [index for index in lst_temple if temple in index]
        data['temple'] = find_temple

        res['status'] = 200
        res['data'] = data

        return res, 200

    except Exception as err:
        return { 'error': err }, 400


