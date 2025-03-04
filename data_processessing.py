in_data = [1,3,4,5,3,5,6,4,5]

for count, x in enumerate(in_data):
    if x == 3:
        in_data.pop(count)