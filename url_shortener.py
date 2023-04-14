#URL shortener using python
import pyshorteners

url = input("\nEnter any URL to shorten: ")
shortener = pyshorteners.Shortener()
short_url = shortener.tinyurl.short(url)

print("\nThe shortened URL is as follows:",short_url,"\n")