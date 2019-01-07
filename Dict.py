import re
import urllib.request

#https://www.dictionary.com/browse/Word

url="https://www.dictionary.com/browse/"

word=input("Enter your word: ")

url=url+word

data=urllib.request.urlopen(url).read()

data1=data.decode("utf-8")

#print(data1)


m=re.search('meta name="description" content="',data1)

start=m.end()
end=start+300

newStr=data1[start:end]

#print(newStr)

m=re.search("See more.",newStr)

end=m.start()-1

definition=newStr[0:end]

print(definition)
