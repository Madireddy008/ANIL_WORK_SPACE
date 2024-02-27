'''
Srting:
    String is a Collection of charecters
Types of declaring the string
    1. Single Quotes Ex: a='Python'
    2. Double Quotes Ex: a="Python"
    3. Triple Quotes Ex: a=
String Methods:
    lower()         upper()         endswith()
    startswith()    replace()       split()
    count()         Rstrip()        Lstrip()
    removeprefix()  removesufix()   index()     find()
    
'''
Name="anil kumar reddy madireddy"
CName="ANIL KUMAR REDDY MADIREDDY"
print ('Printing the Name in Upper Case')
print (Name.upper())
print ('Printing CName in Lower Case')
print (CName.lower())
print ('is Name ends with madireddy ?')
print (Name.endswith("madireddy"))
print ('is Name ends with reddy ?')
print (Name.endswith("reddy"))
print ('is Name ends with kumar ?')
print (Name.endswith("kumar"))
print ('is Name starts with anil ?')
print (Name.startswith("anil"))
print ('is Name starts with a ?')
print (Name.startswith("a"))
print ('is Name starts with madi ?')
print (Name.startswith("madi"))
print ('replaceing ANIL KUMAR REDDY MADIREDDY with ANIL MADIREDDY')
print (CName.replace("ANIL KUMAR REDDY MADIREDDY","ANIL MADIREDDY"))
print ('printing Name using find and index string methods')
print (Name.find("anil"))
print (Name.index("anil"))
print (Name.find("krishna"))
#the below line will return error so commented
# print (Name.index("krishna"))
print ('printing CName & Name with count string method')
print ('Count of A in CName ?')
print (CName.count('A'))
print ('Count of D in CName ?')
print (CName.count('D'))
print ('Count of y in Name ?')
print (Name.count('y'))
print ('Count of r in Name ?')
print (Name.count('r'))
print ('removing suffix from Name=anil kumar reddy madireddy')
print (Name.removesuffix("madireddy"))
print ('removing prefix from Name=anil kumar reddy madireddy')
print (Name.removeprefix("anil kumar reddy"))
print ('printing CName with split')
print (CName.split())
print ('printing CName with strip')
print (CName)
print (len(CName))
print (CName.strip())