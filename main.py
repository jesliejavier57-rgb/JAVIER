# ASSESSMENT 3.7: SORTING ALGORITHMS
# FULL NAME: JESLIE JAVIER
# SORTING METHOD: BUBBLE SORT (ASCENDING A-Z)


def prepare_unique_letters(full_name: str) -> list[str]:
    """Extract letters only (exclude symbols/non-letters) and discard duplicates."""
    seen = set()
    unique_letters = []
    for char in full_name.upper():
        if char.isalpha() and char not in seen:
            seen.add(char)
            unique_letters.append(char)
    return unique_letters


def bubble_sort(arr: list[str]) -> list[str]:
    """Sort an array of letters in ascending order using Bubble Sort."""
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        if not swapped:
            break
    return sorted_arr


full_name = "JESLIE JAVIER"

# Two arrays: unsorted and sorted (duplicates discarded, symbols excluded)
unsorted_array = prepare_unique_letters(full_name)
sorted_array = bubble_sort(unsorted_array)

print("==========================================")
print("  ASSESSMENT 3.7: SORTING ALGORITHMS")
print("        NAME: JESLIE JAVIER")
print("==========================================")
print(f"Unsorted Array (Unique Letters): {unsorted_array}")
print(f"Sorted Array   (Bubble Sort)   : {sorted_array}")
print("==========================================")