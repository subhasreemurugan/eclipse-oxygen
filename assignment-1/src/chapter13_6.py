import urllib.request
url=input("enter the url ").strip()
file1 = urllib.request.urlopen(url)
file2=file1.read()
print(len(file2.split()))
file1.close()


