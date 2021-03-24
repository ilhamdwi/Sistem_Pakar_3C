# Sistem_Pakar_3C
Tugas Sistem Pakar Foward Chain & Backward Chain

global fact global is_changed is_changed = True facts = [["Diam","Sedih"],["Galau","Sedih"],["Ketawa","Senang"]]

Kode di atas untuk mendefinisikan dan menyimpan variable global

def assert_fact(fact): global facts global is_changed if not fact in facts: facts += [fact] is_changed = True

Blok kode di atas adalah sebuah method perulangan untuk menyimpan fakta fakta baru

while is_changed: is_changed = False for A1 in facts: if A1[0] == "Ketawa": assert_fact(["Senang",A1[1]]) if A1[0] == "Diam": assert_fact(["Merana",A1[1]]) if A1[0] == "Diam" and ["Galau",A1[1]] in facts: assert_fact(["Murung",A1[1]]) print("FowardChain") print(facts)

Blok diatas adalah fungsi untuk melooping aturan aturan yang ditetapkan untuk menentukan fakta baru dengan metode Foward Chain kemudian menampilkan fakta tersebut

while is_changed: is_changed = False for A1 in facts: if A1[0] == "Diam" and ["Galau",A1[1]] in facts: assert_fact(["Merana",A1[1]]) if A1[0] == "Diam": assert_fact(["Merana",A1[1]]) if A1[0] == "Senang": assert_fact(["Sedih",A1[1]])

print("BackwardChain")
print(facts)

Blok diatas adalah fungsi untuk melooping aturan aturan yang ditetapkan untuk menentukan fakta baru dengan metode Backward Chain kemudian menampilkan fakta tersebut
