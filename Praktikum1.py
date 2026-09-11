def brute_foce(nums):
    def helper(index, prev_idx):
        if index == len(nums):
            return 0, []
        exclude_len, exclude_path = helper(index + 1, prev_idx)
        include_len, include_path = 0, []
        if prev_idx == -1 or nums[index] > nums[prev_idx]:
            sub_len, sub_path = helper(index+1, index)
            include_len = 1 + sub_len
            include_path = [nums[index]] + sub_path

        if include_len > exclude_len:
            return include_len, include_path
        return exclude_len, exclude_path
    return helper(0,-1)

def dynamic_programming(nums):
    n = len(nums)
    if n == 0:
        return 0, []
    dp = [1] * n
    parent = [-1] * n
    for i in range (n):
        for j in range(i):
            if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

    best = 0
    for i in range (n):
        if dp[i] > dp[best]:
            best = i
    path = []
    now = best
    while now != -1:
        path.append(nums[now])
        now = parent[now]
    path.reverse()
    return dp[best], path

def binary_search(nums):
    n = len(nums)
    if n == 0:
        return 0, []

    element_index = []
    parent = [-1] * n

    for i, x in enumerate(nums):
        low, high = 0, len(element_index)
        while low < high:
            mid = (low + high)//2
            if nums[element_index[mid]] < x:
                low = mid + 1
            else:
                high = mid

        pos = low
        if pos > 0:
            parent[i] = element_index[pos - 1]
        if pos == len(element_index):
            element_index.append(i)
        else:
            element_index[pos] = i

    path = []
    now = element_index[-1]
    while now != -1:
        path.append(nums[now])
        now = parent[now]

    path.reverse()

    return len(element_index), path

def tampilkan_semua(nums):
    print("\n" + "=" * 80)
    print(f"INPUT ARRAY          : {nums}")
    print(f"PANJANG ELEMEN       : {len(nums)}")
    print("=" * 80)

    if(len(nums) <= 20):
        panjang, trail = brute_foce(nums)
        print("\n" + "-" * 80)
        print("[ALGORITMA] 1: Brute Force")
        print("-" * 80)
        print("[WAKTU]        : O(2^n)")
        print("[SPACE]        : O(n)")
        print(f"[PANJANG]      : {panjang}")
        print(f"[TRAIL]        : {trail}")
        print("[KELEBIHAN]    : Mudah dipahami dan diimplementasikan tanpa menggunakan struktur data kompleks.")
        print("[KEKURANGAN]   : Sangat lambat (eksponensial) dan hanya dapat digunakan untuk n kecil (n <= 20).")
    else:
        print("[ALERT] Brute Force Tidak dapat melakukan komputasi saat n terlalu besar (n > 20)")

    panjang, trail = dynamic_programming(nums)
    print("\n" + "-" * 80)
    print("[ALGORITMA] 2: Dynamic Programming")
    print("-" * 80)
    print("[WAKTU]        : O(n^2)")
    print("[SPACE]        : O(n)")
    print(f"[PANJANG]      : {panjang}")
    print(f"[TRAIL]        : {trail}")
    print("[KELEBIHAN]    : Sederhana karena menggunakan tabel dynamic programming 1 dimensi dan jejaknya mudah ditelusuri.")
    print("[KEKURANGAN]   : Kurang optimal untuk N > 10.000 karena kompleksitasnya yang kuadratik.")
    
    panjang, trail = binary_search(nums)
    print("\n" + "-" * 80)
    print("[ALGORITMA] 3: Binary Search (Patience Sorting)")
    print("-" * 80)
    print("[WAKTU]        : O(n log n)")
    print("[SPACE]        : O(n)")
    print(f"[PANJANG]      : {panjang}")
    print(f"[TRAIL]        : {trail}")
    print("[KELEBIHAN]    : Sangat cepat dan efisien dibandingkan algoritma lainnya.")
    print("[KEKURANGAN]   : Konstruksi jejak memerlukan manajemen indeks tambahan yang cermat.")
    
    

def main():
    contoh_default = [10, 9, 2, 5, 3, 7, 101, 18]

    while True:
        print("\n" + "=" * 80)
        print("     SOLUSI PERMASALAHAN LARGEST MONOTONICALLY INCREASING SUBSEQUENCE     ")
        print("=" * 80)
        print("PILIHAN MENU:")
        print("1. Gunakan Array Default [10, 9, 2, 5, 3, 7, 101, 18]")
        print("2. Gunakan array manual")
        print("3. Exit")    
        print("=" * 80)
        pilihan = input("Masukkan pilihan anda (1/2/3): ").strip()

        if pilihan == "1":
            tampilkan_semua(contoh_default)
        elif pilihan == "2":
            raw_input = input("Masukkan angka-angka yang diinginkan yang dipisahkan dengan koma (,) atau spasi: ").strip()
            if not raw_input:
                print("[ALERT] Array tidak boleh kosong!!!")
                continue
            bersih = raw_input.replace(",", " ")
            arr = [int (x) for x in bersih.split()]
            tampilkan_semua(arr)
        elif pilihan == "3":
            print("\n===== Terima Kasih telah menggunakan program kami. =====\n")
            break
        else:
            print("[ALERT] Input invalid!")

if __name__ == "__main__":
    main()
