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

 
#FOR RANDOM DATA
arr_no_of_data=[]
arr_time=[]
for i in range(1,11):
    arr_nos=[]
    for j in range(i*100):
        arr_nos.append(randint(0,i*100))
    start_time=time.time()
    merge_sort(arr_nos,0,i*100-1)
    end_time=time.time()
    arr_no_of_data.append(i*100)
    arr_time.append(int((end_time-start_time)*1000))
    
plt.plot(arr_no_of_data,arr_time,marker='o', markersize=5, label='random data')

#FOR INCREASING DATA
arr_no_of_data=[]
arr_time=[]
for i in range(1,11):
    arr_nos=[]
    for j in range(i*100):
        arr_nos.append(j)
    start_time=time.time()
    merge_sort(arr_nos,0,i*100-1)
    end_time=time.time()
    arr_no_of_data.append(i*100)
    arr_time.append(int((end_time-start_time)*1000))

plt.plot(arr_no_of_data,arr_time,marker='o', markersize=5, label='increasing data')

#FOR DECREASING DATA
arr_no_of_data=[]
arr_time=[]
for i in range(1,11):
    arr_nos=[]
    for j in range(i*100):
        arr_nos.append(i*100-j)
    start_time=time.time()
    merge_sort(arr_nos,0,i*100-1)
    end_time=time.time()
    arr_no_of_data.append(i*100)
    arr_time.append(int((end_time-start_time)*1000))

plt.plot(arr_no_of_data,arr_time,marker='o', markersize=5, label='decreasing data')

#PLOTTING 
plt.xlabel('No of Data')
plt.ylabel('Time in milisec')
plt.title('Merge_Sort')
plt.legend() 
plt.show()
