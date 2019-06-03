import json
import db

def get_data():
    f = open('_city.json', 'r')
    text = f.read()
    data = json.loads(text)
    return data 

def get_prov():
    s = []
    for p in get_data():
        if p['pid'] == 0:
            id = p['id']
            name = p['city_name']
            s.append((id, name))
    return s

def get_cities():
    prov = [x[0] for x in get_prov()]

    s = []
    for c in get_data():
        if c['pid'] in prov and c['city_code'] != '':
            pid = c['pid']
            code = c['city_code']
            name = c['city_name']
            s.append((pid, code, name))
    s.sort(key=lambda x: x[0])
    return s 

def load_provinces():
    database = db.DB()
    results = get_prov()
    database.write_province(results)

def load_cities():
    database = db.DB()
    results = get_cities()
    database.write_city(results)

if __name__ == '__main__':
    #load_provinces()
    load_cities()