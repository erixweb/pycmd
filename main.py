import time
import requests
from os import system


def main():
    inputCmd = input("")

    # Install html
    if inputCmd.startswith("inst --html"):

        url = inputCmd.replace("inst --html ", "")

        print(f"Installing resource {url}")
        # Tiempo cuando empiez a descargarse
        initialTime = time.time()

        opener = requests.get(url)
        # Escribir al archivo inst en el directorio actual
        with open("./inst", "w", encoding="utf-16") as f:
            f.write(opener.text)
        
        finalTime = time.time()
        
        print(f"Installed {url} in {str(finalTime - initialTime)[0:5]} ms")
    elif (inputCmd.startswith("inst --execute")):
        url = inputCmd.replace("inst --execute ", "")

        print(f"Installing resource {url}")
        # Tiempo cuando empiez a descargarse
        initialTime = time.time()

        opener = requests.get(url)
        # Escribir al archivo inst en el directorio actual
        with open(f"./exe-{str(url)[0:5]}", "w", encoding="utf-16") as f:
            f.write(opener.text)
        
        finalTime = time.time()
        
        print(f"Installed {url} in {str(finalTime - initialTime)[0:5]} ms")

        system(f"exe-{str(url)[0:5]}")
    elif (inputCmd.startswith("scrap ") and inputCmd.endswith("--save")):
        cmd = inputCmd.split(" ")
        url = cmd[1]
        element = cmd[2]

        cmd.pop(0)
        cmd.pop(2)
        
        res = requests.get(url).text

        elementIndex = res.find(f"<{element}>")
        startIndex = elementIndex + len(f"<{element}>")
        endIndex = res.find(f"</{element}>")

        scrappedContent = res[startIndex:endIndex]


        print(scrappedContent)

    else:
        main
    
main()