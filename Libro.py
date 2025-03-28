class Libro():
    def __init__(self, titulo:str, autor:str, año_publicacion:int, area:str, codigo:int, unidades:int, disponibles:int):
        self.__titulo = titulo
        self.__autor = autor
        self.__año_publicacion = año_publicacion
        self.__area = area
        self.__codigo = codigo
        self.__unidades = unidades
        self.__disponibles = disponibles

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_titulo(self):
        return self.__titulo

    def set_autor(self, autor):
        self.__autor = autor

    def get_autor(self):
        return self.__autor

    def set_año_publicacion(self, año_publicacion):
        self.__año_publicacion = año_publicacion

    def get_año_publicacion(self):
        return self.__año_publicacion

    def set_area(self, area):
        self.__area = area

    def get_area(self):
        return self.__area

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_codigo(self):
        return self.__codigo

    def set_unidades(self, unidades):
        self.__unidades = unidades

    def get_unidades(self):
        return self.__unidades

    def set_disponibles(self, disponibles):
        self.__disponibles = disponibles

    def get_disponibles(self):
        return self.__disponibles