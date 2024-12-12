def solution(numbers, direction):
    answer = [] 
    # 방법1
    #answer = [0]*len(numbers)

    # for idx, num in enumerate(numbers):
    #     i = (idx + direction + len(numbers)) % len(numbers)
    #     answer[i] = numbers[idx]
  
    # 방법 2
    if direction > 0:
        sliced_list1 = numbers[:(len(numbers)-direction)]
        sliced_list2 = numbers[(len(numbers) - direction):]
        answer = sliced_list2 + sliced_list1
    else:
        direction += len(numbers)
        sliced_list1 = numbers[:(len(numbers)-direction)]
        sliced_list2 = numbers[(len(numbers) - direction):]
        answer = sliced_list2 + sliced_list1
    return answer
    
