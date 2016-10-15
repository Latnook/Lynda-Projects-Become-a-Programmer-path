""" Overloading a Circuit Breaker """

class CircuitBreaker:

    def __init__(self, max_amps):
        self.capacity = max_amps # max capacity in amps
        self.load = 0            # present load in amps

    def connect(self, amps):
        if self.load + amps > self.capacity:
            raise Exception('Connection will exceed capacity')
        elif self.load + amps < 0:
            raise Exception('Connection will cause negative load')
        else:
            self.load += amps

# create a 20A circuit breaker
cb = CircuitBreaker(20)
