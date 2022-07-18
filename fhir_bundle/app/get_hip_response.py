from app import app
import requests
import json
import os,time
from flask import Flask, request

@app.route('/fhir_response', methods=['POST'])
def get_fhir_response():
    data = {"Ack":"ok"}
    return data

