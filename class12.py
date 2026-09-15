#DEBUGGING TECHNIQUES:
#midterm - till modules and packages in unit 2 , only 3 things iterators, decorators and generators 
"""
smart traffic light stimulator
imagine you r developing a smart traffic managment system for a busy city, the system stimulates traffic signals at different road 
intersections and change their colour simultaneously. for 2 intersection ns represents north south traffic direction and ew represents 
east west traffic direction each direction can have a light that is red yellow or green. 
for example if it a market_street = { ns="green", ew ="red"}
it should be like switching_light function 
correctness should be changed using assertion command
ns is green ew is red (program should automitacilly change the light colour - if it is green change to yellow and then red and vice versa)
"""


   
market_street = {'ns': 'green', 'ew': 'red'}

def switch_lights(stoplight):

    for key in stoplight:
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'

        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'

        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

    # Correctness check
    assert 'red' in stoplight.values(), \
        "Neither light is red! " + str(stoplight)


switch_lights(market_street)

print("Traffic signals:", market_street)