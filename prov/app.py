from flask import Flask
from flask import render_template
import db

app = Flask(__name__)

@app.route('/')
def index():
    d = db.DB()
    c = []
    provinces = d.get_province()
    for p in provinces:
        if p['name'] not in ['重庆', '澳门']:
            cities = d.get_prov_cities(p['id'])
            x = dict()
            x['prov'] = p['name']
            x['cities'] = cities
            c.append(x)

    return render_template('head.html', results=c)

@app.route('/test/<code>')
def test(code):
    return render_template('head.html')