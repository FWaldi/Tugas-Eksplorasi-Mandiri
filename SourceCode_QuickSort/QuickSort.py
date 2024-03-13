def quicksort(arr, kiri, kanan):
    if kiri < kanan:
        posisi_pembagi = partisi(arr, kiri, kanan)
        quicksort(arr, kiri, posisi_pembagi - 1)
        quicksort(arr, posisi_pembagi + 1, kanan)

def partisi(arr, kiri, kanan):
    pivot = arr[kiri]
    i = kiri
    j = kanan + 1
    while True:
        i += 1
        while i <= kanan and arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[kiri], arr[j] = arr[j], arr[kiri]
    return j

# Penggunaan contoh
arr = [8, 3, 2, 9, 7, 1, 5, 4]
quicksort(arr, 0, len(arr) - 1)
print(arr)  # Output: [1, 2, 3, 4, 5, 7, 8, 9]
