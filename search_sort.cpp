#include <iostream>
using namespace std;

// Linear Search function (won't be used)
int linearSearch(int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target)
            return i;  // Return index if found
    }
    return -1;  // Return -1 if not found
}

// Bubble Sort function
void bubbleSort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

// Selection Sort function
void selectionSort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < size; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        swap(arr[i], arr[minIndex]);
    }
}

// Binary Search function
int binarySearch(int arr[], int size, int target) {
    int left = 0, right = size - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}

int main() {
    // Input the user to get the array size
    int size;
    cout << "Enter the number of elements: ";
    cin >> size;

    // Input the user to get the numbers inside the array
    int arr[size];
    cout << "Enter the elements: ";
    for (int i = 0; i < size; i++) {
        cin >> arr[i];
    }

    // Input the user to choose a method to sort the array
    int choice;
    cout << "Choose sorting method\n";
    cout << "1. Bubble Sort\n";
    cout << "2. Selection Sort\n";
    cin >> choice;
    
    // Call the functions to sort the array
    if (choice == 1) {
        bubbleSort(arr, size);
    } else if (choice == 2) {
        selectionSort(arr, size);
    }
    
    // Output the sorted array so the user knows
    cout << "Sorted array: ";
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    
    // Input the user to find a certain number within the array
    int target;
    cout << "\nEnter target value to search: ";
    cin >> target;
    
    // Output the result of finding the number within the array
    int result = binarySearch(arr, size, target);
    if (result != -1) {
        cout << "Target found at index " << result << endl;
    } else {
        cout << "Target not found." << endl;
    }
    
    return 0;
}
