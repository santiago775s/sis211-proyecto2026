import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.arbol_titulos import ArbolTitulos
from src.biblioteca import Biblioteca


class TestCatalogoOrdenado(unittest.TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()

    def test_catalogo_vacio(self):
        self.assertEqual(self.biblioteca.catalogo_ordenado(), [])
        self.assertTrue(self.biblioteca.catalogo.esta_vacio())

    def test_titulo_no_encontrado_en_catalogo_vacio(self):
        self.assertEqual(self.biblioteca.buscar_por_titulo("Algoritmos"), [])

    def test_titulo_no_encontrado(self):
        self.biblioteca.registrar_libro("111", "Algoritmos", "Cormen")
        self.assertEqual(self.biblioteca.buscar_por_titulo("Redes"), [])

    def test_orden_alfabetico(self):
        self.biblioteca.registrar_libro("1", "Redes", "Tanenbaum")
        self.biblioteca.registrar_libro("2", "Algoritmos", "Cormen")
        self.biblioteca.registrar_libro("3", "Estructuras", "Weiss")
        self.biblioteca.registrar_libro("4", "bases de datos", "Date")
        titulos = [l.titulo for l in self.biblioteca.catalogo_ordenado()]
        self.assertEqual(titulos, ["Algoritmos", "bases de datos", "Estructuras", "Redes"])

    def test_buscar_ignora_mayusculas(self):
        self.biblioteca.registrar_libro("2", "Algoritmos", "Cormen")
        encontrados = self.biblioteca.buscar_por_titulo("ALGORITMOS")
        self.assertEqual([l.isbn for l in encontrados], ["2"])

    def test_titulos_repetidos_con_distinto_isbn(self):
        self.biblioteca.registrar_libro("2", "Algoritmos", "Cormen")
        self.biblioteca.registrar_libro("1", "Algoritmos", "Sedgewick")
        encontrados = self.biblioteca.buscar_por_titulo("Algoritmos")
        self.assertEqual([l.isbn for l in encontrados], ["1", "2"])

    def test_arbol_sesgado_no_falla(self):
        arbol = ArbolTitulos()
        biblioteca = Biblioteca()
        for i in range(2000):
            libro = biblioteca.registrar_libro(f"{i:05d}", "mismo titulo", "A")
            arbol.insertar(libro)
        self.assertEqual(len(arbol.inorden()), 2000)

    def test_isbn_duplicado_no_altera_el_arbol(self):
        self.biblioteca.registrar_libro("111", "Algoritmos", "Cormen")
        with self.assertRaises(ValueError):
            self.biblioteca.registrar_libro("111", "Otro", "Autor")
        self.assertEqual(len(self.biblioteca.catalogo_ordenado()), 1)


if __name__ == "__main__":
    unittest.main()
