import sys
import os
import math
import random

args = sys.argv
if "-h" in args:
    print("Usage: psmk [OPTIONS]")
    print("    -l        Length of the password to generate, if unspecified, it uses 12.")
    print("    -ch       Characters to use, or {DEFAULT} for default character set of abcd... + capital letters and numbers. -hch for more info")
    print("    -me       Minimum entropy of the password in bits, if unspecified, uses 100.")
    print("    -ex       Characters to exclude from the password.")
    print("    -in       Characters to include in the password, apart from -ch.")
    print("    -c        Count, how many passwords to generate.")
    sys.exit()
if "-hch" in args:
    print("Character Sets:")
    print("    {DEFAULT}        Alphabet + Capital Letters + Numbers")
    print("    {REDUCED}        Alphabet + Numbers, Excluding Capital Letters.")
    print("    {EXTENDED}       Alphabet + Capital letters + numbers + special signs (!@#$%^&* etc..), includes all types of brackets as well.")
    sys.exit()

length = 12
charset = ""
min_entropy = 100
excluded_chars = ""
included_chars = ""
count = 1

def calculate_entropy(charset, password):
    return math.log2(math.pow(len(charset), len(password)))

for i, arg in enumerate(args):
    if arg == "-l" and not args[i+1].startswith("-"):
        length = args[i+1]
    elif arg == "-ch" and not args[i+1].startswith("-"):
        if args[i+1] == "{DEFAULT}":
            charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        elif args[i+1] == "{REDUCED}":
            charset = "abcdefghijklmnopqrstuvwxyz1234567890"
        elif args[i+1] == "{EXTENDED}":
            charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()[]{}"
        else:
            charset = args[i+1]
    elif arg == "-me" and not args[i+1].startswith("-"):
        min_entropy = args[i+1]
    elif arg == "-ex" and not args[i+1].startswith("-"):
        excluded_chars = args[i+1]
    elif arg == "-in" and not args[i+1].startswith("-"):
        included_chars = args[i+1]
    elif arg == "-c" and not args[i+1].startswith("-"):
        count = args[i+1]

charset = charset.replace(excluded_chars, "")
charset += included_chars
charset = "".join(dict.fromkeys(charset))

print(f"Going to generate {count} password(s)\nUsing characters: {charset}\nWith a minimum entropy of: {min_entropy}\nWith a length of: {length}")
print("")

padding = " "

attempts = 0
passwords = []
while len(passwords) < int(count):
    if attempts > 50:
        print("Couldn't generate a password that meets the entropy requirement, try lowering the entropy requirement or increasing the length or the characterset of the password")
        sys.exit()
    password = ''.join(random.choices(charset, k=int(length)))
    if int(calculate_entropy(charset, password)) >= int(min_entropy):
        passwords.append(password)
    else:
        attempts += 1

for password in passwords:
    print(f"{password} : Entropy: {int(calculate_entropy(charset, password))} bits")
