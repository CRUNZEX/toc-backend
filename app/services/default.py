from app import app
from flask import Blueprint, request

@app.route('/', methods = ['GET'])
def get_default():
    return { 'status': 200 }, 200