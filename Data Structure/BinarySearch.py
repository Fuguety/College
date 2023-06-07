class Search:
    def binary_search(self, arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1


arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 12

search_obj = Search()
result = search_obj.binary_search(arr, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")

