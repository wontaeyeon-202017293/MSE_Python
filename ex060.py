# 평균은 리스트의 모든 값들을 합한 후 리스트에 포함된 원소의 개수로 나눠 구한다. 이때 리스트의 모든 값들의 합은 sum을 통해 구하고 리스트에 포함된 원소의 개수는 len를 통해 구한다.
nums = [1, 2, 3, 4, 5]
average = sum(nums) / len(nums)
print(average)