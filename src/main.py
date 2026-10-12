import sys
from pathlib import Path

try:
    from .biblioteca import Biblioteca
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from src.biblioteca import Biblioteca


def main():
    biblioteca = Biblioteca()
    biblioteca.registrar_libro("978-0-13-110362-7", "The C Programming Language", "Kernighan y Ritchie")
    biblioteca.registrar_libro("978-0-262-03384-8", "Introduction to Algorithms", "Cormen")
    biblioteca.registrar_socio("S1", "Ana")
    biblioteca.registrar_socio("S2", "Luis")
    biblioteca.registrar_socio("S3", "Marta")

    isbn = "978-0-262-03384-8"
    biblioteca.prestar(isbn, "S1")
    biblioteca.reservar(isbn, "S2")
    biblioteca.reservar(isbn, "S3")

    siguiente = biblioteca.siguiente_en_espera(isbn)
    print("Siguiente en espera:", siguiente if siguiente else "No hay nadie en espera")

    recibe = biblioteca.devolver(isbn)
    print("Recibe el libro:", recibe if recibe else "Nadie, queda disponible")

    libro = biblioteca.buscar_libro("000")
    print("Búsqueda 000:", libro if libro else "Libro no encontrado")

    historial = biblioteca.historial_de_socio("S1")
    print("Historial de S1:", historial if historial else "No hay préstamos")


if __name__ == "__main__":
    main()
