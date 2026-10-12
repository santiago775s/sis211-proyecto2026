import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.biblioteca import Biblioteca


class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()
        self.biblioteca.registrar_libro("111", "Algoritmos", "Cormen")
        self.biblioteca.registrar_socio("S1", "Ana")
        self.biblioteca.registrar_socio("S2", "Luis")
        self.biblioteca.registrar_socio("S3", "Marta")

    def test_cola_vacia(self):
        self.assertIsNone(self.biblioteca.siguiente_en_espera("111"))

    def test_libro_inexistente(self):
        self.assertIsNone(self.biblioteca.buscar_libro("999"))

    def test_historial_vacio(self):
        self.assertEqual(self.biblioteca.historial_de_socio("S1"), [])

    def test_prestar_libro_ya_prestado(self):
        self.biblioteca.prestar("111", "S1")
        with self.assertRaises(ValueError):
            self.biblioteca.prestar("111", "S2")

    def test_isbn_duplicado(self):
        with self.assertRaises(ValueError):
            self.biblioteca.registrar_libro("111", "Otro", "Autor")

    def test_orden_fifo_en_lista_de_espera(self):
        self.biblioteca.prestar("111", "S1")
        self.biblioteca.reservar("111", "S2")
        self.biblioteca.reservar("111", "S3")
        self.assertEqual(self.biblioteca.siguiente_en_espera("111").id_socio, "S2")
        recibe = self.biblioteca.devolver("111")
        self.assertEqual(recibe.id_socio, "S2")
        self.assertEqual(self.biblioteca.siguiente_en_espera("111").id_socio, "S3")

    def test_devolver_sin_espera_deja_disponible(self):
        self.biblioteca.prestar("111", "S1")
        self.assertIsNone(self.biblioteca.devolver("111"))
        self.assertTrue(self.biblioteca.buscar_libro("111").disponible)

    def test_historial_en_orden_cronologico(self):
        self.biblioteca.registrar_libro("222", "Estructuras", "Weiss")
        self.biblioteca.prestar("111", "S1")
        self.biblioteca.prestar("222", "S1")
        self.assertEqual(self.biblioteca.historial_de_socio("S1"), ["111", "222"])

    def test_reservar_libro_disponible_se_rechaza(self):
        with self.assertRaises(ValueError):
            self.biblioteca.reservar("111", "S1")


if __name__ == "__main__":
    unittest.main()
