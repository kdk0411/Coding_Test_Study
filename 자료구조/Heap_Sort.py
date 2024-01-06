def Heapify(array, index, heap_size):
  largest = index
  left = 2 * index + 1
  right = 2 * index + 2

  if left < heap_size and array[right] > array[largest]:
    largest = left
  if right < heap_size and array[right] > array[largest]:
    largest = right
  if largest != index:
    array[largest], array[index] = array[index], array[largest]
    Heapify(array, largest, heap_size)

def Heap_Sort(array):
  for i in range(len(array)//2 -1, -1, -1):
    Heapify(array, i, len(array))

  for i in range(len(array) - 1, 0, -1):
    array[0], array[i] = array[i], array[0]
    Heapify(array, 0, i)

  return array