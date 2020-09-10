def Translate(text):
    test=""
    for x in text:
        if x.lower() in ['a','e','i','o','u','y','å','ä','ö']:
            test=test+x
        elif x.strip()=="":
            test=test+x
        else:
            test=test+x+'o'+x
    print(test)
text="this is fun"
Translate(text)
        