print("Program ini akan menentukan jumlah hari dalam bulan tertentu!")

def tahunkabisat(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
def haridibulan(month, year):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if tahunkabisat(year) and month == 2:
        return 29
    else:
        return days[month]

def nyoba():
    month = int(input("Masukkan bulan (1-12, 0 untuk keluar): "))
    if month == 0:
        return 0, 0
    year = int(input("Masukkan tahun (e.g., 2023): "))
    return month, year

while True:
    month, year = nyoba()
    if month == 0:
        print("Terima kasih telah menggunakan program saya. Sampai jumpa!")
        break
    elif 1 <= month <= 12:
        harinya = haridibulan(month, year)
        print(f"{harinya} hari dalam sebulan")
    else:
        print("Data tidak valid. Coba lagi.")

