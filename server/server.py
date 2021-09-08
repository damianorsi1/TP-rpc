from xmlrpc.server import SimpleXMLRPCServer
from conexionMysql import DataBase

class RPC:
    
    _metodos_rpc = ['setNewMedicinetype','deleteMedicine','setNewMedicine','getAllMedicinetype','getAllMedicine', 'iniciar_servidor']
    def __init__(self, direccion):
        self.datos = {}
        self._servidor = SimpleXMLRPCServer(direccion, allow_none=True)

        for metodo in self._metodos_rpc:
                self._servidor.register_function(getattr(self, metodo))


    def setNewMedicinetype(self, type):
        return self._datos[type]


    def deleteMedicine(self, type):
        DataBase.delete_tipe_medicamentos(self, type)


    def setNewMedicine(self, nombre, cantidad, codigo, tipo):
        DataBase.insert_medicamentos(self, nombre, cantidad, codigo, tipo)


    def getAllMedicinetype(self, type):
        list(DataBase.select_all_medicamentos_tipos(self, type))


    def getAllMedicine(self):
        list(DataBase.select_all_medicamentos(self))


    def iniciar_servidor(self):
        self._servidor.serve_forever()


# if __name__ == '__main__':
#     rpc =  (('',5500))
#     print('Se a iniciado el Servidor RPC...')
#     rpc.iniciar_servidor()