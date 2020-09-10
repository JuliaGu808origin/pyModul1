def HittaLangstaOrdet(arr):
    max=0
    for x in arr:
        if len(x)>max:
            max=len(x)
            ord=x
    print(ord)

arr=["hello", "super_woman", "hi", "google"]
HittaLangstaOrdet(arr)