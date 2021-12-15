london_co = {
    "r1":{
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
        },
    "r2":{
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
        },
    "sw1":{
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
        }
}

a = input("Введите имя устройства: ")
c = london_co[a].keys()
print("Введите имя параметра: ", c, end = " ")
b = input().lower()

if a in london_co:
    if b in london_co[a]:
        print(london_co[a][b])
    else:
        print("Такого параметра нет")
else:
    print("нет")
