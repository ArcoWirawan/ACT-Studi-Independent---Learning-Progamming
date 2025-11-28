def Tambah(*args):
    result = 0 # hasil default
    for tambah in args: # variabel sementara (tambah), merupakan variabel dari param args
        result += tambah # 0 akan selalu ditambah dari var args
        
    return result

# def Kurang(*args):
#     hasil = args
#     hasil -= args
#     # for kurang in args:
#     #     operasi = hasil 
    
    return hasil
        
def Bagi(*args):
    hasil = 0
    for bagi in args:
        hasil /= bagi
        
    return hasil 

def Kali(*args):
    hasil = 1
    for kali in args:
        hasil *= kali
        
    return hasil

def Modulus(*args):
    for mds in args:
        hasil_bagi = mds
         
    
    return hasil_bagi

# print(Kali(10, 20))
# print(Bagi(10, 2))
        
print(Bagi(10, 2))