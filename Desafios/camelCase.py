s = input()

counter = 1

for i in range(len(s)):
    if ord(s[i]) >= 65 and ord(s[i]) <= 90:
        counter += 1

print(counter)