class Jugador:
    def __init__(self,Nombre,Nacionalidad,Estatura):
        self.__Nombre = Nombre
        self.__Nacionalidad = Nacionalidad
        self.__Estatura = Estatura

    def set_Nombre(self,Nombre):
        self.__Nombre = Nombre
    def set_Nacionalidad(self,Nacionalidad):
        self.__Nacionalidad = Nacionalidad
    def set_Estatura(self,Estatura):
        self.__Estatura = Estatura

    def get_Nombre(self):
        return self.__Nombre
    def get_Nacionalidad(self):
        return self.__Nacionalidad
    def get_Estatura(self):
        return self.__Estatura
    
    def __str__(self):
        return self.__Nombre
    def Mostrar_Todo(self):
        txt = "Nombre: "+self.__Nombre
        txt += "Nacionalidad: "+self.__Nacionalidad
        txt += "Estatura: "+self.__Estatura
        return txt