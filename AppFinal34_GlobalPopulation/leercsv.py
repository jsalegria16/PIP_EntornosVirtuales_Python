import csv

def readcsvfunc(MyPath):
    with open(MyPath, 'r') as MyCsv:
        reader = csv.reader(MyCsv, delimiter=',') ## A iterable
        NameColuoms = next(reader) # LA primera fila son los n0mbres de las columnas
        ListCountryDict = []

        for row in reader:
            MyItereable = zip(NameColuoms,row) # Lista de tuplas (NombreColumna,Valor)
            CountryDict = {key:value for key,value in MyItereable} # Genero un diccionario 
            ListCountryDict.append(CountryDict)# Agrego cada diccionario a la lista.
        return ListCountryDict