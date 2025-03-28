import Usuario as usuario
import Libro as libro
from datetime import datetime, timedelta

class Prestamo():
    def __init__(self, usuario: usuario, libro:libro, fecha_prestamo:timedelta, dias_prestamo:int, fecha_devolucion:datetime):
        self.__usuario = usuario
        self.__libro = libro
        self.__fecha_prestamo = fecha_prestamo
        self.__dias_prestamo = dias_prestamo
        self.__fecha_devolucion = fecha_devolucion

    def get_usuario(self):
        return self.__usuario

    def get_libro(self):
        return self.__libro

    def get_fecha_prestamo(self):
        return self.__fecha_prestamo

    def get_dias_prestamo(self):
        return self.__dias_prestamo

    def get_fecha_devolucion(self):
        return self.__fecha_devolucion

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def set_libro(self, libro):
        self.__libro = libro

    def set_fecha_prestamo(self, fecha_prestamo):
        self.__fecha_prestamo = fecha_prestamo

    def set_dias_prestamo(self, dias_prestamo):
        self.__dias_prestamo = dias_prestamo

    def set_fecha_devolucion(self, fecha_devolucion):
        self.__fecha_devolucion = fecha_devolucion
        
    