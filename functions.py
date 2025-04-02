import time
import os
import sys

#color/style variables
red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = '\033[1m'
italics = '\033[3m'
underline = '\033[4m'
end = '\033[0m'

introduction():
     os.system("clear")
     intro = "Welcome to Incognito Banking."
     for letter in intro:
          sys.stdout.write(bold + letter + end)
          sys.stdout.flush()
          time.sleep(0.07)

     time.sleep(2)

     print()
     print()

     tagline = "Financials for the Future."
     for letter in tagline:
          sys.stdout.write(blue + italics + letter + end)
          sys.stdout.flush()
          time.sleep(0.07)

