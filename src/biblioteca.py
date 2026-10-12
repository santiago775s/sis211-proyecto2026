from .libro import Libro
from .socio import Socio


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.socios = {}

    def registrar_libro(self, isbn, titulo, autor):
        if isbn in self.libros:
            raise ValueError("Ya existe un libro con ese ISBN")
        libro = Libro(isbn, titulo, autor)
        self.libros[isbn] = libro
        return libro

    def registrar_socio(self, id_socio, nombre):
        if id_socio in self.socios:
            raise ValueError("Ya existe un socio con ese código")
        socio = Socio(id_socio, nombre)
        self.socios[id_socio] = socio
        return socio

    def buscar_libro(self, isbn):
        return self.libros.get(isbn)

    def prestar(self, isbn, id_socio):
        libro = self._obtener_libro(isbn)
        socio = self._obtener_socio(id_socio)
        if not libro.disponible:
            raise ValueError("El libro ya está prestado")
        self._asignar(libro, socio)
        return socio

    def reservar(self, isbn, id_socio):
        libro = self._obtener_libro(isbn)
        self._obtener_socio(id_socio)
        if libro.disponible:
            raise ValueError("El libro está disponible, puede prestarse directamente")
        if libro.prestado_a == id_socio:
            raise ValueError("El socio ya tiene este libro")
        libro.encolar(id_socio)

    def devolver(self, isbn):
        libro = self._obtener_libro(isbn)
        if libro.disponible:
            raise ValueError("El libro no está prestado")
        libro.prestado_a = None
        id_siguiente = libro.sacar_siguiente()
        if id_siguiente is None:
            return None
        socio = self.socios[id_siguiente]
        self._asignar(libro, socio)
        return socio

    def siguiente_en_espera(self, isbn):
        libro = self._obtener_libro(isbn)
        id_siguiente = libro.proximo_en_espera()
        if id_siguiente is None:
            return None
        return self.socios[id_siguiente]

    def historial_de_socio(self, id_socio):
        return self._obtener_socio(id_socio).obtener_historial()

    def _asignar(self, libro, socio):
        libro.prestado_a = socio.id_socio
        socio.registrar_prestamo(libro.isbn)

    def _obtener_libro(self, isbn):
        libro = self.libros.get(isbn)
        if libro is None:
            raise KeyError("Libro no encontrado")
        return libro

    def _obtener_socio(self, id_socio):
        socio = self.socios.get(id_socio)
        if socio is None:
            raise KeyError("Socio no encontrado")
        return socio
