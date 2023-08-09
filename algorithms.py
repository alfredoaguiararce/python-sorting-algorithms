class Algorithms:
    @staticmethod
    def bubble_sort(arr):
        """
        The above function implements the bubble sort algorithm to sort an array in ascending order and
        yields the intermediate steps of the sorting process.
        
        :param arr: The parameter "arr" is a list of elements that you want to sort using the bubble
        sort algorithm
        """
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    yield arr

    @staticmethod
    def selection_sort(arr):
        """
        The function implements the selection sort algorithm to sort an array in ascending order.
        
        :param arr: The parameter "arr" is a list of elements that you want to sort using the selection
        sort algorithm
        """
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            yield arr


    @staticmethod
    def merge_sort(arr):
        """
        The function implements the merge sort algorithm to sort an array in ascending order.
        
        :param arr: The parameter "arr" is a list of elements that you want to sort using the merge
        sort algorithm
        """
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            # Recursive calls to merge_sort for left and right halves
            Algorithms.merge_sort(left_half)
            Algorithms.merge_sort(right_half)

            i = j = k = 0

            # Merge two halves back together
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            # Check if any elements were left
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

            yield arr