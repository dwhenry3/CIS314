import secrets
import timeit
import time

start = time.time()
bits = secrets.randbits(16)
end = time.time()
delta = end - start
print("Randbits: ", str(bits), " took %.9f seconds" % delta)

start = timeit.default_timer()
bits = secrets.randbits(16)
end = timeit.default_timer()
delta = end - start
print("Randbits: ", str(bits), " took %.9f seconds" % delta)

start = time.time()
choice = secrets.choice(range(1,65535))
end = time.time()
delta = end - start
print("Choice: ", str(choice), " took %.9f seconds" % delta)

start = timeit.default_timer()
choice = secrets.choice(range(1,65535))
end = timeit.default_timer()
delta = end - start
print("Choice: ", str(choice), " took %.9f seconds" % delta)

start = time.time()
below = secrets.randbelow(65535) + 1
end = time.time()
delta = end - start
print("Randbelow: ", str(below), " took %.9f seconds" % delta)

start = timeit.default_timer()
below = secrets.randbelow(65535) + 1
end = timeit.default_timer()
delta = end - start
print("Randbelow: ", str(below), " took %.9f seconds" % delta)