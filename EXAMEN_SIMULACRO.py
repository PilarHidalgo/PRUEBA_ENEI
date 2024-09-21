#EXAMEN
"""Proyecto de programación:


Crea una clase llamada `Miembro` (del hogar). Esta clase tendrá los siguientes atributos:
- nombre
- edad, 
- género, 
- relación con el/la jefe del hogar, 
- estado civil, 
- máximo nivel educativo (será una variable ordinal del 0 al 7).
- discapacidad
- un booleano = 1 si es que trabaja, 
- el salario mensual > 0 si es que trabaja == 1, en caso contrario, y por conveniencia, el salario será 0. 

- La clase debe tener un método para mostrar la información del `Miembro`, pueden ser sólo los 3 primeros atributos. 

Define una clase llamada `Hogar`. Sus únicos parámetros serán una lista con miembros del hogar.     
Los atributos con los que se inicializa esta clase son:
- la lista llamada miembros.    
- el número de miembros del hogar: Para ello, necesitamos calcular la extensión de la lista de miembros.
- máximo nivel educativo del hogar: Para ello, necesitamos definir un método que nos diga el máximo nivel educativo de la lista de miembros.
- ingreso promedio del hogar: Para ello, necesitamos definir un método que sume los ingresos y dividirlos entre el número de miembros. 
- ratio de dependencia, que es el ratio de personas que trabajan sobre las que no trabajan. Para ello, necesitamos calcular $$P_{trabajan}/P_{notrabajan}$$ donde $P_{trabajan}$ son el número de personas que trabajan, y $P_{notrabajan}$, las que no. 

Crea instancias del siguiente hogar: """

class Miembro:
    def __init__(self, nombre, edad, genero, relacion, ecivil, nivel, discapacidad, trabaja, salario):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.relacion = relacion
        self.ecivil = ecivil
        self.niveledu = nivel
        self.discapacidad = discapacidad
        self.trabaja = trabaja
        self.salario = salario

    def __repr__(self):
        return f"{self.nombre},  {self.edad}, {self.ecivil}"
    

class Hogar:
    def __init__(self, lmiembros):
        self.miembros = lmiembros
        self.nmiembros = len(self.miembros)
        self.max_nivel = self.maximo_nivel()
        self.ingreso_promedio = self.calcula_ingreso()
        self.rdependencia = self.ratiodep()


    def maximo_nivel(self):
        maxinivel = 0
        for miembro in self.miembros:
            if miembro.niveledu > maxinivel:
                maxinivel = miembro.niveledu

        return maxinivel
    
    def calcula_ingreso(self):
        ingreso_total = sum([miembro.salario for miembro in self.miembros])
        return ingreso_total/self.nmiembros
    
    def ratiodep(self):
        indep =  sum([miembro.trabaja for miembro in self.miembros])
        dep = self.nmiembros - indep
        return indep/dep