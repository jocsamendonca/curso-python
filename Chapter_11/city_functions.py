
def city_country(city, country, population=''):
    """Retorna uma string com cidade e país formatada"""
    if population:
        formatted_name = f"{city}, {country} - population {population}"
    else:
        formatted_name = f"{city}, {country}"
    return formatted_name.title()
