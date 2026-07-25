¿Cuál es la función de la clase NodeTree?
La clase NodeTree sirve para crear cada uno de los nodos del árbol, guardando un valor y las referencias a sus hijos izquierdo y derecho.
¿Qué representa el atributo root?
El atributo root representa el nodo principal del árbol, desde donde comienzan todas las operaciones.
¿Qué significa que un nodo tenga como hijo el valor None?
Significa que en ese lado del nodo no existe otro nodo conectado.
¿Cuál es el caso base del método _insertar?
El caso base ocurre cuando el nodo actual es None; en ese momento se crea el nuevo nodo.
¿Qué sucede cuando _insertar encuentra una posición vacía?
Se genera un nuevo nodo con el valor recibido y se coloca en esa posición.
¿Por qué se utiliza return node al final del método _insertar?
Porque permite mantener unidas correctamente las ramas del árbol después de insertar un nuevo nodo.
¿Qué sucede cuando se intenta insertar un valor repetido?
El programa informa que el valor ya existe y no lo vuelve a agregar al árbol.
¿Cómo decide el método buscar si debe continuar a la izquierda o a la derecha?
Compara el valor buscado con el del nodo actual: si es menor va a la izquierda y si es mayor continúa por la derecha.
¿Cuál es el caso base de la búsqueda?
Cuando se llega a un nodo con valor None, la búsqueda termina indicando que el dato no fue encontrado.
¿Cuál es el caso base de los recorridos?
El recorrido se detiene cuando el nodo actual no existe (None).
¿En qué momento se muestra la raíz en el recorrido preorden?
La raíz se imprime primero y después se recorren sus hijos.
¿En qué momento se muestra la raíz en el recorrido inorden?
La raíz se muestra después de recorrer el lado izquierdo y antes de recorrer el lado derecho.
¿En qué momento se muestra la raíz en el recorrido posorden?
La raíz se imprime al final, después de visitar ambos subárboles.
¿Por qué el recorrido inorden muestra los valores ordenados?
Porque siempre visita primero los valores menores, luego el nodo principal y al final los valores mayores.
¿Qué sucede si los valores se insertan de menor a mayor?
El árbol se inclina hacia la derecha y deja de estar equilibrado, pareciéndose a una lista.
¿Cuál es la diferencia entre el while del menú y las llamadas utilizadas dentro de la clase BinaryTree?
El while mantiene el programa funcionando para que el usuario pueda elegir varias opciones, mientras que los métodos de BinaryTree realizan las operaciones del árbol.
¿Qué parte del programa evita que se ingresen letras cuando se solicita un número?
El bloque try-except detecta el error y muestra un mensaje si el usuario escribe algo que no es un número.
¿Por qué la forma del árbol depende del orden de inserción?
Porque cada nuevo valor se coloca comparándolo con los anteriores, así que cambiar el orden produce una estructura diferente.
¿Por qué desde el menú no se debe acceder directamente a tree.root?
Porque la raíz es un atributo interno del árbol y debe manejarse únicamente mediante los métodos de la clase.
¿Qué función cumplen los métodos _preorden, _inorden y _posorden?
Son métodos recursivos que realizan cada tipo de recorrido del árbol empezando desde un nodo determinado y son llamados por los métodos públicos correspondientes.