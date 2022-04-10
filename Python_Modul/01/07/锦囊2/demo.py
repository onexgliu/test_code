import random
import string

password = ''.join([random.choice(string.octdigits)
                    for n in range(10)])
print(password)
