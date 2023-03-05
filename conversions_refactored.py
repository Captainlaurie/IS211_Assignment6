def convert(fromUnit, toUnit, value):
    """
    Converts between Fahrenheit, Celsius and Kelvin, and
    Converts between Miles, Yards and Meters.
    :param fromUnit:
    :param toUnit:
    :param value:
    :return:
    """
    
    #Temperature Conversions
    if fromUnit.upper() == toUnit.upper():
        return value
    
    #from Celsius
    if fromUnit.upper() == 'Celsius' and toUnit.upper() == 'Kelvin':
        return value + 273.15
    
    if fromUnit.upper() == 'Celsius' and toUnit.upper() == 'Fahrenheit':
        return (9/5 * value) + 32
    
    #From Fahrenheit
    if fromUnit.upper() == 'Fahrenheit' and toUnit.upper() == 'Celsius':
        return (value - 32) * 5/9
    
    
    if fromUnit.upper() == 'Fahrenheit' and toUnit.upper() == 'Kelvin':
        return (value + 459.67) * 5/9
    
    #From Kelvin
    if fromUnit.upper() == 'Kelvin' and toUnit.upper() == 'Fahrenheit':
        return (value * 9/5) - 459.67
    
    
    if fromUnit.upper() == 'Kelvin' and toUnit.upper() == 'Celsius':
        return value - 273.15
    
    
    #Distance Conversions
    
    #From Yards
    if fromUnit.upper() == 'Yards' and toUnit.upper() == 'Meters':
        return value / 1.09361
    
    
    if fromUnit.upper() == 'Yards' and toUnit.upper() == 'Miles':
        return value 
    
    #From Meters
    if fromUnit.upper() == 'Meters' and toUnit.upper() == 'Yards':
        return value * 1.09361
    
    
    if fromUnit.upper() == 'Meters' and toUnit.upper() == 'Miles':
        return value 
    
    #From Miles
    if fromUnit.upper() == 'Miles' and toUnit.upper() == 'Yards':
        return value 
    
    
    if fromUnit.upper() == 'Miles' and toUnit.upper() == 'Meters':
        return value 