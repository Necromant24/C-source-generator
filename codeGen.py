
dc = "RentooloEntities"

type = "Tenders"
advField = "Cost"
advFieldType = "int"

get = "Get"

params = ["ById", "By[param]"]

iqueryable = "IQueryable"

startFunc = "public static IQueryable<"

getMethod = startFunc
usingDc="\tusing(var dc = "+dc+"())\r\t{\r"

getMethod += type+"> "+ "Get"+type+"By"+advField+"("+advFieldType+" "+advField.lower()+")"+"\r"+"{\r"
getMethod+= usingDc
getMethod+= "\t\treturn dc."+type+"."+"Where(x=>x."+advField+"=="+advField.lower()+");\r\t}\r}\r"


extensionFunc = startFunc + type+"> "+"filter"+type+"By"+advField
extensionFunc+="(this IQueryable<"+type+"> "+"items, "+advFieldType+ " "+advField.lower()+")\r{\r"
extensionFunc+=usingDc+"\t\treturn items.Where(x=>x."+advField+"=="+advField.lower()+");\r\t}\r}\r\r"


def generateGetMethod(dc,type, field, fieldType):
    num_types = ['int', 'decimal', 'long', 'double', 'int32', 'int64', 'float']

    startFunc = "public static IQueryable<"

    getMethod = startFunc
    usingDc = "\tusing(var dc = " + dc + "())\r\t{\r"

    getMethod += type + "> " + "Get" + type + "By" + field + "(" + fieldType + " " + field.lower() + ")" + "\r" + "{\r"
    getMethod += usingDc
    getMethod += "\t\treturn dc." + type + "." + "Where(x=>x." + field + "==" + field.lower() + ");\r\t}\r}\r"

    return getMethod



def printArr(arr):
    for i in arr.split("\r"):
        print(i)

print("-"*30)
printArr(generateGetMethod(dc,type,advField,advFieldType))
print("-"*20)

printArr(getMethod)
printArr(extensionFunc)