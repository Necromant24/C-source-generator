import classParser
import re
from helpers.formater import printArr, formatStrArrToOne

def generateStrClass(obj):
    print(obj)

def generateStrClass2(path):
    with open(path,'r', encoding='utf-8') as f:
        text = f.read()
        text = re.sub(r'\t\t. ','',text)
        print(text)


def getClass_lines(path):
    with open(path,'r', encoding='utf-8') as f:
        text = f.read()
        text = text.split('class')[1]
        text = '\t\tpublic'+text.split('public',maxsplit=1)[1]

        fields=[]
        for i in text.split("\n"):
            if(i.__contains__('public')):
                fields.append(i)

        return fields

def getListWithoutWSp(arr):
    arr2 = []
    for i in arr:
        if i!='':
            arr2.append(i)

    return  arr2

def replaceTypesToStrType(fields,newWord):

    ar = []
    for i in fields:
        endLine = ' {'+ i.split('{')[1]
        words = getListWithoutWSp(i.split(' '))
        newLine = words[0]+' '+newWord+' '+words[2] + endLine
        ar.append(newLine)

    return ar



print(formatStrArrToOne( replaceTypesToStrType( getClass_lines("classes/Timed.cs"),'string')))