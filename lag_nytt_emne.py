emnekode=[]
sesong=[]
studiepoeng=[]

def nytt_emne():
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

nytt_emne()
print(f"Nytt emne er lagt til:\n{emnekode[-1]}, {sesong[-1]}, {studiepoeng[-1]} poeng ")



