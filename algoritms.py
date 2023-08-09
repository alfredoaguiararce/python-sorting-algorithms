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