# Tugas Praktikum 1

---

## Anggota Kelompok

| Nama                    | NRP        |
| ----------------------- | ---------- |
| M. Haziq Ridwan Parsa   | 5025251053 |
| Earlang Rangga Purwanto | 5025251054 |
| Bayu Setyo Nugroho      | 5025251061 |

---

## Solusi dari Permasalahan Largest Monotonically Increasing Subsequence (LIS)

### Deskripsi Masalah

Largest Monotonically Increasing Subsequence (LIS) adalah permasalahan untuk mencari subsequence terpanjang dari sebuah array bilangan, di mana setiap elemen dalam subsequence tersebut harus lebih besar dari elemen sebelumnya. Perlu diperhatikan bahwa subsequence tidak harus terdiri dari elemen-elemen yang bersebelahan di array asli, tetapi urutan relatif elemennya harus tetap sama.

**Contoh:**

```
Input  : [10, 9, 2, 5, 3, 7, 101, 18]
Output : Panjang = 4, Trail = [2, 3, 7, 18]
```

Terdapat beberapa algoritma yang bisa digunakan untuk menyelesaikan masalah LIS ini, di antaranya menggunakan Brute Force (Naive Approach), Dynamic Programming, Binary Search (Patience Sorting), Fenwick Tree, Divide and Conquer, dan lainnya. Namun, pada praktikum ini, kami hanya menggunakan 3 algoritma yaitu **Brute Force**, **Dynamic Programming**, dan **Binary Search (Patience Sorting)**.

---

### Fitur Program

- Bisa memilih algoritma yang diinginkan (atau menjalankan ketiganya sekaligus untuk perbandingan)
- Bisa memilih ingin menginput nilai sendiri atau menggunakan contoh array default
- Penjelasan mengenai Time Complexity dan Space Complexity menggunakan Big O Notation
- Penjelasan mengenai kelebihan dan kekurangan dari masing-masing algoritma
- Output berupa panjang subsequence beserta trail yang memuat nilai-nilai yang membentuk subsequence tersebut
- Validasi input dan penanganan edge case (array kosong, array satu elemen, dsb.)

---

### Algoritma yang Digunakan

| No  | Algoritma                        | Time Complexity | Space Complexity |
| --- | -------------------------------- | --------------- | ---------------- |
| 1   | Brute Force (Rekursif)           | O(2ⁿ)           | O(n)             |
| 2   | Dynamic Programming              | O(n²)           | O(n)             |
| 3   | Binary Search (Patience Sorting) | O(n log n)      | O(n)             |

#### 1. Brute Force

Mengeksplorasi seluruh kemungkinan kombinasi subsequence secara rekursif. Untuk setiap elemen, program memutuskan apakah elemen tersebut **diambil** (jika nilainya lebih besar dari elemen terakhir yang sudah diambil) atau **dilewati**, lalu membandingkan hasil dari kedua opsi tersebut untuk menemukan subsequence terpanjang.

- **Kelebihan:** Mudah dipahami dan diimplementasikan tanpa menggunakan struktur data kompleks, karena logikanya langsung mencerminkan definisi masalah.
- **Kekurangan:** Sangat lambat (eksponensial) dan hanya dapat digunakan untuk n kecil (n ≤ 20), karena banyak perhitungan berulang untuk state yang sama.

#### 2. Dynamic Programming

Membangun tabel `dp[]` di mana `dp[i]` menyimpan panjang LIS terpanjang yang berakhir di elemen ke-`i`. Setiap elemen dibandingkan dengan seluruh elemen sebelumnya untuk menentukan sambungan terbaik, sehingga perhitungan yang berulang pada Brute Force bisa dihindari.

- **Kelebihan:** Sederhana karena menggunakan tabel dynamic programming 1 dimensi dan jejaknya (trail) mudah ditelusuri menggunakan array `parent[]`.
- **Kekurangan:** Kurang optimal untuk n > 10.000 karena kompleksitasnya yang kuadratik.

#### 3. Binary Search (Patience Sorting)

