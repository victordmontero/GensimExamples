from gensim.summarization import summarize
from gensim.summarization import keywords
import sys
import getopt


def readToEnd(file):
    textFile = open(file, "r")
    content = textFile.read()
    textFile.close()
    return content


def writeToFile(txt, filename):
    textFile = open(filename, "w")
    textFile.write(txt)
    textFile.close()


def getoptions(argv):
    inputfile = ""
    summaryratio = ""
    keywordratio = ""
    helptext = argv[0] + \
        " -i <input file> -s <summary ratio> -k <keyword ratio>"
    try:
        opts, values = getopt.gnu_getopt(argv, "hi:s:k:")
        if "-s" not in argv or "-k" not in argv or "-i" not in argv:
            raise getopt.GetoptError("Missing arguments. Do the following:")
    except getopt.GetoptError as error:
        print error.msg
        print helptext
        sys.exit(2)
    for opt, args in opts:
        if opt == "-i":
            inputfile = args
        elif opt == "-s":
            summaryratio = args
        elif opt == "-k":
            keywordratio = args
    print "Input file is:", inputfile
    print "Summary ratio is:", summaryratio
    print "Keyword ratio is:", keywordratio
    return (inputfile, summaryratio, keywordratio)


argumentlist = getoptions(sys.argv)
text = readToEnd(argumentlist[0])

print 'Input text:'
print text

print "Summary:"
result = summarize(text, ratio=float(argumentlist[1]))
keywordsResult = keywords(text, ratio=float(argumentlist[2]))

print result

print "Keywords:"
print keywordsResult

writeToFile(result, "summary.txt")
writeToFile(keywordsResult, "keywords.txt")
