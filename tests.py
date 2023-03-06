import unittest
from conversions import convertCelsiusToKelvin
from conversions import convertCelsiusToFahrenheit
from conversions import convertFahrenheitToCelsius
from conversions import convertFahrenheitToKelvin
from conversions import convertKelvintoFahrenheit
from conversions import convertKelvintoCelsius
from conversions_refactored import convert
from conversions_refactored import ConversionNotPossible



class ConversionsCheck(unittest.TestCase):

    
    #Tests that intentionally fail
    def test_convertCelsiusToKelvin_0(self):
        value = convertCelsiusToKelvin(10)
        expected = 57
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convertCelsiusToKelvin_00(self):
        value = convertCelsiusToKelvin(20)
        expected = 400
        self.assertAlmostEqual(value, expected, delta=0.01)

    #Test C to K
    def test_convertCelsiusToKelvin(self):
        value = convertCelsiusToKelvin(0)
        expected = 273.15
        self.assertAlmostEqual(value, expected, delta=0.01)

    def test_convertCelsiusToKelvin_2(self):
        value = convertCelsiusToKelvin(200.)
        expected = 473.15
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convertCelsiusToKelvin_3(self):
        value = convertCelsiusToKelvin(300.)
        expected = 573.15
        self.assertAlmostEqual(value, expected, delta=0.01)
    
    def test_convertCelsiusToKelvin_4(self):
        value = convertCelsiusToKelvin(400.)
        expected = 673.15
        self.assertAlmostEqual(value, expected, delta=0.01)
    
    def test_convertCelsiusToKelvin_5(self):
        value = convertCelsiusToKelvin(500.)
        expected = 773.15
        self.assertAlmostEqual(value, expected, delta=0.01)
        
        
    #Test C to F
    def test_convertCelsiusToFahrenheit(self):
        value = convertCelsiusToFahrenheit(0)
        expected = 32
        self.assertAlmostEqual(value, expected, delta=0.01)

    def test_convertCelsiusToFahrenheit_2(self):
        value = convertCelsiusToFahrenheit(200.)
        expected = 392
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convertCelsiusToFahrenheit_3(self):
        value = convertCelsiusToFahrenheit(300.)
        expected = 572
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convertCelsiusToFahrenheit_4(self):
        value = convertCelsiusToFahrenheit(400.)
        expected = 752
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convertCelsiusToFahrenheit_5(self):
        value = convertCelsiusToFahrenheit(500.)
        expected = 932
        self.assertAlmostEqual(value, expected, delta=0.01)
        
        
    #Test F to C
    def test_convertFahrenheitToCelsius(self):
         value = convertFahrenheitToCelsius(0)
         expected = -17.77
         self.assertAlmostEqual(value, expected, delta=0.01)       
        
    def test_convertFahrenheitToCelsius_2(self):
         value = convertFahrenheitToCelsius(200.)
         expected = 93.33
         self.assertAlmostEqual(value, expected, delta=0.01) 
         
    def test_convertFahrenheitToCelsius_3(self):
         value = convertFahrenheitToCelsius(300.)
         expected = 148.88
         self.assertAlmostEqual(value, expected, delta=0.01) 
         
    def test_convertFahrenheitToCelsius_4(self):
         value = convertFahrenheitToCelsius(400.)
         expected = 204.44
         self.assertAlmostEqual(value, expected, delta=0.01) 
         
    def test_convertFahrenheitToCelsius_5(self):
         value = convertFahrenheitToCelsius(500.)
         expected = 260
         self.assertAlmostEqual(value, expected, delta=0.01) 
        
        
        
    #Test F to K
    def test_convertFahrenheitToKelvin(self):
         value = convertFahrenheitToKelvin(0)
         expected = 255.37
         self.assertAlmostEqual(value, expected, delta=0.01) 

    def test_convertFahrenheitToKelvin_2(self):
         value = convertFahrenheitToKelvin(200)
         expected = 366.48
         self.assertAlmostEqual(value, expected, delta=0.01)

    def test_convertFahrenheitToKelvin_3(self):
         value = convertFahrenheitToKelvin(300)
         expected = 422.03
         self.assertAlmostEqual(value, expected, delta=0.01) 

    def test_convertFahrenheitToKelvin_4(self):
         value = convertFahrenheitToKelvin(400)
         expected = 477.59
         self.assertAlmostEqual(value, expected, delta=0.01) 

    def test_convertFahrenheitToKelvin_5(self):
         value = convertFahrenheitToKelvin(500)
         expected = 533.15
         self.assertAlmostEqual(value, expected, delta=0.01)              
   
        
   
    #Test K to F     
    def test_convertKelvintoFahrenheit(self):
         value = convertKelvintoFahrenheit(0)
         expected = -459.67
         self.assertAlmostEqual(value, expected, delta=0.01) 
        
    def test_convertKelvintoFahrenheit_2(self):
         value = convertKelvintoFahrenheit(200)
         expected = -99.67
         self.assertAlmostEqual(value, expected, delta=0.01) 
         
    def test_convertKelvintoFahrenheit_3(self):
         value = convertKelvintoFahrenheit(300)
         expected = 80.33
         self.assertAlmostEqual(value, expected, delta=0.01) 
         
    def test_convertKelvintoFahrenheit_4(self):
         value = convertKelvintoFahrenheit(400)
         expected = 260.33
         self.assertAlmostEqual(value, expected, delta=0.01) 
         
    def test_convertKelvintoFahrenheit_5(self):
         value = convertKelvintoFahrenheit(500)
         expected = 440.33
         self.assertAlmostEqual(value, expected, delta=0.01) 
        
        
    #Test K to C
    def test_convertKelvintoCelsius(self):
         value = convertKelvintoCelsius(0)
         expected = -273.15
         self.assertAlmostEqual(value, expected, delta=0.01) 
        
    def test_convertKelvintoCelsius_2(self):
         value = convertKelvintoCelsius(200)
         expected = -73.15
         self.assertAlmostEqual(value, expected, delta=0.01) 

    def test_convertKelvintoCelsius_3(self):
         value = convertKelvintoCelsius(300)
         expected = 26.85
         self.assertAlmostEqual(value, expected, delta=0.01) 

    def test_convertKelvintoCelsius_4(self):
         value = convertKelvintoCelsius(400)
         expected = 126.85
         self.assertAlmostEqual(value, expected, delta=0.01) 
         
    def test_convertKelvintoCelsius_5(self):
         value = convertKelvintoCelsius(500)
         expected = 226.85
         self.assertAlmostEqual(value, expected, delta=0.01)          
         

    #C to K
    def test_convert_CelsiusToKelvin(self):
        value = convert("Celsius", "Kelvin", 0)
        expected = 273.15
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_CelsiusToKelvin_2(self):
        value = convert("Celsius", "Kelvin", 200)
        expected = 473.15
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_CelsiusToKelvin_3(self):
        value = convert("Celsius", "Kelvin", 300)
        expected = 573.15
        self.assertAlmostEqual(value, expected, delta=0.01)

    def test_convert_CelsiusToKelvin_4(self):
        value = convert("Celsius", "Kelvin", 400)
        expected = 673.15
        self.assertAlmostEqual(value, expected, delta=0.01)

    def test_convert_CelsiusToKelvin_5(self):
        value = convert("Celsius", "Kelvin", 500)
        expected = 773.15
        self.assertAlmostEqual(value, expected, delta=0.01)


    #C to F 
    def test_convert_CelsiusToFahrenheit(self):
        value = convert("Celsius", "Fahrenheit", 0)
        expected = 32
        self.assertAlmostEqual(value, expected, delta=0.01)        
        
    def test_convert_CelsiusToFahrenheit_2(self):
        value = convert("Celsius", "Fahrenheit", 200)
        expected = 392
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_CelsiusToFahrenheit_3(self):
        value = convert("Celsius", "Fahrenheit", 300)
        expected = 572
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_CelsiusToFahrenheit_4(self):
        value = convert("Celsius", "Fahrenheit", 400)
        expected = 752
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_CelsiusToFahrenheit_5(self):
        value = convert("Celsius", "Fahrenheit", 500)
        expected = 932
        self.assertAlmostEqual(value, expected, delta=0.01)


    #Test F to C
    def test_convert_FahrenheitToCelsius(self):
        value = convert("Fahrenheit", "Celsius", 0)
        expected = -17.77
        self.assertAlmostEqual(value, expected, delta=0.01)               
        
    def test_convert_FahrenheitToCelsius_2(self):
        value = convert("Fahrenheit", "Celsius", 200)
        expected = 93.33
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_FahrenheitToCelsius_3(self):
        value = convert("Fahrenheit", "Celsius", 300)
        expected = 148.88
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_FahrenheitToCelsius_4(self):
        value = convert("Fahrenheit", "Celsius", 400)
        expected = 204.44
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_FahrenheitToCelsius_5(self):
        value = convert("Fahrenheit", "Celsius", 500)
        expected = 260
        self.assertAlmostEqual(value, expected, delta=0.01)
        
        
    #Test F to K
    def test_convert_FahrenheitToKelvin(self):
        value = convert("Fahrenheit", "Kelvin", 0)
        expected = 255.37
        self.assertAlmostEqual(value, expected, delta=0.01)      
        
    def test_convert_FahrenheitToKelvin_2(self):
        value = convert("Fahrenheit", "Kelvin", 200)
        expected = 366.48
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_FahrenheitToKelvin_3(self):
        value = convert("Fahrenheit", "Kelvin", 300)
        expected = 422.03
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_FahrenheitToKelvin_4(self):
        value = convert("Fahrenheit", "Kelvin", 400)
        expected = 477.59
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_FahrenheitToKelvin_5(self):
        value = convert("Fahrenheit", "Kelvin", 500)
        expected = 533.15
        self.assertAlmostEqual(value, expected, delta=0.01)
        
      
    #Test K to F     
    def test_convert_KelvintoFahrenheit(self):
        value = convert("Kelvin", "Fahrenheit", 0)
        expected = -459.67
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_KelvintoFahrenheit_2(self):
        value = convert("Kelvin", "Fahrenheit", 200)
        expected = -99.67
        self.assertAlmostEqual(value, expected, delta=0.01) 
        
    def test_convert_KelvintoFahrenheit_3(self):
        value = convert("Kelvin", "Fahrenheit", 300)
        expected = 80.33
        self.assertAlmostEqual(value, expected, delta=0.01) 
        
    def test_convert_KelvintoFahrenheit_4(self):
        value = convert("Kelvin", "Fahrenheit", 400)
        expected = 260.33
        self.assertAlmostEqual(value, expected, delta=0.01) 
        
    def test_convert_KelvintoFahrenheit_5(self):
        value = convert("Kelvin", "Fahrenheit", 500)
        expected = 440.33
        self.assertAlmostEqual(value, expected, delta=0.01) 
        
        
    #Test K to C
    def test_convert_KelvintoCelsius(self):
        value = convert("Kelvin", "Celsius", 0)
        expected = -273.15
        self.assertAlmostEqual(value, expected, delta=0.01) 
        
    def test_convert_KelvintoCelsius_2(self):
        value = convert("Kelvin", "Celsius", 200)
        expected = -73.15
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_KelvintoCelsius_3(self):
        value = convert("Kelvin", "Celsius", 300)
        expected = 26.85
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_KelvintoCelsius_4(self):
        value = convert("Kelvin", "Celsius", 400)
        expected = 126.85
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_KelvintoCelsius_5(self):
        value = convert("Kelvin", "Celsius", 500)
        expected = 226.85
        self.assertAlmostEqual(value, expected, delta=0.01)
        
        
    
    #Test Yards to Meters
    def test_convert_YardsToMeters(self):
        value = convert("Yards", "Meters", 1)
        expected = 0.9144
        self.assertAlmostEqual(value, expected, delta=0.01) 
        
    def test_convert_YardsToMeters_2(self):
        value = convert("Yards", "Meters", 50)
        expected = 45.72
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_YardsToMeters_3(self):
        value = convert("Yards", "Meters", 100)
        expected = 91.44
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_YardsToMeters_4(self):
        value = convert("Yards", "Meters", 500)
        expected = 457.2
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_YardsToMeters_5(self):
        value = convert("Yards", "Meters", 1000)
        expected = 914.4
        self.assertAlmostEqual(value, expected, delta=0.01)
        
        
        
    #Test Yards to Miles    
    def test_convert_YardsToMiles(self):
        value = convert("Yards", "Miles", 50)
        expected = 0.0284091
        self.assertAlmostEqual(value, expected, delta=0.01)       
        
    def test_convert_YardsToMiles_2(self):
        value = convert("Yards", "Miles", 100)
        expected = 0.0568182
        self.assertAlmostEqual(value, expected, delta=0.01) 
        
    def test_convert_YardsToMiles_3(self):
        value = convert("Yards", "Miles", 200)
        expected = 0.113636
        self.assertAlmostEqual(value, expected, delta=0.01) 
        
    def test_convert_YardsToMiles_4(self):
        value = convert("Yards", "Miles", 500)
        expected = 0.284091
        self.assertAlmostEqual(value, expected, delta=0.01) 
        
    def test_convert_YardsToMiles_5(self):
        value = convert("Yards", "Miles", 1000)
        expected = 0.568182
        self.assertAlmostEqual(value, expected, delta=0.01) 
        
        
    #Test Meters to Yards
    def test_convert_MetersToYards(self):
        value = convert("Meters", "Yards", 1)
        expected = 1.09361
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_MetersToYards_2(self):
        value = convert("Meters", "Yards", 100)
        expected = 109.361
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_MetersToYards_3(self):
        value = convert("Meters", "Yards", 200)
        expected = 218.723
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_MetersToYards_4(self):
        value = convert("Meters", "Yards", 500)
        expected = 546.807
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_MetersToYards_5(self):
        value = convert("Meters", "Yards", 1000)
        expected = 1093.61
        self.assertAlmostEqual(value, expected, delta=0.01)
        
        
        
    #Test Meters to Miles
    def test_convert_MetersToMiles(self):
        value = convert("Meters", "Miles", 50)
        expected = 0.0310686
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_MetersToMiles_2(self):
        value = convert("Meters", "Miles", 100)
        expected = 0.0621371
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_MetersToMiles_3(self):
        value = convert("Meters", "Miles", 200)
        expected = 0.124274
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_MetersToMiles_4(self):
        value = convert("Meters", "Miles", 500)
        expected = 0.310686
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_MetersToMiles_5(self):
        value = convert("Meters", "Miles", 1000)
        expected = 0.621371
        self.assertAlmostEqual(value, expected, delta=0.01)
        
        
    #Test Miles to Yards
    def test_convert_MilesToYards(self):
        value = convert("Miles", "Yards", 1)
        expected = 1760
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_MilesToYards_2(self):
        value = convert("Miles", "Yards", 50)
        expected = 88000
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_MilesToYards_3(self):
        value = convert("Miles", "Yards", 200)
        expected = 352000
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_MilesToYards_4(self):
        value = convert("Miles", "Yards", 500)
        expected = 880000
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_MilesToYards_5(self):
        value = convert("Miles", "Yards", 1000)
        expected = 1760000
        self.assertAlmostEqual(value, expected, delta=0.01)
        
        
        
    #Test Miles to Meters   
    def test_convert_MilesToMeters(self):
        value = convert("Miles", "Meters", 1)
        expected = 1609.34
        self.assertAlmostEqual(value, expected, delta=0.01)
        
    def test_convert_MilesToMeters_2(self):
        value = convert("Miles", "Meters", 50)
        expected = 80467.2
        self.assertAlmostEqual(value, expected, delta=0.01) 
        
    def test_convert_MilesToMeters_3(self):
        value = convert("Miles", "Meters", 100)
        expected = 160934.4
        self.assertAlmostEqual(value, expected, delta=0.01) 
        
    def test_convert_MilesToMeters_4(self):
        value = convert("Miles", "Meters", 500)
        expected = 804672
        self.assertAlmostEqual(value, expected, delta=0.01) 
        
    def test_convert_MilesToMeters_5(self):
        value = convert("Miles", "Meters", 1000)
        expected = 1609344
        self.assertAlmostEqual(value, expected, delta=0.01) 
        
        
    #Test incompatible units
    def test_conversion_not_possible(self):
        with self.assertRaises(ConversionNotPossible):
            convert('FAHRENHEIT', 'METERS', 10)
    
    

if __name__ == '__main__':
    unittest.main()