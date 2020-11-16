import classParser




def generateInputFormTags(pathToClass):
    import classParser
    from helpers.variables import numeric_types,date_types

    obj = classParser.getClassObj(pathToClass)

    inputs = []

    fields = obj['fields']

    for i in fields:
        type = 'text'
        if numeric_types.__contains__(i['type']):
            type = 'number'
        elif date_types.__contains__(i['type'].lower()):
            type='date'

        fName = i['name'][0].lower()+i['name'][1:]
        inp = "<input type=\""+type+"\" name=\""+fName+"\"  />"
        inputs.append(inp)


    print(obj)
    return  inputs

# obj - classParser.getClassObj
# model - variable name
# inps - generateInputFormTags
def generateWebForminpsWithData(inps,obj,model):

    fields = obj['fields']

    for i in range(len(inps)):
        inps[i] = inps[i][:len(inps[i])-2]+"value=\"<%="+model+"."+fields[i]['name']+"%>\" />"


    from helpers.formater import printArr

    printArr(inps)







import  helpers.formater as frmts

print(frmts.formatStrArrToOne( generateInputFormTags("classes/Timed.cs")))

#print(frmts.formatStrArrToOne( generateInputFormTags("classes/Articles.cs")))