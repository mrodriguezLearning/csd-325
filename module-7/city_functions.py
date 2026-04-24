'''
Marco Rodriguez Gomez
04/23/2026
Assignment: Test Cases
'''
def city_country(city, country, population='', language=''):
    output = f"{city}, {country}"
    if population:
        output += f" - population {population}"
    if language:
        output += f", {language}"
    return output

# calls as requested
print(city_country('Santiago', 'Chile'))
print(city_country('Santiago', 'Chile', 5000000))
print(city_country('Santiago', 'Chile', 5000000, 'Spanish'))