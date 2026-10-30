teks = input("masukan nilai: ")
try:
    nilai = float(teks)
    print(f"nilai = {nilai}")

except ValueError:
    print("input harus berupa angka.")