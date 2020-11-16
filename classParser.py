

def getClassObj(path):
    import  re

    cs_types=['int','string','bool']

    num_types = ['int','decimal','long','double','int32','int64','float']


    with open(path,"r",encoding="utf-8") as f:

        textlines = f.read().split('\n')
        lines=[]

        classObj = {}

        fields = []

        for i in textlines:

            if(bool(re.search(r"public.",i))):

                lines.append(i.replace("public","").strip().split("{")[0].strip())

        className = lines[0].split("class")[1].strip()

        lines=lines[1:]


        for i in lines:
            ar = i.split(" ")
            field = {"type":ar[0],"name":ar[1]}
            fields.append(field)



        classObj["name"]=className
        classObj["fields"]=fields

        return classObj



#print(getClassObj("classes/Adverts.cs"))


