import argparse, os, time
import urllib.parse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


def Main():
	browser = webdriver.Chrome()
	#website = input("Website Address: ")
	browser.get("https://rishikeshyoga.in/")
	os.system('cls')
	print ("[+] Success! Opened Website, Bot Starting!")
	ExtractBot(browser)
	print ("[+] Success! Opened Website, Extracted!")
	browser.close()

def ExtractBot(browser):
	npage = BeautifulSoup(browser.page_source)
	f=open("website.txt","wb")
	f.write(npage.encode("utf-8"))
	f.close
	altt = getAlt(npage)
	f=open("alt.txt","w+")
	f.writelines(altt)
	f.close


def getAlt(page):
	links = []
	for link in page.find_all("img"):
		#url = link.get()
		print(link['alt'])
		links.append(link)
	return links

if __name__ == '__main__':       
    Main()