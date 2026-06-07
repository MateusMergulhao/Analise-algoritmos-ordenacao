#insertion_sort:
def insertion_sort(arr):
    
    a = arr[:]
    moves = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            moves += 1 

        a[j + 1] = key
        if j + 1 != i:
            moves += 1 

    return a, moves

#merge_sort:
def merge_sort(arr):
    
    moves = [0]

    def _merge(a, left, mid, right):
        left_part = a[left:mid + 1]
        right_part = a[mid + 1:right + 1]
        i = j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                a[k] = left_part[i]
                i += 1
            else:
                a[k] = right_part[j]
                j += 1
            moves[0] += 1
            k += 1

        while i < len(left_part):
            a[k] = left_part[i]
            i += 1
            k += 1
            moves[0] += 1

        while j < len(right_part):
            a[k] = right_part[j]
            j += 1
            k += 1
            moves[0] += 1

    def _sort(a, left, right):
        if left < right:
            mid = (left + right) // 2
            _sort(a, left, mid)
            _sort(a, mid + 1, right)
            _merge(a, left, mid, right)

    a = arr[:]
    _sort(a, 0, len(a) - 1)
    return a, moves[0]

#quick_sort:
def quick_sort(arr):
    
    a = arr[:]
    swaps = [0]

    def _partition(a, low, high):
        pivot = a[high]
        i = low - 1

        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                swaps[0] += 1

        a[i + 1], a[high] = a[high], a[i + 1]
        swaps[0] += 1
        return i + 1

    stack = [(0, len(a) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            p = _partition(a, low, high)
            stack.append((low, p - 1))
            stack.append((p + 1, high))

    return a, swaps[0]