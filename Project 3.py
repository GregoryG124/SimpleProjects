#Greg Grabowski
#EGR 115
#Project 3 Resistor Value Calculator
#5/5/2020


#dictionary of dictionaries to store information about resistors
resistor_dic = {
    'black' : {
        'digit' : 0,
        'multiplier' : 10**0,
        'tolerance' : 'null'
        },
    'brown' : {
        'digit' : 1,
        'multiplier' : 10**1,
        'tolerance' : .01
        },
    'red' : {
        'digit' : 2,
        'multiplier' : 10**2,
        'tolerance' : .02
        },
    'orange' : {
        'digit' : 3,
        'multiplier' : 10**3,
        'tolerance' : 'null'
        },
    'yellow' : {
        'digit' : 4,
        'multiplier' : 10**4,
        'tolerance' : 'null'
        },
    'green' : {
        'digit' : 5,
        'multiplier' : 10**5,
        'tolerance' : .005
        },
    'blue' : {
        'digit' : 6,
        'multiplier' : 10**6,
        'tolerance' : .0025
        },
    'violet' : {
        'digit' : 7,
        'multiplier' : 10**7,
        'tolerance' : .001
        },
    'grey' : {
        'digit' : 8,
        'multiplier' : 10**8,
        'tolerance' : 'null'
        },
    'white' : {
        'digit' : 9,
        'multiplier' : 10**9,
        'tolerance' : 'null'
        },
    'gold' : {
        'digit' : 'null',
        'multiplier' : 10**-1,
        'tolerance' : .05
        },
    'silver' : {
        'digit' : 'null',
        'multiplier' : 10**-2,
        'tolerance' : .1
        },
    'none' : {
        'digit' : 'null',
        'multiplier' : 'null',
        'tolerance' : .2
        },
    }

#Grab colors of four resistor bands

#band1, first digit band
band1 = str(input('Please enter the color of your first resistor band \n'))
while band1 not in resistor_dic.keys() or resistor_dic.get(band1, {}).get('digit') == 'null':
    print('Error, color is not valid for this band')
    band1 = str(input('Please enter the color of your first resistor band \n'))

#band2, second digit band
band2 = str(input('Please enter the color of your second resistor band \n'))
while band2 not in resistor_dic.keys() or resistor_dic.get(band2, {}).get('digit') == 'null':
    print('Error, color is not valid for this band')
    band2 = str(input('Please enter the color of your second resistor band \n'))

#band3, multiplier band
band3 = str(input('Please enter the color of your third resistor band \n'))
while band3 not in resistor_dic.keys() or resistor_dic.get(band3, {}).get('multiplier') == 'null':
    print('Error, color is not valid for this band')
    band3 = str(input('Please enter the color of your third resistor band \n'))

#band4, tolerance band
band4 = str(input('Please enter the color of your forth resistor band \n'))
while band4 not in resistor_dic.keys() or resistor_dic.get(band4, {}).get('tolerance') == 'null':
    print('Error, color is not valid for this band')
    band4 = str(input('Please enter the color of your forth resistor band \n'))

#calculates the resistance of the resistor
base = (resistor_dic.get(band1,{}).get('digit') * 10) + (resistor_dic.get(band2,{}).get('digit'))
multiplier = resistor_dic.get(band3,{}).get('multiplier')
resistance = base * multiplier
#calculates the tolerance of the resistor
tolerance = resistor_dic.get(band4,{}).get('tolerance') * resistance

#summery of data for user
print('the four colors you entered for resistor bands were')
print(band1, ',', band2, ',', band3, ', and', band4)
print('your total resistance was', resistance, 'ohms')
print('with a tolerance of +-', tolerance)