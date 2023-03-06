def convertCelsiusToKelvin(celsius):
    """
    Convert Celsius to Kelvin
    celsius + 273.5
    :param celsius:
    :return:
    """
    kelvin = celsius + 273.15
    return kelvin



def convertCelsiusToFahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit
    9/5 * celsius + 32
    :param celsius:
    :return:
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit



def convertFahrenheitToCelsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius
    (Fahrenheit – 32) * 5/9
    :param fahrenheit:
    :return:
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius



def convertFahrenheitToKelvin(fahrenheit):
    """
    Convert Fahrenheit to Kelvin
    (fahrenheit + 459.67) * 5/9
    :param fahrenheit:
    :return:
    """
    kelvin = (fahrenheit + 459.67) * 5/9
    return kelvin



def convertKelvintoFahrenheit(kelvin):
    """
    Convert Kelvin to Fahrenheit
    (Fahrenheit * 9/5 − 459.67)
    :param kelvin:
    :return:
    """
    fahrenheit = (kelvin * 9/5) - 459.67
    return fahrenheit



def convertKelvintoCelsius(kelvin):
    """
    Convert Kelvin to Celsius
    Kelvin - 273.15
    :param kelvin:
    :return:
    """
    celsius = kelvin - 273.15
    return celsius
    