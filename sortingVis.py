from tkinter import *
from tkinter import ttk
import random
import heapq
from numpy import result_type

window = Tk()
window.title("Sorting Visualization")
window.geometry('800x600')
background = "white smoke"
window.configure(bg=background)
sorting_algos = ('Insertion Sort', 'Bubble Sort', 'Quick Sort', 'Merge Sort')


def generate_array():
    array = []
    for x in range(100):
        array.append(random.randint(1, 50))
    return array


y = generate_array()

example = [5, 1, 2, 7, 3]

# SORTING ALGORITHMS


def insertion_sort(array, callback):
    for idx in range(len(array)-1):
        if array[idx] > array[idx+1]:
            idx2 = idx+1
            while idx2 != 0 and array[idx2] < array[idx2-1]:
                array[idx2], array[idx2-1] = array[idx2-1], array[idx2]
                callback()
                idx2 -= 1


def bubble_sort(array, callback):
    changed = True
    while changed:
        changed = False
        for idx1 in range(len(array)-1):
            idx2 = idx1 + 1
            if array[idx1] > array[idx2]:
                array[idx1], array[idx2] = array[idx2], array[idx1]
                changed = True
                callback()


# def heap_sort(array, callback):
#     heapq._heapify_max(array)
#     callback()
#     for p in range(len(array)):
#         array[-1-p] = heapq._heappop_max(array[:len(array) - p])
#         callback()


# heap_sort(example, lambda: 0)
# print(example)


def mergeSort(arr, lo, hi, callback):
    if hi-lo < 2:
        return arr
    half = int(lo + (hi-lo)/2)
    mergeSort(arr, lo, half, callback)
    mergeSort(arr, half, hi, callback)
    lst = []
    begin = lo
    mid = half
    while lo != mid and half != hi:
        if arr[lo] <= arr[half]:
            lst.append(arr[lo])
            lo += 1
        else:
            lst.append(arr[half])
            half += 1
    if lo != mid:
        for idx in range(lo, mid):
            lst.append(arr[idx])
    elif hi != half:
        for idx in range(half, hi):
            lst.append(arr[idx])
    for idx, element in enumerate(lst):
        arr[begin + idx] = element
        callback()
# Calls mergeSort with correct arguments (wrapper function)


def merge_sort(arr, callback):
    mergeSort(arr, 0, len(arr), callback)


example = [3, 5, 7, 2, 4, 8, 6]


def quickSort(array, lo, hi, callback):
    if hi-lo < 2:
        return
    pivot = partition(array, lo, hi, callback)
    quickSort(array, lo, pivot, callback)
    quickSort(array, pivot+1, hi, callback)


def quick_sort(arr, callback):
    quickSort(arr, 0, len(arr), callback)


def partition(array, lo, hi, callback):
    piv = hi - 1
    for idx in range(lo, piv):
        if array[idx] < array[piv]:
            array[lo], array[idx] = array[idx], array[lo]
            callback()
            lo += 1
    array[piv], array[lo] = array[lo], array[piv]
    # callback when we set the pivot
    callback()
    # pivot is put in place 'lo'
    return lo

    # return array if len(array) < 2 else quick_sort([x for x in array[1:] if x < array[0]]) + [array[0]] + quick_sort([x for x in array[1:] if x >= array[0]])


quick_sort(example, lambda: 0)
print(example)


def handle_sort():
    algo = box.current()
    if algo == 0:
        function = insertion_sort
    elif algo == 1:
        function = bubble_sort
    elif algo == 2:
        function = quick_sort
    elif algo == 3:
        function = merge_sort
    function(y, update_image)
# for x in insertion_sort(); elke x is elke keer dat je insertion_sort aanroept
# for x in insertion_sort(generate_array()):
#     print(x)


# [38, 27, 43, 3]

# [38, 27] // [43, 3]
# [38] // [27]


def handle_new_array():
    global y
    y = generate_array()
    update_image()


def update_image(fill="steel blue"):
    canvas.delete("all")
    # y = generate_array()
    for idx in range(len(y)):
        # coordinates: x1, y1, x2, y2
        canvas.create_rectangle(idx*5+5, 0, idx*5 + 10, y[idx]*10, fill="steel blue", outline="white")
    canvas.update()


# merge_sort(example, lambda: None)
# print(example)
# mergeSort(example, 0, len(example), lambda:None)
# Create button "Generate Array"
button = Button(text="Generate New Array", command=handle_new_array, bg="white")
button.place(x=10, y=10)
button.config(height=3, width=30)

# Create button "GO!"
go_button = Button(text="GO!", bg='white', command=handle_sort)
go_button.place(x=35, y=150)
go_button.config(height=5, width=22)

# Combobox label
lab = Label(window, text="Select the Sorting Algorithm:", bg=background)
lab.place(x=30, y=70)
# Combobox
selected_algo = StringVar()
keepvalue = selected_algo.get()
box = ttk.Combobox(window, textvariable=keepvalue, justify='center')
box['values'] = sorting_algos
box.current(0)
box.place(x=15, y=95)
box.config(width=30)


# Create Canvas for bar chart
height_canvas = 500
width_canvas = 525

canvas = Canvas(window, height=height_canvas, width=width_canvas, bg=background)
y = generate_array()
for idx in range(len(y)):
    # coordinates: x1, y1, x2, y2
    canvas.create_rectangle(idx*5+5, 0, idx*5 + 10, y[idx]*10, fill="steel blue", outline="white")
canvas.place(x=230, y=10)


window.mainloop()
