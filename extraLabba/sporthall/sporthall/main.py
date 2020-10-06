from bokning import Bokning
from kund import Kund
from sporthall import SportHall
from typ import BanaTyp
from datetime import datetime

def checkDate(start, slut, begin, end): 
    if start>=begin and slut>=end: return False
    elif begin <= start <= end: return False
    elif begin <= slut <= end: return False
    return True
    #print(start, slut, begin, end)
    #print(type(start), type(slut), type(begin), type(end))

if __name__ == "__main__":
    kund1 = Kund("kund-1", "11111", "11111@gmail.com", "111", "testgatan 1")
    kund2 = Kund("kund-2", "22222", "22222@gmail.com", "222", "testgatan 2")
    tennis = SportHall (BanaTyp.TENNIS_BANA)
    squash = SportHall (BanaTyp.SQUASH_BANA)
    badminton = SportHall (BanaTyp.BADMINTON_BANA)
    bowling = SportHall (BanaTyp.BOWLING_BANA)
    halls = [tennis, squash, badminton,bowling]

    book1 = Bokning("2020-10-10 10:00", "2020-10-10 12:00", kund1, tennis)
    book2 = Bokning("2020-10-11 10:00", "2020-10-11 12:00", kund1, squash)
    book3 = Bokning("2020-10-10 13:00", "2020-10-10 15:00", kund2, tennis)
    booklist = [book1, book2, book3]

    kund1.addBokning(book1)
    kund1.addBokning(book2)
    kund2.addBokning(book3)

    while True:
        phone = input("log in av din telefon nummer -> ")
        kunds = [k for k in [kund1, kund2] if k.getTelefonnummer()==phone]
        if not kunds:
            print("Finns ingen registerad kund...")
            continue
        kund = kunds[0]
        print("Din bokning: ")
        for b in kund.getBokning():
            print(b)            

        newbok = input("skapa en ny bokning j/n -> ")
        if newbok=="j":
            chosenHall = input("Vilken hall väljer du (tennis/badminton/squash/bowling) ? -> ")
            bookHalls = [b for b in booklist if chosenHall.upper() in b.getHall().getTyp()]
            if bookHalls:
                for each in bookHalls:
                    print(each.writeTaken())
                dateStart1 = input("start tid YYYY-MM-DD hh:mm -> ")
                dateStart = datetime.strptime(dateStart1,"%Y-%m-%d %H:%M")
                dateSlut1 = input("slut tid YYYY-MM-DD hh:mm -> ")
                dateSlut = datetime.strptime(dateSlut1, '%Y-%m-%d %H:%M')
                go_out=False
                for eachdate in bookHalls:
                    [begin, end] = eachdate.getDates()
                    if not checkDate(dateStart, dateSlut, begin, end):
                        print("Date conflict, try again !")
                        go_out = True
                        break
                    #print(eachdate.getDates())
                    #print(type(eachdate.getDates()[0]))
                if go_out: continue
                nybook = Bokning(dateStart1, dateSlut1, kund, bookHalls[0].getHall())
                booklist.append(nybook)
                kund.addBokning(nybook)
                print("success !")
                #bookHalls = [b for b in booklist if chosenHall.upper() in b.getHall().getTyp()]
                #for each in bookHalls:
                #    print(each.writeTaken())
            else: 
                print("Ingen bokning just nu !")
                dateStart1 = input("start tid YYYY-MM-DD hh:mm -> ")
                dateStart = datetime.strptime(dateStart1,"%Y-%m-%d %H:%M")
                dateSlut1 = input("slut tid YYYY-MM-DD hh:mm -> ")
                dateSlut = datetime.strptime(dateSlut1, '%Y-%m-%d %H:%M')
                bookHalls = [b for b in halls if chosenHall.upper() in b.getTyp()]
                nybook = Bokning(dateStart1, dateSlut1, kund, bookHalls[0])
                booklist.append(nybook)
                kund.addBokning(nybook)
                print("success !")
        else: break

    
