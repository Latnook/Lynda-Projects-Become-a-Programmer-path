""" A Functional Breakfast """

def mix_and_cook():
    print('Mixing the ingredients')
    print('Greasing the frying pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side')

def make_omlette(ingredient):
    mix_and_cook()
    omlette = 'a {} omlette'.format(ingredient)
    return omlette

def make_pancake():
    mix_and_cook()
    pancake = 'a delicious pancake'
    return pancake

def fancy_omlette(*ingredients):
    mix_and_cook()
    omlette = 'a fancy omlette with {} ingredients'.format(len(ingredients))
    return omlette
