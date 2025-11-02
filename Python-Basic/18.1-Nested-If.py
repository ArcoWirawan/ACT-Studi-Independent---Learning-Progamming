# kondisi if dalam if (Nested if)
# bagaian yang akan di cek dari if awal ke if cabang

Umur = 17
KTP = False

if Umur >= 17:
    print("Umur kamu sekarang boleh ikut pemilu")
    if KTP == True:
            print("Kamu boleh mengikuti pemilu")
    else: 
            print("KTP tidak ada tidak boleh mengikuti pemilu")
else:
    print("Umur dan tidak punya KTP belum diperbolehkan")

print("\n")
## Case 2 : Penilaian


nilai_ujian = 90
kehadiran = 80
nilai_harian = 77

if nilai_ujian >= 90 and kehadiran >= 80 and nilai_harian >= 75:
    print("Kamu lulus pada ujian ini!")
