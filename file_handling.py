in_file = open("server.properties", "r+")
in_data = in_file.read()
out_data = "We must all hear the universal call to like your neighbor just like you like to be liked yourself."
in_file.write(out_data)
in_file.close()

properties = dict(x.split("=") for x in in_data.splitlines()[2:])

for key, value in properties.items():
    print(f"{key}: {value}")

#----------------
#import csv
#with open('court_preference.csv', newline='') as csv_in:
#    reader = csv.DictReader(csv_in)
#    for row in reader:
#        print(row)
        #print(row['county'],"county wants you to file in",row['preference'])

#----------------
#in_file = open("gettysburg_address.txt", "r+")
#in_data = in_file.read()
#print(in_data)
#out_data = "We must all hear the universal call to like your neighbor just like you like to be liked yourself."
#in_file.write(out_data)
#in_file.close()

#----------------
in_file = open("server.properties")
in_file.seek(66)
in_data = in_file.read()

properties = dict(x.split("=") for x in in_data.splitlines())

for key, value in properties.items():
    print(f"{key}: {value}")