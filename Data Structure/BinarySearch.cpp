#include <iostream>
#include <vector>

class Search {
public:
    int binarySearch(const std::vector<int>& arr, int target) {
        int low = 0;
        int high = arr.size() - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] == target)
                return mid;
            else if (arr[mid] < target)
                low = mid + 1;
            else
                high = mid - 1;
        }

        return -1;
    }
};


int main() {
    std::vector<int> arr = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
    int target = 12;

    Search searchObj;
    int result = searchObj.binarySearch(arr, target);

    if (result != -1)
        std::cout << "Element found at index " << result << std::endl;
    else
        std::cout << "Element not found" << std::endl;

	while(1);

    return 0;
}

