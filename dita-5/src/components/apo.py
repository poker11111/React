import random

def loja_gur_leter_gershere():
    opsionet = ["gur", "letër", "gërshërë"]
    piket_lojtari = 0
    piket_kompjuteri = 0
    raundi = 1

    print("🎮 Loja Gur, Letër, Gërshërë!")
    print("Loja ka 3 raunde. Le të fillojmë!\n")

    while raundi <= 3:
        print(f"--- Raundi {raundi} ---")
        lojtari = input("Zgjedhja jote (gur, letër, gërshërë): ").lower()

        if lojtari not in opsionet:
            print("❌ Zgjedhje e pavlefshme! Ju lutem shkruani: gur, letër ose gërshërë.")
            continue

        kompjuteri = random.choice(opsionet)
        print(f"🤖 Kompjuteri zgjodhi: {kompjuteri}")

        if lojtari == kompjuteri:
            print("🔄 Barazim!")
        elif (
            (lojtari == "gur" and kompjuteri == "gërshërë") or
            (lojtari == "letër" and kompjuteri == "gur") or
            (lojtari == "gërshërë" and kompjuteri == "letër")
        ):
            print("✅ Fitove këtë raund!")
            piket_lojtari += 1
        else:
            print("❌ Kompjuteri fitoi këtë raund.")
            piket_kompjuteri += 1

        print(f"Rezultati: Ti {piket_lojtari} - {piket_kompjuteri} Kompjuteri\n")
        raundi += 1

    print("🎲 Loja përfundoi!")
    if piket_lojtari > piket_kompjuteri:
        print("🏆 Urime! Ti fitove lojën!")
    elif piket_kompjuteri > piket_lojtari:
        print("💻 Kompjuteri fitoi lojën. Provo përsëri!")
    else:
        print("🤝 Loja barazim!")

if __name__ == "__main__":
    loja_gur_leter_gershere()
