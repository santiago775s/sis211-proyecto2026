# SIS-211 · Proyecto de curso (2/2026)

Un mismo software que **crece**: v1 (estructuras simples) → v2 (jerárquicas) → v3 (grafos).


| | |
| --- | --- |
| **Estudiante** | Santiago Torres |
| **Repo** | https://github.com/santiago775s/sis211-proyecto2026.git |

## Mapa v1 (mínimo tres familias distintas)

Familias: arreglo, lista, pila, cola, tabla hash.
`dict` y `set` son **la misma** familia (hash). Sin árboles ni grafos en v1.

| Flujo del dominio | Qué llega / sale / se busca | Familia | La uso porque… |
| --- | --- | --- | --- |
| Siguiente persona en espera por un libro reservado | Llega gente a reservar el mismo libro y se atiende a quien lo pidió primero | Cola | el orden de llegada importa: el primero en pedirlo será el primero en recibirlo cuando el libro se devuelva, se aplica FIFO. |
| Buscar libro por código o ISBN | Se busca rápido un libro concreto por su código o ISBN | Tabla hash | permite un acceso inmediato por clave sin tener que recorrer todo el catálogo. |
| Catálogo de libros disponibles / historial de préstamos de un usuario | Se muestra una secuencia ordenada de los libros o de los préstamos que hizo un usuario | Lista | ayuda a mantener el orden (alfabético o cronológico) y a recorrer todos los elementos. |

Cómo probar un caso límite (vacío, no encontrado o duplicado):

> - Cola vacía: pedir el siguiente en espera por un libro sin reservas debería responder "No hay nadie en espera" o algo similar.
> - Libro inexistente: buscar un código o ISBN que no existe debería responder "Libro no encontrado" o algo similar.
> - Lista vacía: pedir el historial de préstamos de un usuario sin préstamos debería responder "No hay préstamos" o algo similar.
> - Duplicado: intentar prestar un libro que ya está prestado debería rechazar la operación.

## Mapa v2 (branch `v2`, una jerarquía en un flujo nuevo)

Dominio: sistema de biblioteca (el mismo de v1). Familia nueva: **BST**. Sin grafos.

| Flujo nuevo | Qué llega / sale / se busca | Familia | La uso porque… |
| --- | --- | --- | --- |
| Catálogo ordenado por título y búsqueda por título | Cada libro registrado entra al árbol; sale el catálogo en orden alfabético (recorrido inorden) y se buscan libros por título | BST | cada comparación descarta una rama, así que buscar por título no recorre todo el catálogo, y el recorrido inorden devuelve los libros ya ordenados sin tener que reordenar. |

Clave del árbol: `(título en minúsculas, ISBN)`. Así dos libros con el mismo título no se pisan.

Código: `src/arbol_titulos.py` (`NodoTitulo`, `ArbolTitulos`), usado desde `Biblioteca.catalogo_ordenado()` y `Biblioteca.buscar_por_titulo()`. `Biblioteca.registrar_libro()` inserta además cada libro en el árbol; el resto de v1 no cambia.

Caso límite v2 (vacío o no encontrado):

> - Catálogo vacío: `catalogo_ordenado()` devuelve una lista vacía.
> - Título no encontrado: `buscar_por_titulo("Redes")` devuelve una lista vacía y el programa muestra "Título no encontrado".

Pruebas: `python -m unittest discover -s tests -v`. Las de v2 están en `tests/test_v2_catalogo.py`.

## Carpetas

- `src/` — clases del dominio (POO).
- `tests/` — casos límite de v1 y de v2.

## Alcance

- v1: clases en `.py` (POO). Entrega Moodle: **2026-10-07 23:59**.
- Este README **no** sustituye la tarea de Moodle.
- v2: branch `v2`, creada desde `v1`. Entrega Moodle: **2026-11-04 23:59**.
- v3: otra branch, más adelante, a partir de `v2`.
