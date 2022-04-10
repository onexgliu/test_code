import random
import string

password = ''.join([random.choice(string.hexdigits)
                    for n in range(10)])
print(password)
