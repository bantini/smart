import zipfile

filename = "/home/nilayan/Dropbox/ukr.txt.zip"
with zipfile.ZipFile(filename,"r") as reader:
	tweets = reader.read("ukr.txt")
	print tweets
	