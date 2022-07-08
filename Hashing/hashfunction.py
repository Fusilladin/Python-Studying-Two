print(hash(42))
print(hash(42.1))
print(hash(42.11))
print(hash(42.1))

class Customer:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value


alice = Customer(1000)
bob = Customer(1000)

print(alice == bob)
print(alice is bob)
print(hash(alice) == hash(bob))















#
