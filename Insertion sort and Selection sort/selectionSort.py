def selectionSort(A) :
    for value in range(0,len(A)-1):
        i_min = value
        for i in range(i_min+1,len(A)):
            if A[i] < A[i_min]:
                i_min = i
        temp = A[value]
        A[value] = A[i_min]
        A[i_min] = temp
i_min = 0
length = int(input("Masukkan jumlah bilangan : "))
A=[]
for i in range(1,length+1):
    angka = int(input("Angka ke %i : " %i))
    A.append(angka)
selectionSort(A)
print ("Hasil sorting selection sort :" )
print (A)