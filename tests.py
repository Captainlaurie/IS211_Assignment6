import unittest
from conversions import convertCelsiusToKelvin
from conversions import convertCelsiusToFahrenheit
from conversions import convertFahrenheitToCelsius
from conversions import convertFahrenheitToKelvin
from conversions import convertKelvintoFahrenheit
from conversions import convertKelvintoCelsius
from conversions_refactored import convert



class ConversionsCheck(unittest.TestCase):

    #Test C to K
    def test_convertCelsiusToKelvin(self):
        value = convertCelsiusToKelvin(0)
        expected = 273.15
        self.assertAlmostEqual(value, expected, places=2)

    def test_convertCelsiusToKelvin_2(self):
        value = convertCelsiusToKelvin(200.)
        expected = 473.15
        self.assertAlmostEqual(value, expected, places=2)
        
    def test_convertCelsiusToKelvin_3(self):
        value = convertCelsiusToKelvin(300.)
        expected = 573.15
        self.assertAlmostEqual(value, expected, places=2)
    
    def test_convertCelsiusToKelvin_4(self):
        value = convertCelsiusToKelvin(400.)
        expected = 673.15
        self.assertAlmostEqual(value, expected, places=2)
    
    def test_convertCelsiusToKelvin_5(self):
        value = convertCelsiusToKelvin(500.)
        expected = 773.15
        self.assertAlmostEqual(value, expected, places=2)
        
        
    #Test C to F
    def test_convertCelsiusToFahrenheit(self):
        value = convertCelsiusToFahrenheit(0)
        expected = 32
        self.assertAlmostEqual(value, expected, places=2)

    def test_convertCelsiusToFahrenheit_2(self):
        value = convertCelsiusToFahrenheit(200.)
        expected = 392.0
        self.assertAlmostEqual(value, expected, places=2)
        
    def test_convertCelsiusToFahrenheit_3(self):
        value = convertCelsiusToFahrenheit(300.)
        expected = 572.0
        self.assertAlmostEqual(value, expected, places=2)
        
    def test_convertCelsiusToFahrenheit_4(self):
        value = convertCelsiusToFahrenheit(400.)
        expected = 752.0
        self.assertAlmostEqual(value, expected, places=2)
        
    def test_convertCelsiusToFahrenheit_5(self):
        value = convertCelsiusToFahrenheit(500.)
        expected = 392.0
        self.assertAlmostEqual(value, expected, places=2)
        
        
    #Test F to C
    def test_convertFahrenheitToCelsius(self):
         value = convertFahrenheitToCelsius(0)
         expected = -17.77
         self.assertAlmostEqual(value, expected, places=2)       
        
    def test_convertFahrenheitToCelsius_2(self):
         value = convertFahrenheitToCelsius(200.)
         expected = 93.33
         self.assertAlmostEqual(value, expected, places=2) 
         
    def test_convertFahrenheitToCelsius_3(self):
         value = convertFahrenheitToCelsius(300.)
         expected = 148.88
         self.assertAlmostEqual(value, expected, places=2) 
         
    def test_convertFahrenheitToCelsius_4(self):
         value = convertFahrenheitToCelsius(400.)
         expected = 204.44
         self.assertAlmostEqual(value, expected, places=2) 
         
    def test_convertFahrenheitToCelsius_5(self):
         value = convertFahrenheitToCelsius(500.)
         expected = 260
         self.assertAlmostEqual(value, expected, places=2) 
        
        
        
    #Test F to K
    def test_convertFahrenheitToKelvin(self):
         value = convertFahrenheitToKelvin(0)
         expected = 255.37
         self.assertAlmostEqual(value, expected, places=2) 

    def test_convertFahrenheitToKelvin_2(self):
         value = convertFahrenheitToKelvin(200)
         expected = 366.48
         self.assertAlmostEqual(value, expected, places=2)

    def test_convertFahrenheitToKelvin_3(self):
         value = convertFahrenheitToKelvin(300)
         expected = 422.03
         self.assertAlmostEqual(value, expected, places=2) 

    def test_convertFahrenheitToKelvin_4(self):
         value = convertFahrenheitToKelvin(400)
         expected = 477.59
         self.assertAlmostEqual(value, expected, places=2) 

    def test_convertFahrenheitToKelvin_5(self):
         value = convertFahrenheitToKelvin(500)
         expected = 533.15
         self.assertAlmostEqual(value, expected, places=2)              
   
        
   
    #Test K to F     
    def test_convertKelvintoFahrenheit(self):
         value = convertKelvintoFahrenheit(0)
         expected = -459.67
         self.assertAlmostEqual(value, expected, places=2) 
        
    def test_convertKelvintoFahrenheit_2(self):
         value = convertKelvintoFahrenheit(200)
         expected = -99.67
         self.assertAlmostEqual(value, expected, places=2) 
         
    def test_convertKelvintoFahrenheit_3(self):
         value = convertKelvintoFahrenheit(300)
         expected = 80.33
         self.assertAlmostEqual(value, expected, places=2) 
         
    def test_convertKelvintoFahrenheit_4(self):
         value = convertKelvintoFahrenheit(400)
         expected = 260.33
         self.assertAlmostEqual(value, expected, places=2) 
         
    def test_convertKelvintoFahrenheit_5(self):
         value = convertKelvintoFahrenheit(500)
         expected = 440.33
         self.assertAlmostEqual(value, expected, places=2) 
        
        
    #Test K to C
    def test_convertKelvintoCelsius(self):
         value = convertKelvintoCelsius(0)
         expected = -273.15
         self.assertAlmostEqual(value, expected, places=2) 
        
    def test_convertKelvintoCelsius_2(self):
         value = convertKelvintoCelsius(200)
         expected = -73.15
         self.assertAlmostEqual(value, expected, places=2) 

    def test_convertKelvintoCelsius_3(self):
         value = convertKelvintoCelsius(300)
         expected = 26.85
         self.assertAlmostEqual(value, expected, places=2) 

    def test_convertKelvintoCelsius_4(self):
         value = convertKelvintoCelsius(400)
         expected = 126.85
         self.assertAlmostEqual(value, expected, places=2) 
         
    def test_convertKelvintoCelsius_5(self):
         value = convertKelvintoCelsius(500)
         expected = 226.85
         self.assertAlmostEqual(value, expected, places=2)          
         
         
         
    # TODO: Add tests for the new functions to convert temperatures and distances
    
    #C to K
    # TODO: fill in expected values
    def test_convert_CelsiusToKelvin(self):
        value = convert("Celsius", "Kelvin", 0)
        expected = 273.15
        self.assertAlmostEqual(value, expected, places=2)
        
        
    def test_convert_CelsiusToKelvin_2(self):
        value = convert("Celsius", "Kelvin", 0)
        expected = 273.15
        self.assertAlmostEqual(value, expected, places=2)
        
    def test_convert_CelsiusToKelvin_3(self):
        value = convert("Celsius", "Kelvin", 0)
        expected = 273.15
        self.assertAlmostEqual(value, expected, places=2)

    def test_convert_CelsiusToKelvin_4(self):
        value = convert("Celsius", "Kelvin", 0)
        expected = 273.15
        self.assertAlmostEqual(value, expected, places=2)

    def test_convert_CelsiusToKelvin_5(self):
        value = convert("Celsius", "Kelvin", 0)
        expected = 273.15
        self.assertAlmostEqual(value, expected, places=2)


    #C to F
    # TODO: fill in expected values 
    def test_convert_CelsiusToFahrenheit(self):
        value = convert("Celsius", "Fahrenheit", 0)
        expected = 273.15
        self.assertAlmostEqual(value, expected, places=2)        
        
    def test_convert_CelsiusToFahrenheit_2(self):
        value = convert("Celsius", "Fahrenheit", 0)
        expected = 273.15
        self.assertAlmostEqual(value, expected, places=2)
        
    def test_convert_CelsiusToFahrenheit_3(self):
        value = convert("Celsius", "Fahrenheit", 0)
        expected = 273.15
        self.assertAlmostEqual(value, expected, places=2)
        
    def test_convert_CelsiusToFahrenheit_4(self):
        value = convert("Celsius", "Fahrenheit", 0)
        expected = 273.15
        self.assertAlmostEqual(value, expected, places=2)
        
    def test_convert_CelsiusToFahrenheit_5(self):
        value = convert("Celsius", "Fahrenheit", 0)
        expected = 273.15
        self.assertAlmostEqual(value, expected, places=2)
      
        
        

if __name__ == '__main__':
    unittest.main()