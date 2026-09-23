innings = 6.2
print(innings)

remainder = innings % 1
partial = round(remainder * 10)
print(partial)

print(int(6.1 // 1))
print(int(7.2 // 1))

innings_pitched = 5.0   # just a plain variable instead of self.innings_pitched

remainder = innings_pitched % 1
whole_innings = int(innings_pitched // 1)
partial = round(remainder * 10)

if partial == 0:
    fractional_inning = 0.0
elif partial == 1:
    fractional_inning = 1 / 3
elif partial == 2:
    fractional_inning = 2 / 3

print(whole_innings + fractional_inning)