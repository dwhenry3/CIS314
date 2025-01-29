x = 1
while x <= 10:
    print(x)
    x += 1
print("#--------------------")
da_list = ["a", "b", "c", "d", "e"]
index = 0

while index < len(da_list):
    print(da_list[index])
    index += 1
print("#--------------------")
x = 1
while x <= 10:
    if x == 5:
        break
    print(x)
    x += 1
print("#--------------------")
x = 0
while x < 10:        
    x += 1
    if x == 5:
        continue
    print(x)
print("#--------------------")
x = 0
while x <= 10:
    print(x)
    x += 1
else:
    print("x is now",x)
print("#--------------------")
da_list = ["a", "b", "c", "d", "e"]
for item in da_list:
    print(item)
print("#--------------------")
for item in range(1,11):
    print(item)
print("#--------------------")
da_list = ["a", "b", "c", "d", "e"]
for item in da_list:
    if item == "c":
        break
    print(item)
print("#--------------------")
da_list = ["a", "b", "c", "d", "e"]
for item in da_list:
    if item == "c":
        continue
    print(item)
print("#--------------------")
da_list = ["a", "b", "c", "d", "e"]
for item in da_list:
    print(item)
else:
    print("Job's done")