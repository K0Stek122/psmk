# psmk
A simple python script to generate passwords.
```
Usage: psmk [OPTIONS]
    -l        Length of the password to generate, if unspecified, it uses 12.
    -ch       Characters to use, or {DEFAULT} for default character set of abcd... + capital letters and numbers. -hch for more info
    -me       Minimum entropy of the password in bits, if unspecified, uses 100.
    -ex       Characters to exclude from the password.
    -in       Characters to include in the password, apart from -ch.
    -c        Count, how many passwords to generate.
```
