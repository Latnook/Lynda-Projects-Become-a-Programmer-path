""" The Blueprints for Jeans """

class jeans:

    def __init__(self, waist, length, color):
        #arguements for waist, length, and color which get sent to __init__
        #set atributes to appropriate value
        self.waist = waist
        self.length = length
        self.color = color
        #Is the pair of jeans being worn?
        self.wearing = False

    def put_on(self):
        print('Putting on {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = True


    def take_off(self):
        print('Taking off {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = False
