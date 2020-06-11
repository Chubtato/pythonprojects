
def isPallindrome(word):
        if (type(word) != 'string'):
            word = str(word)
        if (word == word[::-1]):
            return True

ls = ["car","dog","racecar","cat","mom","dad", "cac", "ccakcc", "ddaadd", "mmoamm", 1242443453, "!@#$", "she's maddam s'ehs"]
for item in ls:
    if (type(item) != 'string'):
            item = str(item)
    i=0
    t=0
    if len(item)%2 == 0:
        while i <= len(item)/2:
            if item[i] == item[len(item)-i-1]:
                t+=1
            i+=1
        if t>=(len(item))/2:
            print("%s is a pallindrome"%(item))
    else:
        while i < (len(item)-1)/2:
            if item[i] == item[len(item)-i-1]:
                t+=1
            i+=1
        if t>=(len(item)-1)/2:
            print("%s is a pallindrome"%(item))

print("---------------- from Pallindrom function ----------------")

for myword in ls:
    if (isPallindrome(myword)):
        print("%s - is a pallindrome" %(myword))
