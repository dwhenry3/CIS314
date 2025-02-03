class CustomRNG:
    def __init__(self, seed=None):
        if seed is None:
            seed = int(str(id(self))[-6:])  # Use object ID as a fallback seed
        self.state = seed

        # LCG constants (example values from Numerical Recipes)
        self.a = 1664525
        self.c = 1013904223
        self.m = 2**32

    def next(self):
        """Generates the next random number."""
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def next_float(self):
        """Generates a random float between 0 and 1."""
        return self.next() / self.m

    def next_range(self, min_val, max_val):
        """Generates a random number in the given range [min_val, max_val]."""
        return min_val + (self.next() % (max_val - min_val + 1))

# Example Usage:
rng = CustomRNG(seed=300731921167054380809804328925415665067)  # You can set a custom seed or let it generate one
#print(rng.next())        # Random integer
#print(rng.next_float())  # Random float between 0 and 1

x = 0
while x < 10:
    print(rng.next_range(1, 65535))
    x += 1