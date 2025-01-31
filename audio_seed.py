import random
import hashlib
from pydub import AudioSegment

audio_data = AudioSegment.from_file("output.wav", format="wav")
samples = audio_data.get_array_of_samples()

# Hash the audio data using SHA-256
hash_object = hashlib.sha256()
for x in samples:
    hash_object.update(repr(x).encode())
seed = int(hash_object.hexdigest()[:32], 16)  # extract 32-bit seed

# Set the seed for the PRNG
random.seed(seed)

# Generate random numbers using the seeded PRNG
x = 0
while x < 100:
  random_number = random.randint(0,10000)
  print(random_number)
  x+=1