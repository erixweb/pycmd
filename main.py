import time
import requests
from os import system


def main():
    cmd = input("").split(" ")

    if cmd[0] == "inst":
        # inst https://example.com [-s, -r]

        url = cmd[1]
        pkg = url.replace("https://", "")

        installInitialTime = time.time()
        stream = requests.get(url)

        if cmd[2] == "-r":
            print(stream.text)
        elif cmd[2] == "-s":
            with open("./installed", "w", encoding="utf-16") as f:
                f.write(stream.text)

            installFinalTime = time.time()
            print(f"\nInstalled {pkg} in {str(installFinalTime - installInitialTime)[0:5] * 10} ms\nPath: ./installed")
    elif cmd[0] == "webscrap":
        # webscrap https://example.com [element] [-r, -s]

        url = cmd[1]
        element = cmd[2]
        conf = cmd[3]

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
     
    main()
main()