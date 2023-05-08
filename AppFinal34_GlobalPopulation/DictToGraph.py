def GetPopulation(CountryDict):
    
    print('result')
    print(CountryDict)
    print(CountryDict['2022 Population'])
    populationDic = {
        '2022': CountryDict['2022 Population'],
        '2020': CountryDict['2020 Population'],
        '2015': CountryDict['2015 Population'],
        '2010': CountryDict['2010 Population'],
        '2000': CountryDict['2000 Population'],
        '1990': CountryDict['1990 Population'],
        '1980': CountryDict['1980 Population'],
        '1970': CountryDict['1970 Population'],
    }
    

    
    return populationDic.keys(),populationDic.values()
