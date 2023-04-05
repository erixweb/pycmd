import time
import requests
from os import system
import colorama
from colorama import Fore

colorama.init()

try:
    version = "0.2.3"
    while True:
        cmd: str = ""
        cmd: input = input("").split(" ")

        if cmd[1] == "v" or cmd[1] == "version":
            print(f"{Fore.GREEN}Your pywarp version is {version}{Fore.WHITE}")
        elif cmd[1] == "upgrade":
            print(f"{Fore.GREEN}Upgrading your pywarp version{Fore.WHITE}")
            system("""powershell -Command "(New-Object Net.WebClient).DownloadFile('https://raw.githubusercontent.com/erixweb/pycmd/master/main.py', 'C:\pywarp\pywarp.py')""")
            print(f"{Fore.GREEN}Upgraded your pywarp version, refresh this window{Fore.WHITE}")
        elif cmd[1] == "fetch":
            # inst https://example.com [-s, -r]

            url = cmd[2]
            pkg = url.replace("https://", "")
            installInitialTime = time.time()
            stream = requests.get(url)
        
            if cmd[3] == "-r":
                print(stream.text)
            elif cmd[3] == "-s":
                print(f"{Fore.GREEN}Installing {Fore.LIGHTCYAN_EX}{pkg}")
                with open("./installed", "w", encoding="utf-16") as f:
                    f.write(stream.text)

                installFinalTime = time.time()
                print(f"\n{Fore.GREEN}--> Installed {pkg} in {Fore.LIGHTCYAN_EX}{str((installFinalTime - installInitialTime) * 1000)[0:5]} ms\n{Fore.GREEN}--> Path: {Fore.LIGHTCYAN_EX}./installed{Fore.WHITE}")
        elif cmd[1] == "webscrap":
            # webscrap https://example.com [element] [-r, -s]

            url = cmd[2]
            element = cmd[3]
            conf = cmd[4]
            pkg = url.replace("https://", "")

            print(f"{Fore.GREEN}Scrapping {Fore.LIGHTCYAN_EX}{pkg}")
            installInitialTime = time.time()
            res = requests.get(url).text

            elementIndex = res.find(f"<{element}>")
            startIndex = elementIndex + len(f"<{element}>")
            endIndex = res.find(f"</{element}>")

            scrappedContent = res[startIndex:endIndex]

            if conf == "-r":
                print(scrappedContent)
                installFinalTime = time.time()
            elif conf == "-s":
                with open("./scrapped", "w", encoding="utf-16") as f:
                    f.write(scrappedContent)
                installFinalTime = time.time()
            print(f"{Fore.GREEN}[100%] Scrapped {Fore.LIGHTCYAN_EX}{pkg} {Fore.GREEN}took {Fore.LIGHTCYAN_EX}{str((installFinalTime - installInitialTime) * 1000)[0:5]}ms{Fore.WHITE}")
        elif cmd[1] == "dev":
            if cmd[2] == "--npm":
                print(f"{Fore.GREEN}Installing package.json dependencies")
                system("npm install")
                print(f"{Fore.GREEN}Starting web server{Fore.WHITE}")
                system("npm run dev")
        elif cmd[1] == "i":
            if cmd[3] == "--npm":
                iTime = time.time()
                print(f"{Fore.GREEN}Installing {Fore.LIGHTCYAN_EX}{pkg}")
                pkg = cmd[2]
                system(f"npm install {pkg}")
                fTime = time.time()
                print(f"{Fore.GREEN}[100%] Installed {Fore.LIGHTCYAN_EX}{pkg} took {Fore.LIGHTCYAN_EX}{str((fTime- iTime) * 1000)[0:5]}ms{Fore.WHITE}")
            elif cmd[3] == "--pnpm":
                iTime = time.time()
                print(f"{Fore.GREEN}Installing {Fore.LIGHTCYAN_EX}{pkg}")
                pkg = cmd[2]
                system(f"pnpm install {pkg}")
                fTime = time.time()
                print(f"{Fore.GREEN}[100%] Installed {Fore.LIGHTCYAN_EX}{pkg} took {Fore.LIGHTCYAN_EX}{str((fTime- iTime) * 1000)[0:5]}ms{Fore.WHITE}")
        elif cmd[1] == "create":
            pkg = cmd[2]
            iTime = time.time()
            if cmd[3] == "--npm":
                print(f"{Fore.GREEN}Creating {Fore.LIGHTCYAN_EX}{pkg} app")
                system(f"npm create {pkg}@latest")
                fTime = time.time()
                print(f"{Fore.GREEN}[100%] Created {Fore.LIGHTCYAN_EX}{pkg} app took {Fore.LIGHTCYAN_EX}{str((fTime- iTime) * 1000)[0:5]}ms{Fore.WHITE}")
            elif cmd[3] == "--pnpm":
                print(f"{Fore.GREEN}Creating {Fore.LIGHTCYAN_EX}{pkg} app")
                system(f"pnpm create {pkg}@latest")
                fTime = time.time()
                print(f"{Fore.GREEN}[100%] Created {Fore.LIGHTCYAN_EX}{pkg} app took {Fore.LIGHTCYAN_EX}{str((fTime- iTime) * 1000)[0:5]}ms{Fore.WHITE}")
        else:
            print(f"{Fore.RED}UnknownCommand: The command you're trying to run doesn't exist. Try pywarp inst{Fore.WHITE}")
except KeyboardInterrupt:
    system("cls")
    print(f"{Fore.GREEN}Succesfully exited.")