class Book:
    def __init__(self,idbook,auteur,title,datedepub):
        self.__idbook=idbook
        self.__auteur=auteur
        self.__title=title
        self.__datedepub=datedepub
    
    def getidBook(self):
        return self.__idbook

    def getauteur(self):
        return self.__auteur
    
    def gettitle(self):
        return self.__title

    def getdateparu(self):
        return self.__datedepub



