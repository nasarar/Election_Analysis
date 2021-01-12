#what is the score?
score = int(input("what is your test score?"))

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

#counties membership operators
counties = ['Arapahoe', 'Denver', 'Jefferson']
if 'El Paso' in counties:
    print('El Paso is in the counties')
else:
    print('El Paso is not in the counties')