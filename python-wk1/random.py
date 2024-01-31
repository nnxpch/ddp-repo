# Practice calculate temperature

def caltemperature(calcius):
    farenheit = (9/5)*calcius + 32
    kelvin = calcius + 273.15
    return farenheit, kelvin

print(caltemperature(41.65))
print(caltemperature(39.85))