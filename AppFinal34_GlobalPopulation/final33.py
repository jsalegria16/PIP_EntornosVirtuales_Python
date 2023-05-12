import grafico
import DictToGraph
import FiltrarPais
import leercsv

import pandas as pd 


def run():


    MyDAtaFrame = pd.read_csv('33world_population.csv',sep=',')
    
    MyDAtaFrame = MyDAtaFrame[MyDAtaFrame['Continent']=='Asia']
    countries = MyDAtaFrame['Country/Territory'].values
    percentages = MyDAtaFrame['World Population Percentage'].values
    
    print(countries,percentages)
    grafico.generatePieChart(countries,percentages);
    grafico.generateBarChart(countries,percentages)

'''  
    MyCountries = list(filter(lambda item: item['Continent']=='South America',MyCountries))

    NewDict = {item['Country/Territory']: item['World Population Percentage'] for item in MyCountries}
    
    Keys = NewDict.keys()
    Values = NewDict.values()

'''

                    
if __name__ == '__main__':
    run()
    


 