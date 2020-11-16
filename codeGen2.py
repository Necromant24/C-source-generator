#datacontext


types2 = []

import classParser

types2.append(classParser.getClassObj("classes/Articles.cs"))


dc = "Rentoolo"
usingDc = "\tusing(var dc = " + dc + "())\r\t{\r"

getFuncs = []


def getExtensionMethodsForClasses(types2):
    extensionMethods = []

    num_types = ['int', 'decimal', 'long', 'double', 'int32', 'int64', 'float']
    startFunc = "public static IQueryable<"


    for type in types2:
        for field in type["fields"]:
            tName = type["name"]
            fName=field["name"]
            fType=field["type"]

            extensionMethod=""+startFunc+tName+"> filter"+tName+"By"+fName+"(this IQueryable<"+tName+"> items, "+fType+" "+fName.lower()+")\r{\r"
            extensionMethod+="\treturn items.Where(x=>x."+fName+"=="+fName.lower()+");\r}\r\r"

            if(num_types.__contains__(fType)):
                #fName = fName[0].lower()+fName[1:]

                #upper
                extensionMethod+= startFunc+tName+"> filter"+tName+"By"+fName+"Upper(this IQueryable<"+tName+"> items, "
                extensionMethod+= fType+ " "+ fName+")\r{\r\t"
                extensionMethod += "\treturn items.Where(x=>x." + fName + ">=" + fName + ");\r}\r\r"

                # lower
                extensionMethod += startFunc + tName + "> filter" + tName + "By" + fName + "Lower(this IQueryable<" + tName + "> items, "
                extensionMethod += fType + " " + fName + ")\r{\r\t"
                extensionMethod += "\treturn items.Where(x=>x." + fName + "<=" + fName + ");\r}\r\r"

                # upper strict
                extensionMethod += startFunc + tName + "> filter" + tName + "By" + fName + "UpperStrict(this IQueryable<" + tName + "> items, "
                extensionMethod += fType + " " + fName + ")\r{\r\t"
                extensionMethod += "\treturn items.Where(x=>x." + fName + ">" + fName + ");\r}\r\r"

                # lower strict
                extensionMethod += startFunc + tName + "> filter" + tName + "By" + fName + "LowerStrict(this IQueryable<" + tName + "> items, "
                extensionMethod += fType + " " + fName + ")\r{\r\t"
                extensionMethod += "\treturn items.Where(x=>x." + fName + "<" + fName + ");\r}\r\r"



            extensionMethods.append(extensionMethod)

    return extensionMethods



def funcStart(isStatic, className,prefix):
    staticWord = ""
    if isStatic:
        staticWord="static "

    return "public "+staticWord+" IQueryable<"+className+"> "+prefix

#deprecated
def funcStartWithSignature(fStart,className, fieldName, fieldType, prefix):
    signaturePrefix = ""
    if prefix=="filter":
        signaturePrefix="IQueryable<"+className+"> items, "

    fStart+=className+"By"+fieldName+"("+signaturePrefix+fieldType+" "+fieldName
    return fStart


def funcStartWithSignature2(className, fieldName, fieldType, prefix, isStatic):

    fStart = funcStart(isStatic,className,prefix)

    signaturePrefix = ""
    if prefix=="filter":
        signaturePrefix="this IQueryable<"+className+"> items, "

    fStart+=className+"By"+fieldName+"("+signaturePrefix+fieldType+" "+fieldName
    fStart+=")\n{\n\t"
    return fStart


def generateFStartWithDC(fStart,dc):
    fStart += "using(var dc = new "+dc+"())\n\t{\n\t\t"
    return fStart

#print(funcStart(True, "Tenders", "Get"))



