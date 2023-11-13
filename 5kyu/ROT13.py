# How can you tell an extrovert from an introvert at NSA?
# Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.
#
# I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
# According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.
#
# For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.
#
# Test examples:
#
# "EBG13 rknzcyr." -> "ROT13 example."
#
# "This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"

#https://www.codewars.com/kata/52223df9e8f98c7aa7000062
#my solution:

def rot13(message):
    p = ''
    for i in message:
        if ord(i) >= 65 and ord(i) < 78:
            p += chr(ord(i) + 13)
        elif ord(i) >= 78 and ord(i) <= 90:
            p += chr(ord(i) - 13)
        elif ord(i) >= 97 and ord(i) < 110:
            p += chr(ord(i) + 13)
        elif ord(i) >= 104 and ord(i) <= 122:
            p += chr(ord(i) - 13)
        elif ord(i) >= 136 and ord(i) <= 136:
            p += chr(ord(i) - 13)
        else:
            p += i

    return p