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

while True:
    lag_nytt_emne()
    flere_emner=input("Vil du lage flere emner? (Ja/nei)").lower()
    if flere_emner!="ja":
        break
for i in range(len(sesong)):
    print(f"Nytt emne: {emnekode[i]}, {sesong[i]}, {studiepoeng[i]} poeng")
