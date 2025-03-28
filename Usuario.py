class Usuario():
    def __init__(self, nombre:str, identificador:int, tipo_usuario:int, libros_prestados:int = 0):
        self.__nombre = nombre
        self.__identificador = identificador
        self.__tipo_usuario = tipo_usuario
        self.libros_prestados = libros_prestados

    def get_nombre(self):
        return self.__nombre

    def get_identificador(self):
        return self.__identificador

    def get_tipo_usuario(self):
        return self.__tipo_usuario

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_identificador(self, identificador):
        self.__identificador = identificador

    def set_tipo_usuario(self, tipo_usuario):
        self.__tipo_usuario = tipo_usuario
        
    def get_libros_prestados(self):
        return self.libros_prestados

    def set_libros_prestados(self, cantidad):
        self.libros_prestados = cantidad

        
        