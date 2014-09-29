import msvcrt
import time
from random import shuffle, choice
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Global Data
URLS = []
defxpath = '//*[@id="headword"]/div/p/text()'
#baseurl = 'http://www.merriam-webster.com/dictionary/'
baseurl = 'http://mnemonicdictionary.com/?word='
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}

# Intilize Firefox
#driver = webdriver.Firefox()
driver = webdriver.Chrome()

def OpenNextWord():
    url = RandomUrl()
    word = url.replace(baseurl,'')
    print(word)
    # Copy word to clipboard
    pyperclip.copy(word)
    driver.get(url)
#    saveas = "C:/Users/Warlock/Desktop/images/"+word+'.jpg'
#    time.sleep(5)
#    driver.save_screenshot(saveas)
    return None


def RandomUrl():
    url = choice(URLS)
    URLS.remove(url)
    return url



def buildUrls(word):
    builturl = baseurl+word
    URLS.append(builturl)
    return None

def buildWords():
    greword = open('Shuffuled GRE 333.txt','r')
    while(1):
        word = greword.readline()
        if word == '':
            break
        buildUrls(word.strip('\n'))


def main():
    buildWords()
    shuffle(URLS)
    while(1):
        signal = msvcrt.getch()
        if signal == b'\xe0':
            OpenNextWord()
        elif signal ==b' ':
          print('{0} completed and {1} words left'.format(int(333-len(URLS)),len(URLS)))
        else:
            time.sleep(1)

if __name__=="__main__":
    main()