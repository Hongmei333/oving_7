emnekode=[]
sesong=[]
studiepoeng=[]

def nytt_emne():
    kode=input("Skriv inn emnekode:")
    if kode in emnekode:
        print("Emnet er allerede i studieplanen, velg annet:")
        return
        
    tid=input("Skriv inn undervisningstid (Høst/Vår):").capitalize()
    if tid not in ["Høst", "Vår"]:  
        print("Ugyldig! Skriv enten høst eller vår:")  
        return 
    poeng=int(input("Skriv inn studieppoeng for emnet:"))
    emnekode.append(kode.upper())
    sesong.append(tid.capitalize())
    studiepoeng.append(poeng)

    print(f"Emnet {kode.upper()} er lagt til i studieplanen.")

while True:
    nytt_emne()
    flere_emner=input("Vil du lage flere emner? (Ja/nei)").lower()
    if flere_emner!="ja":
        break
for i in range(len(sesong)):
    print(f"Nytt emne: {emnekode[i]}, {sesong[i]}, {studiepoeng[i]} poeng")

studieplan = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
host_semester = [1, 3, 5]
var_semester = [2, 4, 6]


