import pikepdf
import time
from colorama import Fore

password_file = open("rockyou.txt")

i = 0
start_time = time.time()
for password in password_file:
    i += 1
    print(Fore.RED+f"\r {i} Password is tested {password.strip()}", end = "")
    try:
        pikepdf.open("encrypted.pdf",password = password.strip("\n"))
        end_time = time.time()
        print("\n")
        print(Fore.GREEN+ f"password found in {str(end_time-start_time)[:4]} second \nPassword is: ", end = "")
        print(Fore.BLUE+ f" {password}")

        break
    except:
        pass