with open("sample.txt","r") as file:
    content = file.read()
    contenlist= content.split()
    print("word count",len(contenlist))