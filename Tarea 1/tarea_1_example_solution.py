def potencia_manual(base, potencia):
    '''Funcion que toma dos numeros como entradas y devuelve como salidas un
    estado, para saber si se pudo realizar la operacion correctamente
    y el resultado de la operacion base^potencia'''
    def Multiplicacion(n1, n2):
        '''Se crea una funcion para multiplicar
        a base de sumas toma como entrada dos numeros y tiene otro
         numero como salida'''
        i = 1
        a = n1
        if n2 == 0:
            return 0
        else:
            for i in range(i, n2):
                # Suma el primer numero las veces que le diga el segundo numero
                a = a + n1
                i = i + 1
            else:
                return (a)
    k = 0
    result = 1
    estado = 9999
    if type(base) == int:  # revisa si la base es un entero
        if type(potencia) == int:  # revisa si la potencia es un entero
            if base == 0:  # Caso especial. Ademas, se asume que 0^0=0
                estado = 0
# como la base y la potencia son numeros, se tiene un codigo de exito
                result = 0
                return (estado), (result)
# multiplica la base varias veces , tantas como le diga la potencia
            else:
                for i in range(k, potencia):
                    result = Multiplicacion(result, base)
                    k = k + 1
                else:
                    estado = 0
# como la base y la potencia son numeros, se tiene un codigo de exito
                    return (estado), (result)
        else:
            estado = -400
            # codigo de error para cuando la base o la potencia no son numeros
            result = None
            # resultado cuando la base o la potencia no son numeros
            return (estado), (result)
    else:
        estado = -400
        # codigo de error para cuando la base o la potencia no son numeros
        result = None  # resultado cuando la base o la potencia no son numeros
        return (estado), (result)


def separa_letras(Cadena):
    '''Funcion que recibe un texto y devuelve como salidas un
    estado, para saber si se pudo realizar la operacion
    correctamente y dos strings, uno de letras mayusculas y
    otro de minusculas'''
    estado = 7777
    res1 = 0
    res2 = 0
    if type(Cadena) == int:  # Si es un numero
        estado = -100  # Codigo de error unico
        res1 = None  # Resultado si hay un error
        res2 = None  # Resultado si hay un error
        return (estado), (res1), (res2)

    elif len(Cadena) == 0:  # Si esta vacio
        estado = -300  # Codigo de error unico
        res1 = None  # Resultado si hay un error
        res2 = None  # Resultado si hay un error
        return (estado), (res1), (res2)
    else:
        for char in Cadena:  # Si tiene caracteres especiales
            if char in "!#$%&'()*+, -.\"/:;<=>?@[\]^_`{|}~":
                estado = -200  # Codigo de error unico
                res1 = None  # Resultado si hay un error
                res2 = None  # Resultado si hay un error
                return (estado), (res1), (res2)
            else:
                pass  # para salir del ciclo for
        else:
            import re
            estado = 0  # Codigo de exito
            res1 = re.sub('[^A-Z]', '', Cadena)
            # Funcion para eliminar las minusculas
            res2 = re.sub('[^a-z]', '', Cadena)
            # Funcion para eliminar las mayusculas
            return (estado), (res1), (res2)