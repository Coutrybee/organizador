import datetime

class Evento:
    eventos = []
    horas = 12
    proporcion_horas = 0
    proporcion_eventos = 0
     
    def __init__(self, nombre, prioridad):

        self.nombre = nombre
        self.prioridad = int(prioridad)
        self.tiempo = 0
        

        if self in Evento.eventos:
            Evento.eventos.remove(self)
        
        Evento.eventos.append(self)
        Evento.eventos.sort()
    
    def __lt__(self, other):
        return self.prioridad < other.prioridad
    
    def __eq__(self, other):
        return self.nombre.lower() == other.nombre.lower()

    def horas_por_dia(self, n_elementos):
        self.tiempo = round((Evento.proporcion_eventos * Evento.proporcion_horas) / self.prioridad,3)

    @staticmethod
    def n_eventos():
        return len(Evento.eventos)

    @staticmethod
    def print():
        for evento in Evento.eventos:
            print(evento.nombre + " \n\tH:m/dia: " + str(datetime.timedelta(hours=evento.tiempo))[:4] + "\n")

    @staticmethod
    def diccionario_prioridades():
        dic = {}
        for evento in Evento.eventos:
            try:
                dic[evento.prioridad] += 1
            except KeyError:
                dic[evento.prioridad] = 1
        
        return dic

    @staticmethod
    def calcular_proporciones():
        suma = 0
        dic = Evento.diccionario_prioridades()
        for key, value in dic.items():
            suma += value / key
        Evento.calcular_proporcion_eventos(suma)
        Evento.calcular_proporcion_horas(suma)  

        for evento in Evento.eventos:
            evento.horas_por_dia(dic[evento.prioridad])

    @staticmethod
    def calcular_proporcion_eventos(suma):        
        Evento.proporcion_eventos = Evento.n_eventos() / suma

    @staticmethod
    def calcular_proporcion_horas(suma):
        # Evento.proporcion_horas = suma * Evento.proporcion_eventos / Evento.horas
        Evento.proporcion_horas = Evento.horas / Evento.n_eventos() 


f_i = open("eventos.dat", "r")
for line in f_i:
    line_s = line.split("|")
    Evento(line_s[0], line_s[1])

# Evento.print()
Evento.calcular_proporciones()
Evento.print()
suma = 0
for evento in Evento.eventos:
    suma += evento.tiempo

print(suma)

    
