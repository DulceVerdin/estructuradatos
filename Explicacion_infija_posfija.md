El documento explica cómo funciona el algoritmo Shunting-Yard, que convierte una expresión infija (como A + B * C) en una expresión posfija utilizando una pila (Stack).
Los puntos principales son:
La pila se utiliza para almacenar temporalmente operadores y paréntesis mientras se procesa la expresión.
Los operandos (letras o números) se envían directamente a la salida.
Los paréntesis de apertura ( se apilan.
Los paréntesis de cierre ) hacen que se desapilen los operadores hasta encontrar el (, el cual se elimina.
Los operadores (+, -, *, /, $) comparan su prioridad con el operador que está en la cima de la pila. Si el de la pila tiene mayor o igual prioridad, se desapila y se envía a la salida; después se apila el operador actual.
El documento también describe las funciones principales de la pila:
Push: agregar un elemento.
Top/Peek: consultar el elemento superior sin eliminarlo.
Pop: eliminar y devolver el elemento superior.
is_empty: verificar si la pila está vacía.
Como ejemplo, convierte la expresión A + B * C en A B C * +, demostrando que la multiplicación tiene prioridad sobre la suma.
Finalmente, incluye algunos prompts de evidencia utilizados durante el desarrollo del proyecto para documentar la implementación, la corrección de errores y la integración de la interfaz gráfica con la estructura de datos.