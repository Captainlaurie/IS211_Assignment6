def convertCelsiusToKelvin(celsius):
    """
    Convert Celsius to Kelvin
    celsius + 273.5
    :param celsius:
    :return:
    """
    return celsius + 273.15


def convertCelsiusToFahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit
    9/5 * celsius + 32
    :param celsius:
    :return:
    """
    return (celsius * 9/5) + 32 

# TODO: add 2 more functions to convert F to C and F to K

def convertFahrenheitToCelsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius
    (Fahrenheit – 32) * 5/9
    :param fahrenheit:
    :return:
    """
    return (fahrenheit - 32) * 5/9

def convertFahrenheitToKelvin(fahrenheit):
    """
    Convert Fahrenheit to Kelvin
    (fahrenheit + 459.67) * 5/9
    :param fahrenheit:
    :return:
    """
    return (fahrenheit + 459.67) * 5/9

def convertKelvintoFahrenheit(kelvin):
    """
    Convert Kelvin to Fahrenheit
    (Fahrenheit * 9/5 − 459.67)
    :param kelvin:
    :return:
    """
    return (kelvin * 9/5) - 459.67


def convertKelvintoCelsius(kelvin):
    """
    Convert Kelvin to Celsius
    Kelvin - 273.15
    :param kelvin:
    :return:
    """
    return kelvin - 273.15