
emnekode=[]
sesong=[]
studiepoeng=[]

def lag_nytt_emne():
    kode=input("Skriv inn emnekode:").upper()
    tid=input("Skriv inn undervisningstid (høst/vår):").capitalize()
    while tid not in ["Høst", "Vår"] :  
        print("Må enten være høst eller vår! Prøv igjen.") 
        tid=input("Skriv inn undervisningstid (høst/vår):").capitalize()
    
    while True:
        try:
            poeng = int(input("Skriv inn studiepoeng (0–30): "))
            if 0 <= poeng <= 30:
                break
            else:
                print("Ugyldig! Studiepoeng må være mellom 0 og 30.")
        except ValueError:
            print("Dette er ikke et heltall. Prøv igjen.")

       
    emnekode.append(kode)
    sesong.append(tid)
    studiepoeng.append(poeng)

while True:
    lag_nytt_emne()
    flere_emner=input("Vil du lage flere emner? (ja/nei)").lower()
    if flere_emner!="ja":
        break
for i in range(len(sesong)):
    print(f"Nytt emne: {emnekode[i]}, {sesong[i]}, {studiepoeng[i]} poeng")


