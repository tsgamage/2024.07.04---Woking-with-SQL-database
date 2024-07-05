TEXT_FILE = "studentsIndex.txt"

def  docRead(path):
    strPath = f"{path}"
    method = open(strPath, "r").read()
    return method

def docWrite(path, data):
    strPath = f"{path}"
    strData = f"{data}"
    method = open(strPath, "w").write(strData)
    return method

loopTime = 0

def currentIndex():
    indexNum = int(docRead(TEXT_FILE))
    return indexNum

def increaseCurrentIndexByOne():
    indexNum = int(docRead(TEXT_FILE))
    indexNum += 1
    docWrite(TEXT_FILE, indexNum)