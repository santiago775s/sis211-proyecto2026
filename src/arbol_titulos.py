class NodoTitulo:
    def __init__(self, clave, libro):
        self.clave = clave
        self.libro = libro
        self.izquierdo = None
        self.derecho = None


class ArbolTitulos:
    def __init__(self):
        self.raiz = None
        self.tamano = 0

    @staticmethod
    def _clave(libro):
        return (libro.titulo.casefold(), libro.isbn)

    def esta_vacio(self):
        return self.raiz is None

    def insertar(self, libro):
        clave = self._clave(libro)
        nuevo = NodoTitulo(clave, libro)
        self.tamano += 1
        if self.raiz is None:
            self.raiz = nuevo
            return
        actual = self.raiz
        while True:
            if clave < actual.clave:
                if actual.izquierdo is None:
                    actual.izquierdo = nuevo
                    return
                actual = actual.izquierdo
            else:
                if actual.derecho is None:
                    actual.derecho = nuevo
                    return
                actual = actual.derecho

    def buscar_por_titulo(self, titulo):
        objetivo = titulo.casefold()
        encontrados = []
        pila = []
        actual = self.raiz
        while pila or actual is not None:
            while actual is not None:
                pila.append(actual)
                actual = actual.izquierdo
            actual = pila.pop()
            titulo_nodo = actual.clave[0]
            if titulo_nodo == objetivo:
                encontrados.append(actual.libro)
            elif titulo_nodo > objetivo:
                break
            actual = actual.derecho
        return encontrados

    def inorden(self):
        resultado = []
        pila = []
        actual = self.raiz
        while pila or actual is not None:
            while actual is not None:
                pila.append(actual)
                actual = actual.izquierdo
            actual = pila.pop()
            resultado.append(actual.libro)
            actual = actual.derecho
        return resultado
