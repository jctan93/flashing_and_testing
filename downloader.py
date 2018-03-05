#!/usr/bin/python3
from bs4 import BeautifulSoup
import os, argparse, urllib.request

parser = argparse.ArgumentParser()
parser.add_argument("--LaaG", action='store_true')
parser.add_argument("--AaaG", action='store_true')
parser.add_argument("--url")

args = parser.parse_args()

#page  = urllib.request.urlopen("https://mcg-depot.intel.com/artifactory/cactus-absp-jf/build/eng-builds/master/PSI/daily/").read()
global laag_link
laag_link = "http://andromeda01.png.intel.com/share/apl/master/daily/pub/"

if args.url:
	laag_link = args.url

laag  = urllib.request.urlopen(laag_link).read()
#print(page)

laag_soup = BeautifulSoup(laag, "lxml")
#print(soup.prettify())

if args.LaaG:
	print("Downloading LaaG")
	for a in laag_soup.find_all("a", href=True):
		if "clearlinux.img" in a['href']:
			pass
		elif "." in a['href']:
			#print("Found: " + a['href'])
			download_link = laag_link + a['href']
			print("Download link: " + download_link)
			urllib.request.urlretrieve(download_link, a['href'])
	
if args.AaaG:
	print("Downloading AaaG")
