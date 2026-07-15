# Simulación de Cola de Impresión

## Descripción
Este proyecto implementa una **cola de impresión** en Python utilizando la clase `Queue` basada en listas enlazadas.  
La cola respeta estrictamente el principio **FIFO (First In, First Out)**: el primer trabajo en entrar es el primero en salir.

## Algoritmo
1. Recibir y validar los datos capturados (usuario, documento, páginas).
2. Crear un objeto `TrabajoImpresion`.
3. Asignar un consecutivo de llegada.
4. Agregar el objeto al final de la cola mediante `enqueue`.
5. Actualizar la lista o tabla de trabajos pendientes.
6. Para imprimir, comprobar primero que la cola no esté vacía.
7. Retirar el elemento del frente mediante `dequeue`.
8. Mostrar un mensaje con el documento procesado y actualizar la interfaz.
9. Si no existen trabajos pendientes, informar al usuario sin generar excepción.

## Operaciones de la clase Queue
- **enqueue(data):** Inserta un trabajo al final de la cola.
- **dequeue():** Retira el trabajo al frente de la cola.
- **firstQueue():** Consulta el primer trabajo sin eliminarlo.
- **lastQueue():** Consulta el último trabajo sin eliminarlo.
- **printQueue():** Devuelve todos los trabajos en orden FIFO.
- **isEmpty():** Verifica si la cola está vacía.

## Ejemplo de uso
```python
gestor = GestorImpresion()
gestor.agregar_trabajo("Alejandro", "Tesis.pdf", 120)
gestor.agregar_trabajo("María", "Reporte.docx", 15)
print(gestor.listar_trabajos())  # Muestra la cola
print(gestor.imprimir_siguiente())  # Atiende el primer trabajo