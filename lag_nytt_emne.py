emnekode=[]
sesong=[]
studiepoeng=[]

def lag_nytt_emne():
    kode=input("Skriv inn emnekode:")
    tid=input("Skriv inn undervisningstid (høst/vår):")     
    poeng=int(input("Skriv inn studieppoeng for emnet:"))
    emnekode.append(kode.upper())
    sesong.append(tid.capitalize())
    studiepoeng.append(poeng)

lag_nytt_emne()


print(f"Nytt emne: {emnekode[-1]}, {sesong[-1]}, {studiepoeng[-1]} poeng")
