total = 0

narx1 = int(input("son kiriting: "))
narx2 = int(input("son kiriting: "))
narx3 = int(input("son kiriting: "))
narx4 = int(input("son kiriting: "))
narx5 = int(input("son kiriting: "))

if narx1 % 5 == 0:
    total = total + narx1
if narx2 % 5 == 0:
    total = total + narx2
if narx3 % 5 == 0:
    total = total + narx3
if narx4 % 5 == 0:
    total = total + narx4
if narx5 % 5 == 0:
    total = total + narx5

print(total)
