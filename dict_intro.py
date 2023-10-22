vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford fiesta Ghia 1.4'
}

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"
# my_car = vehicles['fiesta']
# print(my_car)

# learner = vehicles.get('er5')
# print(learner)

# for key in vehicles:
#    print(key, vehicles[key], sep=": ")

#updating a dictionary
vehicles['virago'] = "Yamaha XV535"

del vehicles['toy']
#del vehicles['F1']
#result = vehicles.pop('F1', None)
#print(result)
#print()

#result = vehicles.pop('F1', 'You wish!, Sell the Learjet and you might afford a racing car.')
#print(result)
#plane = vehicles.pop('learjet')
#print(plane)
#bike = vehicles.pop('tenere', 'Not Present')
#print(bike)
#print()

for key, value in vehicles.items():
    print(key, value, sep=", ")
