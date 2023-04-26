#Exercise 05
#1
def selection_sort(numbers: list):
    for fill_slot in range(0, len(numbers) - 1):
        position_of_max = fill_slot

        for location in range(fill_slot +1, len(numbers)):
            if numbers[location] < numbers[position_of_max]:
                position_of_max = location
        temp = numbers[fill_slot]
        numbers[fill_slot] = numbers[position_of_max]
        numbers[position_of_max] = temp

my_list = [3, 7, 8, 9, 4, 2, 1]
print(f'My list before sorting {my_list}')
selection_sort(my_list)
print(f'My list after sorting {my_list}')

#2
def binary_search(text: list, target: str):
    first = 0
    last = len(text) - 1

    while first <= last:
        mid = (first + last) // 2
        if text[mid] == target:
            return text[mid]
        else:
            if target < text[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return None

text = ["book", "table", "money", "pen", "hair"]
target = "money"
result = binary_search(text, target)
print(f"The word is '{result}'.")

#3-6
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def __my_hash(self, key):
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            hash_val = 0
            for char in key:
                hash_val = (hash_val * 31 + ord(char)) % self.size
            return hash_val
        else:
            raise ValueError("Key must be an integer or a string.")

    def put(self, key, data):
        hash_key = self.__my_hash(key)
        bucket = self.table[hash_key]
        for i, (k, d) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, data)
                return
        bucket.append((key, data))

    def get(self, key):
        hash_key = self.__my_hash(key)
        bucket = self.table[hash_key]
        for k, d in bucket:
            if k == key:
                return d
        return None
