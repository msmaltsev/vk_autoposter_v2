# -*- coding: utf-8 -*-
try:
    from os import getuid
except ImportError:
    def getuid():
        return 4000

from flask import Flask, render_template, request, redirect
import json, datetime, time
import os
from dispatch import *

app = Flask(__name__, template_folder='templates')

@app.route("/", methods=['GET', 'POST'])
def index():

    disp_list = os.listdir(os.getcwd() + '/dispatches/')
    for i in disp_list:
        d = Dispatch(i)
        print(d.dispatchAsDict())

    return render_template('index.html')

@app.route("/new", methods=['GET', 'POST'])
def new():
    return render_template('new.html')

@app.route("/save_dispatch", methods = ['GET', 'POST'])
def save_dispatch():

    if request.method == 'POST':
        print(request.form['dispatch_name'])
        dispatch_name = request.form['dispatch_name']
        text = request.form['text']
        links = request.form['links']
        print(links)
        d = Dispatch(dispatch_name)
        d.addText(text)
        d.addLinks(links)

    return render_template('save_dispatch.html')


if __name__ == "__main__":
    app.run(port=getuid() + 1000)
    
