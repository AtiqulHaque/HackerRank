spc = ''
sp="Www.HackerRank.com"

for i in range(len(sp)):
    if ord(sp[i]) >= 65 and ord(sp[i]) <= 90:
        spc += chr(ord(sp[i]) + 32)
    elif ord(sp[i]) >= 97 and ord(sp[i]) <= 122:
        spc += chr(ord(sp[i]) - 32)
    else:
        spc+=sp[i]

print(spc)
