""" 
Kwargs = 

1. data disimpan dalam label (dictionary)
2. dipanggil dengan menyebutkan nama parameternya
3. parameter ditempatkan pada saat data dipanggil
4. pada definisi nama fungsi, dituliskan **kwargs 

2. **kwargs (Keyword Arguments)

    Wujud Asli: Dictionary {'kunci': 'nilai', 'kunci2': 'nilai2'}

    Analogi: Loker Barang. Si penjaga loker (fungsi) butuh label nama untuk menyimpan dan mengambil barangnya.
"""


def BioData(nama, hobi, fav_band):
    """default function"""
    print(f"Nama = {nama}")
    print(f"Hobi = {hobi}")
    print(f"band favorit = {fav_band}")
    

BioData("aarwannzxp","Touring", "The Jansen")


## use **kwargs

def Someone(**kwargs):
    print(kwargs["name"])
    print(f"Fav Band = {kwargs['band']}")
    
Someone(name="arwanzxp",band="The Jansen")


    