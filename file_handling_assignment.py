import re

out_data = []
in_file = open("access.log")
in_data = in_file.readlines()

for x in in_data:
    if x.find("BotPoke") < 0:
        out_data.append(x)

print("The log has",len(out_data),"entries after filtering BotPoke")

ip_finder = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
ip_address_set = set()
for x in out_data:
    result = re.match(ip_finder, x)
    if result:
        ip_address_set.add(result[0])

print("The IP Addresses remaining are:", ip_address_set)