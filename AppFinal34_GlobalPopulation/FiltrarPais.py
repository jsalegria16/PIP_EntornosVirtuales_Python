
def PopulationByCountry(countries,country):
    result = list(filter(lambda item:item['Country/Territory']==country,countries))
    
    print(result)
    return result