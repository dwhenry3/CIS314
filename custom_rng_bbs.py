class BlumBlumShubRNG:
    def __init__(self, seed=None):
        if seed is None:
            seed = int(str(id(self))[-6:])  # Use object ID as a fallback seed

        # Choose two large prime numbers p and q where p ≡ q ≡ 3 (mod 4)
        self.p = 499
        self.q = 547
        self.n = self.p * self.q  # Modulus for the generator

        # Ensure the seed is coprime to n
        self.state = seed % self.n
        if self.state == 0:
            self.state = 1  # Avoid zero state

    def next(self):
        """Generates the next random number."""
        self.state = (self.state ** 2) % self.n
        return self.state

    def next_bit(self):
        """Generates a random bit (0 or 1)."""
        return self.next() & 1  # Extract the least significant bit

    def next_float(self):
        """Generates a random float between 0 and 1."""
        return self.next() / self.n

    def next_range(self, min_val, max_val):
        """Generates a random number in the given range [min_val, max_val]."""
        return min_val + (self.next() % (max_val - min_val + 1))

# Example Usage:
#bbs_rng = BlumBlumShubRNG(seed=300731921167054380809804328925415665067)
bbs_rng = BlumBlumShubRNG()
#print(bbs_rng.next())        # Random integer
#print(bbs_rng.next_bit())    # Random bit (0 or 1)
#print(bbs_rng.next_float())  # Random float between 0 and 1

x = 0
while x < 10:
    print(bbs_rng.next_range(1, 65535))
    x += 1
