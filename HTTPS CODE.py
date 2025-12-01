https={"403":"Forbidden","404":"Not found","301":"Moved Permanently","304":"Not Modified","307":"Temporary redirect"}
A=input("Https code: ")
if A in https:
    print(https[A])
else:
    print("Incorrect nummber")