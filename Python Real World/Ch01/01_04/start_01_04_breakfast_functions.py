""" A Functional Breakfast """

cheese = 'cheddar'

def mix_and_cook():
    print('Mixing the ingredients')
    print('Greasing the frying pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side')

def make_omlette():
    cheese = 'swiss'
    #This function takes the cheese from the local scope.
    #If I would want the function to use the global scope cheese, I would add the line "global cheese"
    mix_and_cook()
    omlette = 'a {} omlette'.format(cheese)
    return omlette

def make_pancake():
    mix_and_cook()
    #This function can't find cheese in the local scope so it takes it from the global scope
    pancake = 'a {} pancake'.format(cheese)
    return pancake

def fancy_omlette(*ingredients):
    mix_and_cook()
    omlette = 'a fancy omlette with {} ingredients'.format(len(ingredients))
    return omlette
