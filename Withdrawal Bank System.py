print("selamat datang ke bank axlez")
Withdraw=float(input("masukkan jumlah uang yang ingin tarik:"))


if Withdraw > 1250000:
    print("Batas penarikan terlampaui")
elif Withdraw < 50000:
    print("Harus lebih dari Rp50000")
elif Withdraw % 50000 == 0:
    sisa_seratus = Withdraw // 100000
    sisa_limapuluh = (Withdraw - (sisa_seratus * 100000)) // 50000
    print(f"{sisa_seratus} lembar Rp100.000 dan {sisa_limapuluh} lembar Rp50.000")
else:
    print("Harus kelipatan Rp50.000")
