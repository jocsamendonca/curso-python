from city_functions import city_country

def test_city_country():
    """Cidades e países como 'Santiago, Chile' funcionam?"""
    formatted_name = city_country('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'

def test_city_country_populatoon():
    """Cidade, País e População funcionam?"""
    formatted_name = city_country('santiago', 'chile', population=5000000)
    assert formatted_name == 'Santiago, Chile - Population 5000000'