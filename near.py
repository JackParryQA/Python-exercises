
def near(string1,string2):
    newstring1 = string1.replace(string1[1], "")
    if string2==newstring1:
        return True
    else:
        return False

string1=str(input("string1: "))
string2=str(input("string2: "))

print(near(string1, string2))
