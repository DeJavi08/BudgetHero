def hitung_sisa(uang_saku, pengeluaran_list):
    total = sum(pengeluaran_list)
    if total > 2 * uang_saku:
        raise ValueError("Error: Pengeluaran melebihi batas wajar!")
    sisa = uang_saku - total
    return total, sisa

def kategori_keuangan(sisa, uang_saku):
    persentase = sisa / uang_saku
    if persentase >= 0.3:
        return "Hemat"
    elif persentase >= 0.1:
        return "Cukup"
    else:
        return "Boros"

def main():
    try:
        uang_saku = float(input("Masukkan uang saku mingguan: "))
        hari = int(input("Masukkan jumlah hari (max 7): "))

        if uang_saku <= 0 or hari <= 0 or hari > 7:
            raise ValueError("Input tidak valid!")

        pengeluaran = []
        for i in range(hari):
            nilai = float(input(f"Pengeluaran hari ke-{i+1}: "))
            if nilai < 0:
                raise ValueError("Nominal pengeluaran harus positif!")
            pengeluaran.append(nilai)

        total, sisa = hitung_sisa(uang_saku, pengeluaran)
        kondisi = kategori_keuangan(sisa, uang_saku)

        print("\n=== LAPORAN KEUANGAN MINGGUAN ===")
        print(f"Total pengeluaran : Rp{total:,.2f}")
        print(f"Sisa saldo akhir  : Rp{sisa:,.2f}")
        print(f"Kondisi keuangan  : {kondisi}")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
