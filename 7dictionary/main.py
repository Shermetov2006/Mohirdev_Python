from lugat import lugat

soz=(input("iltimos so'z kiriting: ").lower()).strip()
tarjima=lugat.get(soz)

if tarjima==None:
    print(f"Bunday so'z mavjud emas.")
else:
    print(f"{lugat[soz]}")