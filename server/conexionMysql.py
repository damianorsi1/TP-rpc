import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.Connect(
            host='localhost',
            user='root',
            password='root',
            db='farmacia'
        )
        self.cursor = self.connection.cursor()
        print("conexion exitosa con la bd...")


##------------------getAllMedicine------------------
    def select_all_medicamentos(self):
        sql = 'SELECT idmedicamento, nombre, cantidad, codigo, tipo FROM medicamento'
        try:
            self.cursor.execute(sql)
            medicamentos = self.cursor.fetchall()
            for medicamento in medicamentos:
                print("ID:", medicamento[0])
                print("Nombre:", medicamento[1])
                print("Cantidad:", medicamento[2])
                print("Codigo:", medicamento[3])
                print("Tipo:", medicamento[4])
                print("------------------\n")
        
        except Exception as e:
            raise


##------------------getAllMedicinetype------------------
    def select_all_medicamentos_tipos(self, tipo):
        sql = 'SELECT idmedicamento, nombre, cantidad, codigo, tipo FROM medicamento WHERE tipo = %s'
        values = (tipo)
        try:
            self.cursor.execute(sql, values)
            medicamentos = self.cursor.fetchall()
            for medicamento in medicamentos:
                print("ID:", medicamento[0])
                print("Nombre:", medicamento[1])
                print("Cantidad:", medicamento[2])
                print("Codigo:", medicamento[3])
                print("Tipo:", medicamento[4])
                print("------------------\n")
        
        except Exception as e:
            raise


##------------------DeleteMedicine------------------
    def delete_tipe_medicamentos(self, tipo):
        sql = 'DELETE FROM medicamento WHERE tipo = %s'
        values = (tipo)
        try:
            self.cursor.execute(sql, values)
            self.connection.commit()
            print("Los tipos de medicamento se dieron de baja exitosamente!.")

        except Exception as e:
            raise


##------------------InsertMedicine------------------
    def insert_medicamentos(self, nombre, cantidad, codigo, tipo):
        sql = 'INSERT INTO medicamento (nombre, cantidad, codigo, tipo) values (%s, %s, %s, %s)'
        values = (nombre, cantidad, codigo, tipo)
        try:
            self.cursor.execute(sql, values)
            self.connection.commit()
            print("El medicamento se agrego exitosamente!.")
            print(values)
        
        except Exception as e:
            raise


database = DataBase();

# database.select_all_medicamentos();                                                       #  select_all_medicamentos(self):
# database.select_all_medicamentos_tipos('diclo');                                        #  select_all_medicamentos_tipos(self, type):
# database.delete_tipe_medicamentos("diclo");                                                #  delete_type_medicamentos(self, type):
# database.insert_medicamentos('PARACETAMOL','30','1232123','PARACETA');                   #  insert_medicamentos(self, nombre, cantidad, codigo, tipo):