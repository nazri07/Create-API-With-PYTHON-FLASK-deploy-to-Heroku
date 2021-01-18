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
    elif nazri == "arti":
        twit = request.args.get("nama", "")
        link = "http://primbon.com/arti_nama.php?nama1={}&proses=+Submit%21+".format(urllib.parse.quote(twit))
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html.parser')
        a = soup.find('div', attrs={'id':'body','class':'width'}).text
        ret = {}
        ret["result"] = a.replace("\n","").replace("Nama:ARTI NAMA (JAWA)Berikut ini adalah kumpulan arti nama lengkap dari A-Z dalam budaya (bahasa) Jawa untuk Laki-laki (L) dan Perempuan (P).Arti Nama (L) Arti Nama (P)ARTI NAMA (ARAB / ISLAM)Berikut ini adalah kumpulan arti nama lengkap dari A-Z dalam budaya (bahasa) Arab atau bernuansa Islami untuk Laki-laki (L) dan Perempuan (P).Arti Nama (L) Arti Nama (P)Catatan: Gunakan juga aplikasi numerologi Kecocokan Nama, untuk melihat sejauh mana keselarasan nama anda dengan diri anda.","")
        return  make_response(jsonify(ret))
      
if __name__ == "__main__":
    app.run()
