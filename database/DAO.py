from database.DB_connect import DBConnect
from model.Aeroporto import Aeroporto
from model.voli import Voli


class DAO():
    @staticmethod
    def getDistMin(distMin):
        conn=DBConnect.get_connection()
        cursor=conn.cursor(dictionary= True)

        res = []
        query="""select *
                from flights f 
                where f.DISTANCE > %s"""

        cursor.execute(query,(distMin,))

        for row in cursor:
            res.append(Voli(**row))

        cursor.close()
        conn.close()

        return res

    @staticmethod
    def getAeroporti():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []
        query = """SELECT * FROM airports"""

        cursor.execute(query)

        for row in cursor:
            res.append(Aeroporto(**row))

        cursor.close()
        conn.close()

        return res








