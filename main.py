import time
import requests
from os import system
from os import getcwd
from os import chdir
from os import mkdir
from os import listdir
import colorama
from colorama import Fore

colorama.init()

try:
    version = "1.0.0"
    while True:
        cmd: str = ""
        cmd: input = input("").split(" ")

        if cmd[0] == "v" or cmd[0] == "version":
            print(f"{Fore.GREEN}Your pywarp version is {version}{Fore.WHITE}")
        elif cmd[0] == "upgrade":
            print(f"{Fore.GREEN}Upgrading your pywarp version{Fore.WHITE}")
            system("""powershell -Command "(New-Object Net.WebClient).DownloadFile('https://raw.githubusercontent.com/erixweb/pycmd/master/main.py', 'C:\pywarp\pywarp.py')""")
            print(f"{Fore.GREEN}Upgraded your pywarp version, refresh this window{Fore.WHITE}")
        elif cmd[0] == "fetch":
            # inst https://example.com [-s, -r]

            url = cmd[1]
            pkg = url.replace("https://", "")
            installInitialTime = time.time()
            stream = requests.get(url)
        
            if cmd[2] == "-r":
                print(stream.text)
            elif cmd[2] == "-s":
                print(f"{Fore.GREEN}Installing {Fore.LIGHTCYAN_EX}{pkg}")
                with open("./installed", "w", encoding="utf-16") as f:
                    f.write(stream.text)

                installFinalTime = time.time()
                print(f"\n{Fore.GREEN}--> Installed {pkg} in {Fore.LIGHTCYAN_EX}{str((installFinalTime - installInitialTime) * 1000)[0:5]} ms\n{Fore.GREEN}--> Path: {Fore.LIGHTCYAN_EX}./installed{Fore.WHITE}")
        elif cmd[0] == "webscrap":
            # webscrap https://example.com [element] [-r, -s]

            url = cmd[1]
            element = cmd[2]
            conf = cmd[3]
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
        elif cmd[0] == "dev":
            if cmd[1] == "--npm":
                print(f"{Fore.GREEN}Installing package.json dependencies")
                system("npm install")
                print(f"{Fore.GREEN}Starting web server{Fore.WHITE}")
                system("npm run dev")
        elif cmd[0] == "i":
            if cmd[2] == "--npm":
                iTime = time.time()
                print(f"{Fore.GREEN}Installing {Fore.LIGHTCYAN_EX}{pkg}")
                pkg = cmd[1]
                system(f"npm install {pkg}")
                fTime = time.time()
                print(f"{Fore.GREEN}[100%] Installed {Fore.LIGHTCYAN_EX}{pkg} took {Fore.LIGHTCYAN_EX}{str((fTime- iTime) * 1000)[0:5]}ms{Fore.WHITE}")
            elif cmd[2] == "--pnpm":
                iTime = time.time()
                print(f"{Fore.GREEN}Installing {Fore.LIGHTCYAN_EX}{pkg}")
                pkg = cmd[1]
                system(f"pnpm install {pkg}")
                fTime = time.time()
                print(f"{Fore.GREEN}[100%] Installed {Fore.LIGHTCYAN_EX}{pkg} took {Fore.LIGHTCYAN_EX}{str((fTime- iTime) * 1000)[0:5]}ms{Fore.WHITE}")
        elif cmd[0] == "create":
            pkg = cmd[1]
            iTime = time.time()
            if cmd[2] == "--npm":
                print(f"{Fore.GREEN}Creating {Fore.LIGHTCYAN_EX}{pkg} app")
                system(f"npm create {pkg}@latest")
                fTime = time.time()
                print(f"{Fore.GREEN}[100%] Created {Fore.LIGHTCYAN_EX}{pkg} app took {Fore.LIGHTCYAN_EX}{str((fTime- iTime) * 1000)[0:5]}ms{Fore.WHITE}")
            elif cmd[2] == "--pnpm":
                print(f"{Fore.GREEN}Creating {Fore.LIGHTCYAN_EX}{pkg} app")
                system(f"pnpm create {pkg}@latest")
                fTime = time.time()
                print(f"{Fore.GREEN}[100%] Created {Fore.LIGHTCYAN_EX}{pkg} app took {Fore.LIGHTCYAN_EX}{str((fTime- iTime) * 1000)[0:5]}ms{Fore.WHITE}")
        elif cmd[0] == "dir":
            print(f"{Fore.GREEN}Your current dir is {Fore.LIGHTCYAN_EX}{getcwd()}{Fore.WHITE}")
        elif cmd[0] == "vol":
            if cmd[1] == "c" or cmd[1] == "C":
                chdir("C:\\")
            elif cmd[1] == "e" or cmd[1] == "E":
                chdir("E:\\")
        elif cmd[0] == "cd":
            goto = cmd[1]

            chdir(f"{goto}")
        elif cmd[0] == "mkdir":
            name = cmd[1]
            mkdir(name)
        elif cmd[0] == "ls":
            for dir in listdir():
                print(f"{Fore.GREEN}- {Fore.LIGHTCYAN_EX}{dir}{Fore.WHITE}")
        elif cmd[0] == "vscode":
            system("code .")
        elif cmd[0] == "cls":
            system("cls")
        elif cmd[0] == "cat":
            print(f"{Fore.GREEN}Here's {Fore.LIGHTCYAN_EX}{cmd[1]} content{Fore.WHITE}")
            FileStream = open(cmd[1], "r")
            print(FileStream.read())
        else:
            print(f"{Fore.RED}UnknownCommand: The command you're trying to run doesn't exist. Try pywarp inst{Fore.WHITE}")
except:
    system("cls")
    print(f"{Fore.RED}Error")