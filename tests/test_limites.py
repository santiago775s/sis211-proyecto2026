import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.biblioteca import Biblioteca


class TestCasosLimite(unittest.TestCase):
    """Casos límite definidos en el README (vacío, no encontrado, duplicado)."""

    def setUp(self):
        self.biblioteca = Biblioteca()
        self.biblioteca.registrar_libro("111", "Algoritmos", "Cormen")
        self.biblioteca.registrar_socio("S1", "Ana")
        self.biblioteca.registrar_socio("S2", "Luis")

    def test_cola_vacia(self):
        # Cola vacía: pedir el siguiente en espera cuando no hay reservas
        self.assertIsNone(self.biblioteca.siguiente_en_espera("111"))

    def test_libro_inexistente(self):
        # Libro inexistente: buscar un código o ISBN que no existe
        self.assertIsNone(self.biblioteca.buscar_libro("999"))

    def test_historial_vacio(self):
        # Lista vacía: historial de socio sin préstamos
        self.assertEqual(self.biblioteca.historial_de_socio("S1"), [])

    def test_prestar_libro_ya_prestado(self):
        # Duplicado: intentar prestar un libro que ya está prestado
        self.biblioteca.prestar("111", "S1")
        with self.assertRaises(ValueError):
            self.biblioteca.prestar("111", "S2")

    def test_isbn_duplicado(self):
        # Duplicado: intentar registrar un libro con un ISBN ya existente
        with self.assertRaises(ValueError):
            self.biblioteca.registrar_libro("111", "Otro", "Autor")


def test_caso_limite():
    """Función de prueba para compatibilidad con pytest/runners directos."""
    b = Biblioteca()
    b.registrar_libro("111", "Algoritmos", "Cormen")
    assert b.siguiente_en_espera("111") is None
    assert b.buscar_libro("999") is None


if __name__ == "__main__":
    unittest.main()
