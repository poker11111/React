import tkinter as tk  # Importon modulën për ndërfaqe grafike (GUI)
import random  # Importon modulën për zgjedhje të rastësishme

def loja_gur_leter_gershere_gui():
    opsionet = ["gur", "letër", "gërshërë"]  # Opsionet e lojës: gur, letër, gërshërë
    piket_lojtari = 0  # Pikët fillestare të lojtarit
    piket_kompjuteri = 0  # Pikët fillestare të kompjuterit

    def luaj(lojtari_zgjedhja):
        nonlocal piket_lojtari, piket_kompjuteri  # Lejon ndryshimin e variablave nga funksioni prind

        kompjuteri_zgjedhja = random.choice(opsionet)  # Kompjuteri zgjedh një opsion rastësisht
        rezultat_var.set(f"Kompjuteri zgjodhi: {kompjuteri_zgjedhja}")  # Shfaq zgjedhjen e kompjuterit

        # Kontrollo kush fiton raundin sipas rregullave të lojës
        if lojtari_zgjedhja == kompjuteri_zgjedhja:
            status_var.set("Barazim!")  # Në rast barazimi
        elif (
            (lojtari_zgjedhja == "gur" and kompjuteri_zgjedhja == "gërshërë") or
            (lojtari_zgjedhja == "letër" and kompjuteri_zgjedhja == "gur") or
            (lojtari_zgjedhja == "gërshërë" and kompjuteri_zgjedhja == "letër")
        ):
            piket_lojtari += 1  # Lojtari fiton pikë
            status_var.set("Ti fitoje raundin!")  # Mesazh fitoreje për lojtarin
        else:
            piket_kompjuteri += 1  # Kompjuteri fiton pikë
            status_var.set("Kompjuteri fitoi raundin.")  # Mesazh humbjeje për lojtarin

        # Përditëso tekstet e pikëve në ndërfaqe
        pike_lojtari_var.set(f"Piket e tua: {piket_lojtari}")
        pike_kompjuteri_var.set(f"Piket e kompjuterit: {piket_kompjuteri}")

    # Krijo dritaren kryesore të aplikacionit
    dritarja = tk.Tk()
    dritarja.title("Loja Gur, Letër, Gërshërë")  # Titulli i dritares
    dritarja.geometry("350x250")  # Madhësia e dritares
    dritarja.configure(bg="#f0f8ff")  # Ngjyra e sfondit (light blue)

    # Variablat e lidhura me tekstet që do ndryshojnë gjatë lojës
    rezultat_var = tk.StringVar()
    status_var = tk.StringVar()
    pike_lojtari_var = tk.StringVar(value="Piket e tua: 0")
    pike_kompjuteri_var = tk.StringVar(value="Piket e kompjuterit: 0")

    # Etiketa për udhëzimet e lojtarit
    tk.Label(dritarja, text="Zgjidh: Gur, Letër apo Gërshërë", 
             font=("Arial", 14), bg="#f0f8ff", fg="#333").pack(pady=10)

    # Krijo një frame për butonat, për të organizuar më mirë layout-in
    frame_buttons = tk.Frame(dritarja, bg="#f0f8ff")
    frame_buttons.pack()

    # Butoni për zgjedhjen "Gur"
    tk.Button(frame_buttons, text="Gur", width=10, bg="#4CAF50", fg="white", 
              font=("Arial", 12, "bold"), command=lambda: luaj("gur")).pack(side="left", padx=5)

    # Butoni për zgjedhjen "Letër"
    tk.Button(frame_buttons, text="Letër", width=10, bg="#2196F3", fg="white", 
              font=("Arial", 12, "bold"), command=lambda: luaj("letër")).pack(side="left", padx=5)

    # Butoni për zgjedhjen "Gërshërë"
    tk.Button(frame_buttons, text="Gërshërë", width=10, bg="#f44336", fg="white", 
              font=("Arial", 12, "bold"), command=lambda: luaj("gërshërë")).pack(side="left", padx=5)

    # Etiketat që tregojnë zgjedhjen e kompjuterit dhe rezultatin e raundit
    tk.Label(dritarja, textvariable=rezultat_var, font=("Arial", 12), bg="#f0f8ff", fg="#555").pack(pady=5)
    tk.Label(dritarja, textvariable=status_var, font=("Arial", 12, "bold"), bg="#f0f8ff", fg="#000").pack(pady=5)

    # Etiketat që tregojnë pikët e lojtarit dhe kompjuterit
    tk.Label(dritarja, textvariable=pike_lojtari_var, font=("Arial", 12), bg="#f0f8ff", fg="#008000").pack(pady=2)
    tk.Label(dritarja, textvariable=pike_kompjuteri_var, font=("Arial", 12), bg="#f0f8ff", fg="#800000").pack(pady=2)

    # Nis dritaren dhe fillon programin
    dritarja.mainloop()

# Thirr funksionin kryesor nëse ky skedar ekzekutohet direkt
if __name__ == "__main__":
    loja_gur_leter_gershere_gui()
kur fillon 