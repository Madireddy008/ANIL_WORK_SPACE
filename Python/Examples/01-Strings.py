#STRINGS:

#Variable Declaration
str1 = "Madireddy"
str2 = "Anil Kumar"
str3 = "Sravani"
str4 = "Anil Kumar Reddy"
str5 = "   Moviyasri Reddy   "

#String Concatination
Concat = str1 + " " + str2
Concat1 = str1 + " " + str3
print("String Concatination str1+str2:",Concat)
print("String Concatination str1+str3:",Concat1)

#String Length
str_length = len(str1)
print("Length of the string:", str_length)

#String Upper and LowerCase
uppercase = str1.upper()
lowercase = str3.lower()
print("Uppercase of str1 :", uppercase)
print("Lowercase of str3 :", lowercase)

#String Replacing
str_replace = str4.replace("Reddy", "Reddy Madireddy")
print("Modified text of str4 :", str_replace)

#String Split
str2_Split = str2.split()
print("Split of str2 :", str2_Split)

#String Strip
strip_str5 = str5.strip()
print("Stripped text:", strip_str5)

#String Substring
substring = "Kumar"
if substring in str4:
    print(substring, "found in the text")
else:
    print(substring,"Not Found in str4")