## String Manipulation

# Alternating Characters
s1 = "BAAABBAABABA"
s2 = ""
counter = 0

for i in range(len(s1)):
  if i == 0:
    prev = s1[i]
    s2 += prev
  else:
    curr = s1[i]
    if curr == prev:
      counter += 1
    else:
      s2 += curr
      prev = curr

print("My original string was", s1)
print("My manipulated string is", s2)
print("The manipulation required", counter, "deletions")

#####################################
# Compare Strings
s1 = 'abcde'
s2 = 'abcce'
smaller = -1
i = 0

if len(s1) > len(s2):
  for i in range(len(s2)):
    if s1[i] != s2[i]:
      if s1[i] < s2[i]:
        smaller = s1
      else:
        smaller = s2
elif len(s1) < len(s2):
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      if s1[i] < s2[i]:
        smaller = s1
      else:
        smaller = s2
elif len(s1) == len(s2):
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      if s1[i] < s2[i]:
        smaller = s1
      else:
        smaller = s2

print('smaller string is', smaller)

#####################################
# Merge Strings
s1 = 'aaaaaaa'
s2 = 'bbbbcccdddd'
out = ''
i = 0

while i < len(s1) and i < len(s2):
  out += s1[i] + s2[i]
  i += 1
while i < len(s1):
  out += s1[i]
  i += 1
while i < len(s2):
  out += s2[i]
  i += 1

print(out)

#####################################
# Bisection Search for Root-finding
eps = 1e-5
max_iter = 10000

# define the search region as an interval in which the function changes sign
a = 1
b = 2
f_a = a ** 3 - a - 2
f_b = b ** 3 - b - 2

print('This needs to be negative f_a =', f_a)
print('This needs to be positive f_b =', f_b)

i = 0
while i < max_iter:
  c = (a+b)/2
  f_c = c ** 3 - c - 2
  if abs(f_c) < eps or c - a < eps:
    print("solution is found at c =", c)
    print("after i =", i)
    break
  i += 1
  if f_c < 0:
    a = c
  else:
    b = c
if i == max_iter:
  print('Solution is not found.')
