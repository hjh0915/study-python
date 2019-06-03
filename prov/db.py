import psycopg2

class DB(object):
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="shop", 
            user="hjh", 
            password="1234", 
            host="localhost", 
            port="5432"
        )
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()


    def write_province(self, data):
        for x in data:
            self.cursor.execute("""
                insert into province (id, name) values (%s, %s)
            """, (x[0], x[1]))

        self.conn.commit()

    def write_city(self, data):
        for x in data:
            self.cursor.execute("""
                insert into pcity (pid, code, name) values (%s, %s, %s)
            """, (x[0], x[1], x[2]))

        self.conn.commit()

    def get_province(self):
        '''获取所有省份'''

        self.cursor.execute("select id, name from province")
        results = [] 
        for r in self.cursor.fetchall():
            d = dict()
            d['id'] = r[0]
            d['name'] = r[1]
            results.append(d)
    
        return results

    def get_prov_cities(self, pid):
        '''获取指定省份的所属城市'''
        
        self.cursor.execute("select pid, code, name from pcity where pid = %s", (pid,))
        results = [] 
        for r in self.cursor.fetchall():
            d = dict()
            d['pid'] = r[0]
            d['code'] = r[1]
            d['name'] = r[2]
            results.append(d)
    
        return results