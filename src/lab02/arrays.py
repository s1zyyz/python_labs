def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """ Возвращает кортеж (минимум, максимум). Если список пуст — ValueError """
    if len(nums) == 0:
        raise ValueError
    
    max = nums[0]
    min = nums[0]
    
    for i in nums:
        if i > max:
            max = i
        if i < min:
            min = i
    return min,max

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """ Вернуть отсортированный список уникальных значений (по возрастанию) """
    if len(nums) == 0:
            return []
        
    last = list(set(nums))
    for i in range(len(last)):
        for j in range(i + 1, len(last)):
            if last[j] < last[i]:
                last[i], last[j] = last[j], last[i]
    return last


def flatten(mat: list[list | tuple]) -> list:
    """ список списков/кортежей в один список по строкам (row-major). Если встретилась строка/элемент, который не является списком/кортежем — TypeError. """
    a = []
    for i in mat:
        if not isinstance(i, (list, tuple)):
            raise TypeError()
        for j in i:
            if isinstance(j, (list, tuple)):  
                raise TypeError()
            a.append(j)
            
    return a
            

""" print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))
print(min_max([])) """
""" 
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0])) """

 
""" print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))   """
    
    
    
