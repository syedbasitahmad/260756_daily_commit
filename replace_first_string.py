
def replace_repeated(c):
    hash = dict()
    c= list(c)
    for i in range(len(c)):
        if c[i] not in hash.keys():
            hash[c[i]] = 1
        else:
            c[i] = "$"
    return "".join(c)

a = input("Enter string")
print(replace_repeated(a))

# Unit Testing

def test_method():
    assert replace_repeated("aabbccddee") == "a$b$c$d$e$"