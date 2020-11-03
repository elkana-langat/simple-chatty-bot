a = int(input())
b = int(input())
h = int(input())

if h > b:
    print("Excess")
else:
    if h < a:
        print("Deficiency")
    else:
        print("Normal")
