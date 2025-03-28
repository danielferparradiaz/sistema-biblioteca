import os
from datetime import datetime, timedelta
import Prestamo as prestamo


class Funciones:
    def __init__(self, usuarios, libros, prestamos):
        self.usuarios = usuarios
        self.libros = libros
        self.prestamos = prestamos

    def mostrar_menu(self):
        print("\n")
        print("~" * 25)
        print("Sistema de la biblioteca")
        print("~" * 25)
        print("\n")

        while True:
            print("[1]. Listar todos los libros disponibles")
            print("[2]. Consultar por título, autor o área")
            print("[3]. Realizar un préstamo")
            print("[4]. Devolver un libro")
            print("[5]. Consultar un libro prestado por usuario")
            print("[6]. Limpiar consola")
            print("[7]. Salir")

            try:
                opcion = int(input("Opción: "))
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue

            if opcion == 1:
                self.listar_libros()
            elif opcion == 2:
                self.consultar_libro()
            elif opcion == 3:
                self.realizar_prestamo()
            elif opcion == 4:
                self.devolver_libro()
            elif opcion == 5:
                self.consultar_prestamos_usuario()
            elif opcion == 6:
                self.limpiar_consola()
            elif opcion == 7:
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def listar_libros(self):
        print(" - " * 25)
        print("Libros encontrados:")
        for l in self.libros:
            print(f"Título: {l.get_titulo()}, Autor: {l.get_autor()}, Disponibles: {l.get_disponibles()}")
        print(" - " * 25)

    def consultar_libro(self):
        busqueda = input("Ingrese título, autor o área: ").lower().strip()
        resultados = [
            l for l in self.libros if 
            busqueda in l.get_titulo().lower() or 
            busqueda in l.get_autor().lower() or 
            busqueda in l.get_area().lower()
        ]
        if resultados:
            print(" - " * 25)
            print("Libros encontrados:")
            for l in resultados:
                print(f"Título: {l.get_titulo()}, Autor: {l.get_autor()}, Área: {l.get_area()}")
            print(" - " * 25)
        else:
            print(" - " * 25)
            print("No se encontraron libros que coincidan con la búsqueda.")
            print(" - " * 25)

    def realizar_prestamo(self):
        nombre = input("Ingrese su nombre: ").strip()
        usuario = next((u for u in self.usuarios if u.get_nombre().lower() == nombre.lower()), None)

        if not usuario:
            print("Usuario no encontrado.")
            return

        if usuario.libros_prestados >= 3:
            print("No puede realizar el préstamo. Ya tiene 3 libros prestados.")
            return

        busqueda = input("Ingrese título, autor o área del libro que desea prestar: ").lower().strip()
        resultados = [l for l in self.libros if 
                      busqueda in l.get_titulo().lower() or 
                      busqueda in l.get_autor().lower() or 
                      busqueda in l.get_area().lower()]

        if not resultados:
            print(" - " * 25)
            print("No se encontraron libros.")
            print(" - " * 25)
            return

        for i, l in enumerate(resultados, start=1):
            print(" - " * 25)
            print(f"[{i}] {l.get_titulo()} - {l.get_autor()} (Código: {l.get_codigo()}, Disponibles: {l.get_disponibles()})")
            print(" - " * 25)

        try:
            seleccion = int(input("Seleccione el número del libro: ")) - 1
            if seleccion < 0 or seleccion >= len(resultados):
                print(" - " * 25)
                print("Selección inválida.")
                print(" - " * 25)
                return
            libro_prestar = resultados[seleccion]
        except ValueError:
            print(" - " * 25)
            print("Debe ingresar un número válido.")
            print(" - " * 25)
            return

        if libro_prestar.get_disponibles() <= 0:
            print(" - " * 25)
            print("No hay unidades disponibles.")
            print(" - " * 25)
            return

        print("[1]. 1 día")
        print("[2]. 1 semana")
        print("[3]. 2 semanas")
        print("[4]. 1 mes")
        plazo_opcion = int(input("Ingrese la opción del plazo: "))
        plazo_dias = {1: 1, 2: 7, 3: 14, 4: 30}.get(plazo_opcion, 7)

        libro_prestar.set_disponibles(libro_prestar.get_disponibles() - 1)
        usuario.libros_prestados += 1

        fecha_prestamo = datetime.now()
        fecha_devolucion = fecha_prestamo + timedelta(days=plazo_dias)

        nuevo_prestamo = prestamo.Prestamo(usuario, libro_prestar, fecha_prestamo, plazo_dias, fecha_devolucion)
        self.prestamos.append(nuevo_prestamo)

        print(" - " * 25)
        print(f"Préstamo realizado con éxito. {usuario.get_nombre()} ha tomado '{libro_prestar.get_titulo()}'.")
        print(" - " * 25)

    def devolver_libro(self):
        nombre = input("Ingrese su nombre: ").strip()
        codigo = int(input("Ingrese el código del libro: "))

        prestamo_usuario = next((p for p in self.prestamos if p.get_usuario().get_nombre().lower() == nombre.lower() and p.get_libro().get_codigo() == codigo), None)

        if not prestamo_usuario:
            print("No se encontró un préstamo con esos datos.")
            return

        libro_devolver = prestamo_usuario.get_libro()
        libro_devolver.set_disponibles(libro_devolver.get_disponibles() + 1)
        self.prestamos.remove(prestamo_usuario)

        print(f"Libro '{libro_devolver.get_titulo()}' devuelto con éxito.")

    def consultar_prestamos_usuario(self):
        nombre = input("Ingrese el nombre del usuario: ").strip()
        prestamos_usuario = [p for p in self.prestamos if p.get_usuario().get_nombre().lower() == nombre.lower()]

        if prestamos_usuario:
            print(f"Libros prestados por {nombre}:")
            for p in prestamos_usuario:
                print(f"- {p.get_libro().get_titulo()} (Devolver antes del {p.get_fecha_devolucion().strftime('%Y-%m-%d')})")
        else:
            print("Este usuario no tiene libros prestados.")

    def limpiar_consola(self):
        os.system('cls' if os.name == 'nt' else 'clear')
