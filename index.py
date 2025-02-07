#                    int   float   complex  boolean     list       tuple     string     range
   
    #  int          yes     yes     yes     yes         No      false       true        true

    # float         true    true    yes     yes         false   false       true        false

    # complex       false   false   yes     yes         false   false       true        false

    # boolean       true    true    true    true        false   false       true        true

    # list          false   false   false   true        true    true        true        false  

    # tuple         false   false   false   true        true    true        true        false

    # string        false   false   false   true        true    true        true        false

    # range         false   false   false   true        true    true        true        false


cmp = 3 + 5j
# print(int(cmp))
# print(float(cmp))
print(bool(cmp))
print(complex(cmp))
# print(list(cmp))
# print(tuple(cmp))
print(str(cmp))
# print(range(cmp))

bool1 = 1
print(bool1)
print(int(bool1))
print(float(bool1))
print(bool(bool1))
print(str(bool1))
# print(list(bool1))
# print(tuple(bool1))
print(range(bool1))
print(complex(bool1))

list11 = [1,2,3,'sandhya', True, [6,7]]
# print(int(list11))
# print(float(list11))
# print(complex(list11))
print(bool(list11))
print(list(list11))
print(tuple(list11))
print(str(list11))
# print(range(list11))

tup = (1,2,3, True, 'str1', 0.9)
# print(int(tup))
# print(float(tup))
# print(complex(tup))
print(bool(tup))
print(list(tup))
print(tuple(tup))
print(str(tup))
# print(range(tup))

str1 = "sandhya"
# print(int(str1))
# print(float(str1))
# print(complex(str1))
print(bool(str1))
print(list(str1))
print(tuple(str1))
print(str(str1))
# print(range(str1))

# print(int(range(0,100)))
# print(float(range(0,100)))
print(bool(range(0,100)))
# print(complex(range(0,100)))
print(list(range(0,100)))
print(tuple(range(0,100)))
print(str(range(0,100)))
# print(range(range(0,100)))





