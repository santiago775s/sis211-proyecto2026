from collections import deque


class Libro:
    def __init__(self, isbn, titulo, autor):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.prestado_a = None
        self.lista_espera = deque()

    @property
    def disponible(self):
        return self.prestado_a is None

    def encolar(self, id_socio):
        if id_socio in self.lista_espera:
            raise ValueError("El socio ya está en la lista de espera")
        self.lista_espera.append(id_socio)

    def proximo_en_espera(self):
        if not self.lista_espera:
            return None
        return self.lista_espera[0]

    def sacar_siguiente(self):
        if not self.lista_espera:
            return None
        return self.lista_espera.popleft()

    def __str__(self):
        estado = "disponible" if self.disponible else f"prestado a {self.prestado_a}"
        return f"[{self.isbn}] {self.titulo} - {self.autor} ({estado})"
