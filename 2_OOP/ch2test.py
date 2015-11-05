def addLetter (x):
    result = ord(x) - ord(a)
    return result


#start of the main program
#prompt user for a file

while True:
    speech = input("Enter file name:")

    wholeFile = open(speech, 'r+').read()
    lowlet = wholeFile.lower()
    letters= list(lowlet)
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    n = len(letters)
    f = float(n)
    occurrences = {}
    d = {}


    #number of letters
    for x in alpha:
        occurrences[x] = letters.count(x)
        d[x] =(occurrences[x])/f
    for x in occurrences:
        print (x, occurrences[x], d[x])
