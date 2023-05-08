import grafico
import DictToGraph
import FiltrarPais
import leercsv

def run():

    MyCountries = leercsv.readcsvfunc('33world_population.csv')
    
    MyCountries = list(filter(lambda item: item['Continent']=='South America',MyCountries))

    NewDict = {item['Country/Territory']: item['World Population Percentage'] for item in MyCountries}
    
    Keys = NewDict.keys()
    Values = NewDict.values()
    
    print(Keys,Values)
    grafico.generatePieChart(Keys,Values);
    grafico.generateBarChart(Keys,Values)

                    
if __name__ == '__main__':
    run()
    


 