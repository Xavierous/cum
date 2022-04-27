import os
if __name__ == "__main__":
   try:
       os.system("git pull")
       __import__("run5").lisensi().folder()
   except Exception as e:
       exit(str(e))
