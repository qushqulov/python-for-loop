n = int(input("son kiriting: "))

juft = 0
toq = 0

i = 1
while i <= n:
    if i % 2 == 0:
        juft = juft + i
    else:
        toq = toq + i
    i = i + 1

print("Juft:", juft, ", Toq:", toq)

