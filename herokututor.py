from flask import Flask, Response, jsonify, abort, make_response,  render_template, redirect, request
from faster_than_requests import requests
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json, requests, traceback, os, lxml, re, urllib, urllib3, urllib.parse, argparse, pytz, urllib.request, time

app = Flask(__name__)

@app.route('/')
def home():
    """Landing page."""
    return render_template('FILE-HTML-LO.html')

@app.route("/api/<path:nazri>", methods=['GET', 'POST'])
def api(nazri):
    if nazri == "nazri":
        ret = "Nazri Ganteng"
        return make_response(jsonify(ret))
    elif nazri == "tambah-aja-scraplo-sini":
        ret["result"] = "Nazri Ganteng Cuy"
        return make_response(jsonify(ret))
      
if __name__ == "__main__":
    app.run()