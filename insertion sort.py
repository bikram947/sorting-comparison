import matplotlib.pyplot as plt
import time
from random import randint

#INSERTION SORT FUNCTION
def insertion_sort(arr,n):
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

#FOR RANDOM DATA
arr_no_of_data=[]
arr_time=[]
for i in range(1,11):
    arr_nos=[]
    for j in range(i*100):
        arr_nos.append(randint(0,i*100))
    start_time=time.time()
    insertion_sort(arr_nos,i*100)
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
    insertion_sort(arr_nos,i*100)
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
    insertion_sort(arr_nos,i*100)
    end_time=time.time()
    arr_no_of_data.append(i*100)
    arr_time.append(int((end_time-start_time)*1000))

plt.plot(arr_no_of_data,arr_time,marker='o', markersize=5, label='decreasing data')

#PLOTTING 
plt.xlabel('No of Data')
plt.ylabel('Time in milisec')
plt.title('Insertion_Sort')
plt.legend() 
plt.show()
