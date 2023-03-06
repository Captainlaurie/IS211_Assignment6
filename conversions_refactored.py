class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):
    """
    Converts between Fahrenheit, Celsius and Kelvin, and
    Converts between Miles, Yards and Meters.
    :param fromUnit:
    :param toUnit:
    :param value:
    :return:
    """
    
    # Check if units are compatible
    temperature_units = ['CELSIUS', 'FAHRENHEIT', 'KELVIN']
    distance_units = ['YARDS', 'METERS', 'MILES']
    
    if fromUnit.upper() not in temperature_units and fromUnit.upper() not in distance_units:
        raise ConversionNotPossible(f"Conversion from {fromUnit.upper()} is not possible.")
        
    if toUnit.upper() not in temperature_units and toUnit.upper() not in distance_units:
        raise ConversionNotPossible(f"Conversion to {toUnit.upper()} is not possible.")
    
    if fromUnit.upper() in temperature_units and toUnit.upper() in distance_units:
        raise ConversionNotPossible(f"Conversion between {fromUnit.upper()} and {toUnit.upper()} is not possible.")
        
    if fromUnit.upper() in distance_units and toUnit.upper() in temperature_units:
        raise ConversionNotPossible(f"Conversion between {fromUnit.upper()} and {toUnit.upper()} is not possible.")

        
    #return same value if units are the same
    if fromUnit.upper() == toUnit.upper():
        return value
    
    
    #Temperature Conversions
    
    #from Celsius to Kelvin
    if fromUnit.upper() == 'CELSIUS' and toUnit.upper() == 'KELVIN':
        return value + 273.15
    
    #from Celsius to Fahrenheit
    if fromUnit.upper() == 'CELSIUS' and toUnit.upper() == 'FAHRENHEIT':
        return (9/5 * value) + 32
    
    #From Fahrenheit to Celsius
    if fromUnit.upper() == 'FAHRENHEIT' and toUnit.upper() == 'CELSIUS':
        return (value - 32) * 5/9
    
    #From Fahrenheit to Kelvin
    if fromUnit.upper() == 'FAHRENHEIT' and toUnit.upper() == 'KELVIN':
        return (value + 459.67) * 5/9
    
    #From Kelvin
    if fromUnit.upper() == 'KELVIN' and toUnit.upper() == 'FAHRENHEIT':
        return (value * 9/5) - 459.67
    
    
    if fromUnit.upper() == 'KELVIN' and toUnit.upper() == 'CELSIUS':
        return value - 273.15
    
    
    #Distance Conversions
    
    #From Yards
    if fromUnit.upper() == 'YARDS' and toUnit.upper() == 'METERS':
        return value * 0.9144
    
    
    if fromUnit.upper() == 'YARDS' and toUnit.upper() == 'MILES':
        return value / 1760
    
    #From Meters
    if fromUnit.upper() == 'METERS' and toUnit.upper() == 'YARDS':
        return value * 1.093613
    
    if fromUnit.upper() == 'METERS' and toUnit.upper() == 'MILES':
        return value / 1609.344
    
    #From Miles
    if fromUnit.upper() == 'MILES' and toUnit.upper() == 'YARDS':
        return value * 1760
    
    
    if fromUnit.upper() == 'MILES' and toUnit.upper() == 'METERS':
        return value * 1609.344
    
    