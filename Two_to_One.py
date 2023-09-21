#Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible,
#  containing distinct letters - each taken only once - coming from s1 or s2.


def longest(a1, a2):
    a3 = a1 + a2
    print(''.join(list((sorted(set(a3))))))

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

print(longest(a,b))

