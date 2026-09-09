# SIS-211 · Proyecto de curso (2/2026)

Un mismo software que **crece**: v1 (estructuras simples) → v2 (jerárquicas) → v3 (grafos).

**Hoy solo existe la branch `v1`.** No creen `v2` ni `v3`.

| | |
| --- | --- |
| **Estudiante** | Santiago Torres |
| **Dominio** | Sistema de biblioteca |
| **Repo** | https://github.com/TU-USUARIO/sis211-proyecto2026.git |

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

## Carpetas

- `src/` — clases del dominio (POO). Hoy no codeen.
- `tests/` — un caso límite, cuando implementen.

## Alcance

- v1: clases en `.py` (POO). Entrega Moodle: **2026-10-07 23:59**.
- Este README **no** sustituye la tarea de Moodle.
- v2 y v3: otras branches, más adelante, a partir de `v1`.
