times = int(input("Matar in ett antal minuter -> "))
if times<60:
    print(f"Antal minuter: {times}")
elif 60<=times<24*60:
    timmar=int(times/60)
    minuter=times%60
    print(f"Antal timmar {timmar}, antal minuter {minuter}")
else:
    dygn=int(times/60/24)
    timmar=int(times/60)-dygn*24
    minuter=times-timmar*60-dygn*24*60
    print(f"Antal dygn {dygn}, antal timmar {timmar}, antal minuter {minuter}")

belopp=int(input("Ange ett belopp som ska betalas -> "))
# lapp500,lapp100,koron10,koron5,korono2,koron1
lapp500=int(belopp/500)
rest=belopp%500
lapp100=int(rest/100)
rest=rest%100
koron10=int(rest/10)
rest=rest%10
koron5=int(rest/5)
rest=rest%5
koron2=int(rest/2)
koron1=rest%2
print("Result: ")
if lapp500:
    print(f"{lapp500} x 500-lappar")
if lapp100:
    print(f"{lapp100} x 100-lappar")
if koron10:
    print(f"{koron10} x 10-kronor")
if koron5:
    print(f"{koron5} x 5-kronor")
if koron2:
    print(f"{koron2} x 2-kronor")
if koron1:
    print(f"{koron1} x 1-kronor")