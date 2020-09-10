print([x for x in range(1,1001) if x%17==0])

jamnalist=[x for x in range(265,291) if x%2==0]
print(jamnalist)
summa=sum(jamnalist)
num=len(jamnalist)
average=summa/num
print(f"Summa: {summa}, medelvärdet: {average}")
