from src.cn.data_base_connection import Database
from src.models.dbModel import dbModel
from src.entities.customerEntity import customerEntity

class customerModel(dbModel):

    def __init__(self):
        dbModel.__init__(self)
        
    def get_customers(self):
        _db = None
        _data = []
        try:
            _db = Database()
            _db.connect(self.host,self.port,self.user,self.password,self.database)
            print('Se conecto a la bd')
            _con_client = _db.get_client()

            _sql = """SELECT c.full_name, 
                    c.cod
                FROM    main.customer c; """   

            _cur = _con_client.cursor()
            _cur.execute(_sql,)
            _rows = _cur.fetchall()
        
            for row in _rows:
                _entity  = customerEntity()
                _entity.full_name = row[0]
                _entity.cod = row[1]
                _data.append(_entity)

            _cur.close()
        except(Exception) as e:
            print(str(e))
            #self.add_log(str(e),type(self).__name__)
        finally:
            if _db is not None:
                _db.disconnect()
                print("Se cerro la conexion")
        return _data
    

    def add_customer(self,entity):
        _db = None
        _data = []
        try:
            print(12)
            _db = Database()
            _db.connect(self.host,self.port,self.user,self.password,self.database)
            print('Se conecto a la bd')
            _con_client = _db.get_client()

            _sql = """INSERT INTO main.customer (full_name , cod)
                    VALUES (%s,%s); """  

            _cur = _con_client.cursor()
            _cur.execute(_sql,(entity.full_name,entity.cod))
            _con_client.commit()
            _cur.close()
        except(Exception) as e:
            print(str(e))
            #self.add_log(str(e),type(self).__name__)
        finally:
            if _db is not None:
                _db.disconnect()
                print("Se cerro la conexion")
        return entity
    
    def update_customer(self,entity):
        _db = None
        _data = []
        try:
            print(12)
            _db = Database()
            _db.connect(self.host,self.port,self.user,self.password,self.database)
            print('Se conecto a la bd')
            _con_client = _db.get_client()

            _sql = """UPDATE main.customer
                    SET full_name = %s 
                    WHERE cod = %s; """  

            _cur = _con_client.cursor()
            _cur.execute(_sql,(entity.full_name,entity.cod))
            _con_client.commit()
            _cur.close()
        except(Exception) as e:
            print(str(e))
            #self.add_log(str(e),type(self).__name__)
        finally:
            if _db is not None:
                _db.disconnect()
                print("Se cerro la conexion")
        return entity