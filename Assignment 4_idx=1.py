s1 = "Python is a powerful high-level, object-oriented programming language created by Guido van Rossum."
s2 = "It has simple easy-to-use syntax, making it the perfect language for someone trying to learn computer programming for the first time."
s3 = "Professionally, Python is great for backend web development, data analysis, artificial intelligence, and scientix computing."

length = len(s1) + len(s2) + len(s3)
wCount = len(s1.split()) + len(s2.split()) + len(s3.split())

s2m = s2.strip(" ")
s3m = s3.strip(" ")

# using first index = 1
secret = s1[-20] 
secret += s1[-3]
secret += s1[-81]
secret += s2m[41]
secret += s2m[3]
secret += s3m[-31]
secret += s3m[-9]

print("Total characters in string s1, s2 and s3 are {} characters".format(length))
print("Total words in string s1, s2 and s3 are {} words".format(wCount))
print("The secret code is {}".format(secret))