def generateGetMethodsForClass(types):
    extensionMethods = []

    dc = "RentooloEntities"
    usingDc = "\tusing(var dc = " + dc + "())\r\t{\r"

    num_types = ['int', 'decimal', 'long', 'double', 'int32', 'int64', 'float']
    startFunc = "public static IQueryable<"

    for type in types:
        for field in type["fields"]:
            tName = type["name"]
            fName = field["name"]
            fType = field["type"]

            extensionMethod = "" + startFunc + tName + "> Get" + tName + "By" + fName + "(" + fType + " " + fName.lower() + ")\r{\r"
            extensionMethod += "\treturn dc."+tName+".Where(x=>x." + fName + "==" + fName.lower() + ");\r}\r\r"

            if (num_types.__contains__(fType)):
                # fName = fName[0].lower()+fName[1:]

                # upper
                extensionMethod += startFunc + tName + "> Get" + tName + "By" + fName + "Upper("
                extensionMethod += fType + " " + fName + ")\r{\r"
                extensionMethod += usingDc
                extensionMethod += "\t\treturn dc."+tName+".Where(x=>x." + fName + ">=" + fName + ");\r\t}\r}\r\r"

                # lower
                extensionMethod += startFunc + tName + "> Get" + tName + "By" + fName + "Lower("
                extensionMethod += fType + " " + fName + ")\r{\r"
                extensionMethod += usingDc
                extensionMethod += "\t\treturn dc."+tName+".Where(x=>x." + fName + "<=" + fName + ");\r\t}\r}\r\r"

                # upper strict
                extensionMethod += startFunc + tName + "> Get" + tName + "By" + fName + "UpperStrict("
                extensionMethod += fType + " " + fName + ")\r{\r"
                extensionMethod += usingDc
                extensionMethod += "\t\treturn dc."+tName+".Where(x=>x." + fName + ">" + fName + ");\r\t}\r}\r\r"

                # lower strict
                extensionMethod += startFunc + tName + "> Get" + tName + "By" + fName + "LowerStrict("
                extensionMethod += fType + " " + fName + ")\r{\r"
                extensionMethod += usingDc
                extensionMethod += "\t\treturn dc."+tName+".Where(x=>x." + fName + "<" + fName + ");\r\t}\r}\r\r"

            extensionMethods.append(extensionMethod)

    return extensionMethods


def getClassNameAndFields(path):
    import re
    with open(path,"r",encoding='utf-8') as f:

        textlines = f.read().split("\n")
        lines = []
        first = True
        for i in textlines:
            if first:
                if (bool(re.search(r"public.", i))):
                    lines.append(i.replace("public", "").strip().split("{")[0].strip().split(" ")[2])
                    first=False
                    continue

            if (bool(re.search(r"public.", i))):
                lines.append(i.replace("public", "").strip().split("{")[0].strip().split(" ")[1])


        className = lines[0]
        lines = lines[1:]

        
        return (className,lines,)


def generateUpdateMethod(className,fields):

    clName = className
    if className[len(className)-1]=='s':
        clName=className[:len(className)-1]


    method = "public static void UpdateAll"+clName+"Fields("+className+" oldItem, "+className+" newItem)\n{\n"

    for i in fields:
        method+= "\toldItem."+i+" = "+"newItem."+i+";\n"

    method+="}\n\n"
    return method

# the same but with custom var names
def generateUpdateMethod2(className,fields,name1,name2):

    clName = className
    if className[len(className)-1]=='s':
        clName=className[:len(className)-1]


    method = "public static void UpdateAll"+clName+"Fields("+className+" "+name1+", "+className+" "+name2+")\n{\n"

    for i in fields:
        method+= "\t"+name1+"."+i+" = "+name2+"."+i+";\n"

    method+="}\n\n"
    return method

#generateCloneMethod("classes/Articles.cs")

clNameAndFields = getClassNameAndFields("classes/Timed.cs")
# print(clNameAndFields)
print(generateUpdateMethod(clNameAndFields[0],clNameAndFields[1]))

fStart1 = funcStartWithSignature2("Tenders","Cost","int","filter",True)
print(fStart1)
print(generateFStartWithDC(fStart1,"RentooloEntities"))
#
# for i in generateGetMethodsForClass(types2):
#     for j in i.split("\r"):
#         print(j)
