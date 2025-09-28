emnekode=[]
sesong=[]
studiepoeng=[]

def lag_nytt_emne(kode,tid,poeng):
    emnekode.append(kode.upper())
    sesong.append(tid.capitalize())
    studiepoeng.append(poeng)

lag_nytt_emne("dat100", 'høst', 10)

print(f"Nytt emne:{emnekode[-1]}, {sesong[-1]}, {studiepoeng[-1]} poeng")
