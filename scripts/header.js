const toDisplay = `\n./pywarp\npywarp inst https://example.com -s\nInstalling resource example.com\n\nInstalled example.com in 420ms\nPath: ./installed\n\npywarp webscrap https://example.com title -r\nExample Domain`
const speed = 45
let i = 0
document.querySelector("header").querySelector(".card").innerHTML = ""

const writeOne = () => {
    if (i < toDisplay.length) {
        document.querySelector("header").querySelector(".card").innerHTML += toDisplay.charAt(i)
        i++
        setTimeout(writeOne, speed);
    }
}

writeOne()