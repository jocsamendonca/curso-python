cities = {
    'fortaleza': {
        'country': 'brasil',
        'population': 2000000,
        'fact': 'capital do Ceára',
    },
    'iguatu': {
        'country': 'brazil',
        'population': 100000,
        'fact': 'Em obras',
    },
    'lisboa': {
        'country': 'portugal',
        'population': 653489,
        'fact': 'Capital de Portugal',
    }
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}:")
    print(f'\tCountry: {city_info['country'].title()}')
    print(f'\tPopulation: {city_info['population']:,}')
    print(f'\tFact: {city_info['fact'].title()}')
    '''
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    
    print(f'\tCoutry: {country.title()}')
    #print('\tPopulation: {:,}'.format(population))
    print(f'\tPopulation: {population:,}')
    print(f'\tFact: {fact.title()}')
    #print(f"\t{city_info}")
    '''