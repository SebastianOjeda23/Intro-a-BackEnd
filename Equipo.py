class Equipo:
    def __init__(self,Nombre,Ciudad,Campeonatos,Sponsor):
        self.__Nombre = Nombre
        self.__Ciudad = Ciudad
        self.__Campeonatos = Campeonatos
        self.__Sponsor = Sponsor
        self.__Jugadores = []

    def set_Nombre(self,Nombre):
        self.__Nombre = Nombre
    def set_Ciudad(self,Ciudad):
        self.__Ciudad = Ciudad
    def set_Campeonatos(self,Campeonatos):
        self.__Campeonatos = Campeonatos
    def set_Sponsor(self,Sponsor):
        self.__Sponsor = Sponsor
    #Carga masiva de jugadores
    def set_Jugadores(self,Jugadores):
        self.__Jugadores = Jugadores

    def get_Nombre(self):
        return self.__Nombre
    def get_Ciudad(self):
        return self.__Ciudad
    def get_Campeonatos(self):
        return self.__Campeonatos
    def get_Sponsor(self):
        return self.__Sponsor
    def get_Jugadores(self):
        return self.__Jugadores
    
    def __str__(self):
        return "Nombre de equipo: "+self.__Nombre
    
    
    def Mostrar_Todo(self):
        txt = "Nombre de equipo: "+self.__Nombre
        txt += "Nombre ciudad: "+self.__Ciudad
        txt += "Campeonatos: "+self.__Campeonatos
        txt += "Sponsor: "+self.__Sponsor
        return txt
    
    def Contratar_Jugador(self,Jugador):
        if Jugador in self.__Jugadores:
            print("Ya esta en el equipo.")
        else: 
            self.__Jugadores.append(Jugador)

    def Despedir_Jugador(self,Jugador):
        if Jugador not in self.__Jugadores:
            print("No esta en el equipo.")
        else:
            self.__Jugadores.remove(Jugador)
    