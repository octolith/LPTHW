fn1 = 1084900
fn2 = 773
fn3 = 7276

f1 = -fn1 -fn3
f2 = -fn1 -fn2
f3 = -fn1
f4 = -fn1 +fn2
f5 = -fn1 +fn3
f6 = fn1 -fn3
f7 = fn1 -fn2
f8 = fn1
f9 = fn1 +fn2
f10 = fn1 +fn3

A0 = 10
A1 = 1
A2 = 1.67
A3 = 0.28

m = ((A2 + A3)/10)*100

A = (4 * ((A2 / 4) ** 2) + 4 * ((A3 / 4) ** 2)) / (2*((A0 / 2) ** 2)) * 100

B1 = A3 / 4
B2 = A2 / 4
B3 = A0 / 2
B4 = A2 / 4
B5 = A3 / 4
B6 = A3 / 4
B7 = A2 / 4
B8 = A0 / 2
B9 = A2 / 4
B10 = A3 / 4

print(f"fn1 = {fn1}")
print(f"fn2 = {fn2}")
print(f"fn3 = {fn3}")
print(f"")
print(f"f1 = -fn1 -fn3 = {f1}")
print(f"f2 = -fn1 -fn2 = {f2}")
print(f"f3 = -fn1 = {f3}")
print(f"f4 = -fn1 +fn2 = {f4}")
print(f"f5 = -fn1 +fn3 = {f5}")
print(f"f6 = fn1 -fn3 = {f6}")
print(f"f7 = fn1 -fn2 = {f7}")
print(f"f8 = fn1 = {f8}")
print(f"f9 = fn1 +fn2 = {f9}")
print(f"f10 = fn1 +fn3 = {f10}")
print(f"")
print(f"A0 = {A0}")
print(f"A1 = {A1}")
print(f"A2 = {A2}")
print(f"A3 = {A3}")
print(f"")
print(f"m = {m}%")
print(f"")
print(f"A = {A}%")
print(f"")
print(f"B1 = A3 / 4 = {B1}")
print(f"B2 = A2 / 4 = {B2}")
print(f"B3 = A0 / 2 = {B3}")
print(f"B4 = A2 / 4 = {B4}")
print(f"B5 = A3 / 4 = {B5}")
print(f"B6 = A3 / 4 = {B6}")
print(f"B7 = A2 / 4 = {B7}")
print(f"B8 = A0 / 2 = {B8}")
print(f"B9 = A2 / 4 = {B9}")
print(f"B10 = A3 / 4 = {B10}")
