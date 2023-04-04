import random
import requests


def main():
    inputCmd = input("")

    if inputCmd.startswith("inst --html"):

        url = inputCmd.replace("inst --html ", "")
        opener = requests.get(url)


        print(f"Installing resource {url}")
        
        with open("./inst", "w", encoding="utf-8") as f:
            f.write(opener.text)

        
        print(f"Installed {url}")
        
    else:
        print("err")
    
main()