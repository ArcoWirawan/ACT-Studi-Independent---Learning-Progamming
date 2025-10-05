"""
Suhu :
1. Celcius
2. Reamur
3. Fahrenheit
4. Kelvin

"""

# Konversi celcius ke satuan suhu lain

c_input = int(input("Berapa suhu hari ini = "))
print(f"Suhu hari ini adalah {c_input}")

# Rumus konversi ke Reamur
CelciusToReamur = 4/5 * c_input
print(f"Suhu hari ini {CelciusToReamur}")

# Rumus konversi ke Fahrenheit
CelciusToFahrenheit = 9/5 * c_input + 32
print(f"Suhu hari ini {CelciusToFahrenheit}F")

# Rumus konversi ke Kelvin
CelciusToKelvin = c_input + 273
print(f"Suhu hari ini {CelciusToKelvin}K")



### EXAM ###
# 1. konversi Fahrenheit ke kelvin 
FahrenheitToKelvin = 5/9 * (CelciusToFahrenheit - 32) + 273
print(f"Hasil konversi Fahrenheit to Kelvin = {FahrenheitToKelvin}")

# 2. Konversi Kelvin to Fahrenheit
KelvinToFahrenheit = 9/5 * (CelciusToKelvin - 273) + 32
print(f"Hasil konversi Kelvin to Fahrenheit = {KelvinToFahrenheit}")

