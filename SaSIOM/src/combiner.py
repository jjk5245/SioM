import xml.etree.ElementTree as ET
import re 

def findFunction(id):
    return 0

#variables
fileName      = "" # the name for the program file
fileExtension = "" # the extension for the program file

# open xml file

tree = ET.parse('../Architecture/program.xml')
root = tree.getroot()

#File
fileName = root.find("metadata").find("name").text # read program name
fileName = re.sub('[^A-Za-z0-9]+', '', fileName)
fileExtension = root.find("metadata").find("extension").text # read program extension
fileExtension = re.sub('[^A-Za-z0-9]+', '', fileExtension)
fileName = fileName + "." + fileExtension

# create file with program name
f = open("../systems/" + fileName, 'w')
f.truncate() #empty the file before use

#includes

#definitions
defs = ""
for function in root.find("code").find("manipulations").findall("function"):
    fId = re.sub('[^A-Za-z0-9]+', '', function.find("metadata").find("id").text)
    ff = open("../Blocks/Functions/f" + fId + ".py")
    defs += "\n" + ff.read() + "\n"
f.write(defs)

#Variables
data = "\n"
# read program data elements
for element in root.find("code").find("data").findall("element"):
    eName =  re.sub('[^A-Za-z0-9]+', '', element.find("name").text)
    eType = re.sub('[^A-Za-z0-9]+', '', element.find("type").text)
    eValu = re.sub('[^A-Za-z0-9]+', '', element.find("value").text)
    data += eName + " = " + eValu + "\n"

# Write data elements to write to program
f.write(data)

# code
code = ""
for function in root.find("code").find("manipulations").findall("function"):
    fName = re.sub('[^A-Za-z0-9]+', '', function.find("metadata").find("name").text)
    fOut  = ""
    fIn   = ""
    
    #output(s)
    for output in function.find("outputs").findall("output"):
        fOut += re.sub('[^A-Za-z0-9]+', '', output.find("name").text + ",")
        fOut += ","
    # remove last ',' in fOut
    fOut = fOut[:-1]
    
    #input(s)
    for inputz in function.find("inputs").findall("input"):
        fIn += re.sub('[^A-Za-z0-9]+', '', inputz.find("name").text + ",")
        fIn += ","
    # remove last ',' in fIn
    fIn = fIn[:-1]
    
    code += "\n"
    if(len(fOut) > 0):
        code += fOut + " = "
    code += fName + "(" + fIn + ")\n"
    
f.write(code)