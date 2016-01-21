import os

def touch(file):
    f = open(file, "w")
    f.close()
def printFile(file):
    if os.path.isfile(file):
        print(" +----+ [J-Word - {0}] +----+ ".format(file))
        fileObj = open(file)
        for i in fileObj.readlines():
            print(i)
        print(" +----+ [End Of File] +----+")
    else:
        print("error> File does not exist. Use \"file touch {0}\" to create it.".format(file))
def writeTo(file, string):
    fObj = open(file, "w")
    fObj.write(string)
    fObj.close
    
