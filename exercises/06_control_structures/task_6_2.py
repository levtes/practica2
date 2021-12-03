# -*- coding: utf-8 -*-
"""
Задание 6.2
"""
a = input().split(".")
if 1 <= int(a[0]) <= 223:
    print("unicast")
elif 224 <= int(a[0]) <= 239:
    print("multicast")
elif a[0] == "255" and a[1] == "255" and a[2] == "255" and a[3] == "255":
    print("local broadcast")
elif a[0] == "0" and a[1] == "0" and a[2] == "0" and a[3] == "0":
    print("unassigned")
else:
    print("unused")
