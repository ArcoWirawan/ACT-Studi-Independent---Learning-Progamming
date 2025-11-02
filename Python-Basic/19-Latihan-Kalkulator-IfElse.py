## Membuat Kalkulator 
## Menggunakan if then and else

try:
    while True:
        print(f"{10*"="}SIMPLE CALCULATOR{10*"="}")
        num1 = float(input("Number 1 = "))
        num2 = float(input("Number 2 = "))
        math_operator = str(input("PILIH OPERATOR MATH (+ - * ** / ) = "))

        if math_operator == "+":
            tambah = num1 + num2
            print(f"{num1} + {num2} = {tambah}")
        elif math_operator == "-":
            kurang = num1 - num2
            print(f"{num1} -  {num2} = {kurang}")
        elif math_operator == "*":
            kali = num1 * num2
            print(f"{num1} x {num2} = {kali}")
        elif math_operator == "/":
            bagi = num1 / num2
            print(f"{num1} : {num2} = {bagi}")
        else:
            print("Ada yang terlewat, try again")
except KeyboardInterrupt:
    print("\nEXIT!!")
except ValueError:
    print("\nJANGAN MELEWATI ISIAN YANG ADA!!")






