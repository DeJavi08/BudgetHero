<h1 align="center">💸 Welcome to <b>BudgetHero</b> 👋</h1>
<p align="center">
  <img src="https://img.shields.io/badge/version-1.0-blue.svg" />
  <img src="https://img.shields.io/badge/python-3.10%2B-yellow.svg" />
  <img src="https://img.shields.io/badge/license-open--source-blue.svg" />
  <img src="https://img.shields.io/badge/status-stable-brightgreen.svg" />
</p>

<p align="center">
  <i>Simple personal finance tracker for students — manage your weekly allowance, track spending, and stay financially smart 💰</i>
</p>

## 🧠 Overview

**BudgetHero** adalah program sederhana berbasis Python yang membantu pelajar mengatur uang saku mingguan dengan mencatat pengeluaran harian, menghitung sisa saldo, dan memberikan evaluasi keuangan otomatis (*Hemat / Cukup / Boros*).

## 🏁 Features

✅ Catat pengeluaran harian  
✅ Hitung total & sisa saldo mingguan  
✅ Evaluasi kondisi keuangan otomatis  
✅ Validasi input agar lebih aman  
✅ Program ringan & mudah dijalankan di semua OS

## 🧩 Tech Specs

| Komponen              | Spesifikasi                 |
| --------------------- | --------------------------- |
| **Bahasa Pemrograman** | Python 3.10+                |
| **Platform**           | Windows / Linux / macOS     |
| **Editor**             | VSCode / Notepad / IDLE      |
| **Versi**              | 1.0 (Oktober 2025)          |

## ⚙️ How It Works

### 🔹 Input
- Uang saku mingguan  
- Jumlah hari (maksimal 7)  
- Daftar pengeluaran harian  

### 🔹 Process
1. Menjumlahkan total pengeluaran  
2. Menghitung sisa saldo  
3. Menentukan status keuangan  

### 🔹 Output
- Total pengeluaran mingguan  
- Sisa saldo akhir  
- Status keuangan: *Hemat / Cukup / Boros*

## 💻 Pseudocode

```text
Begin
    Input uang_saku
    Input jumlah_hari
    total_pengeluaran = 0
    For i = 1 to jumlah_hari:
        Input pengeluaran_harian
        total_pengeluaran += pengeluaran_harian
    sisa = uang_saku - total_pengeluaran
    If sisa >= 0.3 * uang_saku:
        Print "Hemat"
    Else if sisa >= 0.1 * uang_saku:
        Print "Cukup"
    Else:
        Print "Boros"
End
````

## 🧮 Source Code (Python)

```python
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
```

## 🧾 Example Run

**Input:**

```
Masukkan uang saku mingguan: 100000
Masukkan jumlah hari (max 7): 3
Pengeluaran hari ke-1: 20000
Pengeluaran hari ke-2: 30000
Pengeluaran hari ke-3: 10000
```

**Output:**

```
=== LAPORAN KEUANGAN MINGGUAN ===
Total pengeluaran : Rp60,000.00
Sisa saldo akhir  : Rp40,000.00
Kondisi keuangan  : Hemat
```

## 🚨 Error Handling

| Jenis Kesalahan      | Kondisi               | Pesan                                     |
| -------------------- | --------------------- | ----------------------------------------- |
| Input negatif        | Pengeluaran < 0       | "Input tidak valid"                       |
| Hari melebihi batas  | jumlah_hari > 7       | "Batas maksimal 7 hari"                   |
| Pengeluaran berlebih | total > 2 × uang_saku | "Error: Pengeluaran melebihi batas wajar" |

## 📊 Testing Results

| Uang Saku | Hari | Total Pengeluaran | Sisa  | Status |
| --------- | ---- | ----------------- | ----- | ------ |
| 100000    | 3    | 60000             | 40000 | Hemat  |
| 100000    | 5    | 85000             | 15000 | Cukup  |
| 100000    | 7    | 98000             | 2000  | Boros  |

## 🚀 Future Development

* [ ] Menambahkan grafik pengeluaran mingguan
* [ ] Menyimpan data ke file JSON / SQLite
* [ ] Membuat versi web atau mobile

---

## 👨‍💻 Author

**Javier Ahmad**
🎓 Pelajar & Youtuber @ Vibe Coding
📅 Versi: 1.0 (Oktober 2025)
📫 Kontak: [GitHub](https://github.com/DeJavi08)

<p align="center">
  <i>Created with ❤️ by Javier Ahmad</i><br>
  <img src="https://img.shields.io/badge/BudgetHero-Built%20with%20Python-blue?logo=python" />
</p>
