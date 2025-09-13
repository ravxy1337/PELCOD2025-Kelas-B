print("=====NILAI KAMU YANG DIPEROLEH=====\n")

nilai_tugas = 90
nilai_uts = 67
nilai_uas = 75
#veriable bobot nilai
bobot_tugas = 0.3
bobot_uts = 0.3
bobot_uas = 0.4

nilai_akhir = (nilai_tugas * bobot_tugas) + (nilai_uts * bobot_uts) + (nilai_uas * bobot_uas)
nilai_akhir = round(nilai_akhir, 1)

print("Nilai Tugas Kamu: ", nilai_tugas)
print("Nilai UTS kamu: ", nilai_uts)
print("Nilai UAS kamu: ", nilai_uas)
print("================================================")
print("Nilai akhir dari tugas: ", nilai_tugas * bobot_tugas)
print("Nilai akhir dari UTS: ", nilai_uts * bobot_uts)
print("Nilai akhir dari UAS: ", nilai_uas * bobot_uas)
print("================================================")
print("nilai akhir mu adalah: ", nilai_akhir)