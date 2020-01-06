#PROGRAM PENGURUTAN ANGKA INPUTAN SERTA PENCARIAN ANGKA INPUTAN#
import time
def gaps(size):
    length = size.bit_length()
    for k in range(length - 1, 0, -1):
        yield 2**k - 1
 
 #proses shell short 
def shell_sort(alist):
    def insertion_sort_with_gap(gap):
        for i in range(gap, len(alist)):
            temp = alist[i]
            j = i - gap
            while (j >= 0 and temp < alist[j]):
                alist[j + gap] = alist[j]
                j = j - gap
            alist[j + gap] = temp
 
    for g in gaps(len(alist)):
        insertion_sort_with_gap(g)
        
#proses binary search
def binarySearch(alist, cari, l, x):
    if cari <= l:
        mid = (cari + (l-cari)//2)
        
        if alist[mid] == x:
            return mid
        if alist[mid]>x:
            #Fungsi map()
            return binarySearch(alist, cari, mid-1, x)
        else:
            return binarySearch(alist, mid+1, l, x)
    return -1
#fungsi rekrusi        
def datainput(alist):
    shell_sort(alist)   
    print("Sorted list: ", end="")
    #ITTERATOR
    for x in alist:
        print(x)
    #HIGH ORDER FUNCTION
    return(shell_sort)
    
def main():
    print("Shell Sort[program pengurutan angka]")
    print("Ketik " + " 1337 " + " untuk membuka fitur")
    firstanswer = int(input("Masukan Key : "))
    start_time = time.time()
    if firstanswer == 1337:
        alist = input("Masukan Angka Pengurutan : ").split()
        alist = [int(x) for x in alist]
        print("=====================")
        print("Hasil dari shell short")
        #RIO DARMAWAN
        datainput(alist)
        print("=====================")
        print("--- %s seconds ---" % (time.time() - start_time))
        print("=====================")
        start_time = time.time()
        print("Program binary search")
        cari = int(input("Masukkan nilai yang dicari : "))
        result = binarySearch(alist, 0, len(alist)-1, cari)
        if result == -1:
            print('Angka tidak ada di dalam list')
        else:
            print('Angka ada di dalam list',result)
        print("--- %s seconds ---" % (time.time() - start_time))
main()