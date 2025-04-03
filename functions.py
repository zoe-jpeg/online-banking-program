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

#introduction function / greet user
def introduction():
     os.system("clear")
     intro = "Welcome to Cognito Inc. Banking."
     for letter in intro:
          sys.stdout.write(bold + letter + end)
          sys.stdout.flush()
          time.sleep(0.07)

     time.sleep(1.2)

     print()
     print()

     tagline = "Financials for the Future."
     for letter in tagline:
          sys.stdout.write(blue + italics + letter + end)
          sys.stdout.flush()
          time.sleep(0.07)
     print()

def user_login():
     os.system("clear")
     message = "LOGIN TO YOUR ACCOUNT"
     for letter in message:
          sys.stdout.write(bold + letter + end)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(0.8)
     print()
     account_number = input("\nAccount Number: ")
     pin_number = input("PIN: ")