Menjaga sebuah array bantu (`tails`) yang menyimpan nilai ekor terkecil untuk setiap kemungkinan panjang subsequence. Posisi penyisipan tiap elemen baru dicari menggunakan binary search, sehingga proses jauh lebih cepat dibanding pendekatan Dynamic Programming biasa.

- **Kelebihan:** Sangat cepat dan efisien dibandingkan algoritma lainnya, menjadi standar untuk data berukuran besar.
- **Kekurangan:** Konstruksi jejak (trail) memerlukan manajemen indeks tambahan yang cermat, karena array `tails` sendiri bukan representasi langsung dari subsequence yang valid.

> **Catatan:** Karena adanya lebih dari satu kemungkinan subsequence dengan panjang maksimal yang sama, trail hasil dari ketiga algoritma di atas bisa saja berbeda satu sama lain untuk input yang sama — namun panjangnya akan selalu identik.

---

### Cara Menjalankan Program

```bash
python nama_file.py
```

Setelah dijalankan, program akan menampilkan menu berikut:

```
================================================================================
     SOLUSI PERMASALAHAN LARGEST MONOTONICALLY INCREASING SUBSEQUENCE
================================================================================
PILIHAN MENU:
1. Gunakan Array Default [10, 9, 2, 5, 3, 7, 101, 18]
2. Gunakan array manual
3. Exit
================================================================================
```

- **Pilihan 1** akan langsung menjalankan ketiga algoritma menggunakan array contoh default.
- **Pilihan 2** meminta pengguna memasukkan array sendiri, dipisahkan dengan koma atau spasi (contoh: `5, 3, 8, 1, 9` atau `5 3 8 1 9`).
- **Pilihan 3** keluar dari program.

---

### Contoh Output

```
================================================================================
INPUT ARRAY          : [10, 9, 2, 5, 3, 7, 101, 18]
PANJANG ELEMEN       : 8
================================================================================

--------------------------------------------------------------------------------
[ALGORITMA] 1: Brute Force
--------------------------------------------------------------------------------
[WAKTU]        : O(2^n)
[SPACE]        : O(n)
[PANJANG]      : 4
[TRAIL]        : [2, 3, 7, 18]
[KELEBIHAN]    : Mudah dipahami dan diimplementasikan tanpa menggunakan struktur data kompleks.
[KEKURANGAN]   : Sangat lambat (eksponensial) dan hanya dapat digunakan untuk n kecil (n <= 20).

--------------------------------------------------------------------------------
[ALGORITMA] 2: Dynamic Programming
--------------------------------------------------------------------------------
[WAKTU]        : O(n^2)
[SPACE]        : O(n)
[PANJANG]      : 4
[TRAIL]        : [2, 5, 7, 101]
[KELEBIHAN]    : Sederhana karena menggunakan tabel dynamic programming 1 dimensi dan jejaknya mudah ditelusuri.
[KEKURANGAN]   : Kurang optimal untuk N > 10.000 karena kompleksitasnya yang kuadratik.

--------------------------------------------------------------------------------
[ALGORITMA] 3: Binary Search (Patience Sorting)
--------------------------------------------------------------------------------
[WAKTU]        : O(n log n)
[SPACE]        : O(n)
[PANJANG]      : 4
[TRAIL]        : [2, 3, 7, 18]
[KELEBIHAN]    : Sangat cepat dan efisien dibandingkan algoritma lainnya.
[KEKURANGAN]   : Konstruksi jejak memerlukan manajemen indeks tambahan yang cermat.
```

---

### Struktur Kode

```
├── nama_file.py
│   ├── brute_force()            # Algoritma 1: Brute Force rekursif
│   ├── dynamic_programming()    # Algoritma 2: DP O(n^2)
│   ├── binary_search()          # Algoritma 3: Patience Sorting O(n log n)
│   ├── tampilkan_semua()        # Menjalankan & menampilkan hasil ketiga algoritma
│   └── main()                   # Menu CLI interaktif
```
