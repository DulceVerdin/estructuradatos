1 . ¿Cuál es la función de la clase NodeTree?
Representar cada nodo del árbol binario, almacenando un valor y las referencias a sus hijos izquierdo y derecho

2 . ¿Qué representa el atributo root?
Representa la raíz del árbol binario, es decir, el primer nodo del árbol

3 . ¿Qué significa que un nodo tenga como hijo el valor None?
Significa que ese nodo no tiene hijo en ese lado (izquierdo o derecho)


4 . ¿Cuál es el caso base del método _insertar?

if node is None:
    return NodeTree(value)

Cuando la posición está vacía, se crea un nuevo nodo

5 . ¿Qué sucede cuando _insertar encuentra una posición vacía?
Crea un nuevo nodo con el valor recibido y lo devuelve para insertarlo en el árbol

6 . ¿Por qué se utiliza return node al final del método _insertar?
Para conservar las conexiones entre los nodos y mantener correctamente la estructura del árbol

7 . ¿Qué sucede cuando se intenta insertar un valor repetido?
Se muestra el mensaje "El valor ya existe en el árbol." y el valor no se inserta nuevamente

8 . ¿Cómo decide el método buscar si debe continuar a la izquierda o a la derecha?
Si el valor buscado es menor que el del nodo actual, continúa a la izquierda; si es mayor, continúa a la derecha

9 . ¿Cuál es el caso base de la búsqueda?

if node is None:
    return False

Si llega a una posición vacía, significa que el valor no existe

10 , ¿Cuál es el caso base de los recorridos?

if node is not None:

Solo continúa el recorrido cuando el nodo existe

11 . ¿En qué momento se muestra la raíz en el recorrido preorden?
Al inicio del recorrido, antes de visitar los hijos izquierdo y derecho

12 . ¿En qué momento se muestra la raíz en el recorrido inorden?
Después de recorrer el subárbol izquierdo y antes de recorrer el derecho

13 . ¿En qué momento se muestra la raíz en el recorrido posorden?
Al final, después de recorrer los subárboles izquierdo y derecho

14 . ¿Por qué el recorrido inorden muestra los valores ordenados?
Porque visita primero los valores menores (izquierda), luego la raíz y finalmente los valores mayores (derecha), respetando las reglas del árbol binario de búsqueda

15 . ¿Qué sucede si los valores se insertan de menor a mayor?
El árbol pierde su equilibrio y se forma como una lista enlazada hacia la derecha, haciendo menos eficiente la búsqueda

16 . ¿Cuál es la diferencia entre el while del menú y las llamadas utilizadas dentro de la clase BinaryTree?
El while mantiene activo el menú para que el usuario realice varias operaciones. Las llamadas dentro de BinaryTree ejecutan las operaciones del árbol mediante recursividad

17 . ¿Qué parte del programa evita que se ingresen letras cuando se solicita un número?
El bloque:

try:
    
except ValueError:
    print("Debes ingresar un número entero.")

que captura el error cuando se introduce un dato no numérico

18 . ¿Por qué la forma del árbol depende del orden de inserción?
Porque cada nuevo valor se coloca comparándolo con los nodos existentes. Un orden diferente de inserción produce una estructura diferente del árbol

19 . ¿Por qué desde el menú no se debe acceder directamente a tree.root?
Porque root es un atributo interno de la clase. El menú debe utilizar únicamente los métodos públicos para respetar la encapsulación y evitar modificar directamente la estructura del árbol

20 . ¿Qué función cumplen los métodos _preorden, _inorden y _posorden?
Son métodos auxiliares recursivos que realizan los recorridos del árbol comenzando desde un nodo determinado. Los métodos públicos (preorden, inorden y posorden) los llaman iniciando desde la raíz del árbol