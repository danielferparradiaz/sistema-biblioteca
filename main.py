import Usuario as usr
import Prestamo as prestamo
import Libro as libro
from Funciones import Funciones

usuarios = [
    usr.Usuario("Laura", 11, 0),
    usr.Usuario("Carlos", 12, 0),
    usr.Usuario("Enrique", 13, 1),
    usr.Usuario("Daniel", 14, 0),
    usr.Usuario("Paula", 15, 1),
]

libros = [
    libro.Libro("Citas del Presidente Mao Tse-Tung", "Mao Tse-Tung", 1964, "Politica", 111, 4, 3),
    libro.Libro("Harry Potter", "J.K Rowling", 1997, "fantasia", 112, 10, 1),
    libro.Libro("El Señor de los anillos", "J.R.R. Tolkien", 1954, "fantasia", 113, 7, 3),
    libro.Libro("El Alquimista", "Paulo Coelho", 1991, "Novela narrativa, ficcion", 114, 2, 2),
    libro.Libro("El Código da Vinci", "Dan Brown", 2003, "Novela policíaca Ciencia ficción", 115, 5, 1),
    libro.Libro("Crepúsculo – La saga", "Stephenie Meyer", 2005, "Novela", 116, 8, 2),
    libro.Libro("Lo que el viento se llevó", "Margaret Mitchell", 1936, "Ficción histórica", 117, 19, 5),
    libro.Libro("Piense y hágase rico", "Napoleón Hill", 1937, "Autoayuda; superación personal", 118, 11, 10),
    libro.Libro("El diario de Ana Frank", "Ana Frank", 1947, "Autobiografía", 119, 5, 1),
    libro.Libro("Confieso que he vivido", "Pablo Neruda", 1974, "Memorias y autobiografía", 120, 10, 1),
]

prestamos = []

sistema_biblioteca = Funciones(usuarios, libros, prestamos)
sistema_biblioteca.mostrar_menu()
