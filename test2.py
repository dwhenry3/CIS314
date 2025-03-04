class Attorney:
    def __init__(self, name):
        self.name = name

lawyers = []
lawyers.append(Attorney("Dane"))
lawyers.append(Attorney("Amanda"))
lawyers.append(Attorney("Erik"))

while True:
    try:
        new_attorney = input("What is the attorney's name?")
        lawyers.append(Attorney(new_attorney))
        break
    except:
        print("Do Better")

print(lawyers[len(lawyers)-1].name)