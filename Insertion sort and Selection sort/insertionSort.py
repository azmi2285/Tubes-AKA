def insertionSort(A):
    for value in range(1, len(A)):
        temp = A[value]
        i = value - 1
        while i >=0 and A[i] > temp:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = temp
value = 0
length = int(input("Masukkan jumlah bilangan : "))
A=[]
for i in range(1,length+1):
    angka = int(input("Angka ke %i : " %i))
    A.append(angka)

insertionSort(A)
print ("Hasil sorting insertion sort :" )
print (A)
