import time
import requests
from os import system

while True:
    cmd = ""
    cmd = input("").split(" ")

    if cmd[1] == "help":
        print("Help")
    if cmd[1] == "inst":
        # inst https://example.com [-s, -r]

        url = cmd[2]
        pkg = url.replace("https://", "")
        installInitialTime = time.time()
        stream = requests.get(url)

        if cmd[3] == "-r":
            print(stream.text)
        elif cmd[3] == "-s":
            print(f"Instaling {pkg}")
            with open("./installed", "w", encoding="utf-16") as f:
                f.write(stream.text)

            installFinalTime = time.time()
            print(f"\nInstalled {pkg} in {str(installFinalTime - installInitialTime)[0:5]} ms\nPath: ./installed")
    elif cmd[1] == "webscrap":
        # webscrap https://example.com [element] [-r, -s]

        url = cmd[2]
        element = cmd[3]
        conf = cmd[4]

        res = requests.get(url).text

        elementIndex = res.find(f"<{element}>")
        startIndex = elementIndex + len(f"<{element}>")
        endIndex = res.find(f"</{element}>")

        scrappedContent = res[startIndex:endIndex]

        if conf == "-r":
            print(scrappedContent)
        elif conf == "-s":
            with open("./scrapped", "w", encoding="utf-16") as f:
                f.write(scrappedContent)