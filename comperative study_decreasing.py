import matplotlib.pyplot as plt
import time
from random import randint

#MERGE SORT FUNCTION
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
    L = [0] * (n1) 
    R = [0] * (n2) 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
    i = 0
    j = 0
    k = l   
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
def merge_sort(arr,l,r): 
    if l < r: 
        m = int((l+(r-1))/2)
        merge_sort(arr, l, m) 
        merge_sort(arr, m+1, r) 
        merge(arr, l, m, r) 


#BUBBLE SORT FUNCTION
def bubble_sort(arr,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                t=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=t


#INSERTION SORT FUNCTION
def insertion_sort(arr,n):
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key


 
#FOR DECREASING DATA
arr_no_of_data=[]
arr_time_merge=[]
arr_time_bubble=[]
arr_time_insertion=[]
for i in range(1,11):
    arr_no_of_data.append(i*100)
    
    arr_nos=[]
    for j in range(i*100):
        arr_nos.append(i*100-j)
    start_time=time.time()
    merge_sort(arr_nos,0,i*100-1)
    end_time=time.time()
    arr_time_merge.append(int((end_time-start_time)*1000))

    arr_nos=[]
    for j in range(i*100):
        arr_nos.append(i*100-j)
    start_time=time.time()
    bubble_sort(arr_nos,i*100)
    end_time=time.time()
    arr_time_bubble.append(int((end_time-start_time)*1000))

    arr_nos=[]
    for j in range(i*100):
        arr_nos.append(i*100-j)
    start_time=time.time()
    insertion_sort(arr_nos,i*100)
    end_time=time.time()
    arr_time_insertion.append(int((end_time-start_time)*1000))
    
plt.plot(arr_no_of_data,arr_time_merge,marker='o', markersize=5, label='merge sort')
plt.plot(arr_no_of_data,arr_time_bubble,marker='o', markersize=5, label='bubble sort')
plt.plot(arr_no_of_data,arr_time_insertion,marker='o', markersize=5, label='insertion sort')

#PLOTTING 
plt.xlabel('No of Data')
plt.ylabel('Time in milisec')
plt.title('Comperative Study on decreasing Data')
plt.legend() 
plt.show()
         
