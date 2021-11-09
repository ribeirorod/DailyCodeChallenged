
#built in sorted method
#optional merged.sort() / merged.sort(reverse=True) descending
def merge_sort (lists):
    merged = list(set([e for l in lists for e in l]))
    return sorted(merged)

#using bubble sort method
def merge_bubblesort(lists):
        merged = list(set([e for l in lists for e in l]))
        for i in range(len(merged)):
            issorted = True
            for j in range(len(merged) - i - 1):
                if merged[j] > merged[j+1]:
                    merged[j], merged[j + 1] = merged[j + 1], merged[j]
            if issorted:
                break
        return merged

# explore other sorting algorithms

assert merge_sort([[1], [1, 3, 5], [1, 10, 20, 30, 40]]) == [1, 3, 5, 10, 20, 30, 40]
assert merge_bubblesort([[1], [1, 3, 5], [1, 10, 20, 30, 40]]) == [1, 3, 5, 10, 20, 30, 40]