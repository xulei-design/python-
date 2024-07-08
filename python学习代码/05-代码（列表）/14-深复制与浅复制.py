import copy

# 浅复制
nums = [1, 2, 3, 4, 5, 6]
nums1 = nums  # 深拷贝/浅拷贝？ 都不是，是一个指向，是赋值

nums2 = nums.copy()  # 浅拷贝，两个内容一模一样，但不是同一个对象，不同指向

nums3 = copy.copy(nums)  # 和 nums.copy()功能一样，都是浅拷贝

# 深拷贝。只能使用copy模块实现、
words = ['hello', 'good', 'hi', [100, 200, 300], 'monkey', 'eyes']
# words 和 words1 都是浅拷贝
# 浅拷贝认为只拷贝了一层
# word1 = words.copy()

# 深拷贝得 words2
words2 = copy.deepcopy(words)
words[0] = '你好'
words[3][2] = 100
print(words2) #
# print(word1)

words[3][0] = 1
print(words)
# print(word1) # 浅拷贝只拷贝了一层，内列表是第二层
