1. El Rol de la Pila en la Conversión (Infija a Posfija)
En esta primera etapa (método infija_a_posfija), la pila se utiliza exclusivamente para guardar y ordenar los operadores y paréntesis, asegurando que se respete la jerarquía matemática de los signos. Los números nunca entran a la pila aquí; pasan directamente a la lista de salida.

Reglas lógicas que ejecuta la pila:
Si es un número: Se va directo a la salida.

Si es un paréntesis abierto (: Se guarda en la pila inmediatamente.

Si es un paréntesis cerrado ): La pila empieza a sacar (pop) operadores y a mandarlos a la salida hasta que encuentra el ( que le corresponde.

Si es un operador (+, -, *, /, $): No se puede apilar un operador sobre otro de igual o mayor jerarquía. Si el operador en la cima de la pila tiene mayor o igual prioridad que el que acaba de llegar, la pila saca (pop) al viejo, lo manda a la salida, y luego acepta (push) al nuevo.

Ejemplo de traza con la expresión 2 + 3 * 4:
Token 2: Es un número. Pasa directo a la salida.

Salida: 2 | Pila: [ Vacía ]

Token +: Es un operador. Como la pila está vacía, entra con un push.

Salida: 2 | Pila: [ + ]

Token 3: Es un número. Pasa directo a la salida.

Salida: 2 3 | Pila: [ + ]

Token *: Es un operador. Se compara su prioridad (2) con la de la cima de la pila, que es + (1). Como el * tiene mayor prioridad, se permite colocarlo encima con un push.

Salida: 2 3 | Pila: [ * , + ] (el asterisco está arriba)

Token 4: Es un número. Pasa directo a la salida.

Salida: 2 3 4 | Pila: [ * , + ]

Fin de la expresión: El ciclo de lectura termina, por lo tanto, se vacía todo lo que quede dentro de la pila de arriba hacia abajo haciendo pop.

Primer pop: Saca el * y lo manda a la salida.

Segundo pop: Saca el + y lo manda a la salida.

Resultado Final de la Conversión: 2 3 4 * +

2. El Rol de la Pila en la Evaluación (Cálculo del Resultado)
En esta segunda etapa (método evaluar_posfija), el comportamiento de la pila se invierte por completo. Ahora, la pila se utiliza exclusivamente para guardar los números (operandos), mientras que los operadores sirven como el disparador automático que ejecuta las operaciones matemáticas.

Reglas lógicas que ejecuta la pila:
Si es un número: Se convierte de texto a entero (int) y se guarda en la pila con un push.

Si es un operador: Se retiran de inmediato los dos últimos números de la pila usando pop(). Se realiza la operación matemática correspondiente y el resultado parcial se vuelve a guardar en la pila con un push.

Ejemplo de traza con la expresión obtenida 2 3 4 * +:
Token 2: Es un número. Hace push(2).

Pila: [ 2 ]

Token 3: Es un número. Hace push(3).

Pila: [ 3 , 2 ]

Token 4: Es un número. Hace push(4).

Pila: [ 4 , 3 , 2 ] (el 4 está en la cima)

Token *: Es un operador.

Primer pop(): Extrae el operando derecho = 4.

Segundo pop(): Extrae el operando izquierdo = 3.

Se calcula: 3 * 4 = 12.

Se hace push(12) del resultado.

Pila: [ 12 , 2 ]

Token +: Es un operador.

Primer pop(): Extrae el operando derecho = 12.

Segundo pop(): Extrae el operando izquierdo = 2.

Se calcula: 2 + 12 = 14.

Se hace push(14) del resultado final.

Pila: [ 14 ]

Fin de la expresión: El programa hace un último pop() y devuelve el número 14, que es el resultado definitivo que se imprime en tu pantalla.