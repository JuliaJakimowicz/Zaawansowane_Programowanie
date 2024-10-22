def merge_and_process_lists(list1: list, list2: list) -> list:
    combined_list = list(set(list1 + list2))
    result_list = [x ** 3 for x in combined_list]
    return result_list

list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
result = merge_and_process_lists(list_a, list_b)
print(result)
