import sys

for arg in sys.argv:
    import os

    print(os.fsencode(arg))
