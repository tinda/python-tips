
# 1. 交換值
from xml.etree.ElementTree import Element
import sys
x, y = 1, 2
print(x, y)
x, y = y, x
print(x, y)

# 2. 字符串列表合併為一個字符串
sentence_list = ["my", "name", "is", "George"]
sentence_string = " ".join(sentence_list)
print(sentence_string)

# 3. 將字符串拆分為子字符串列表
sentence_string = "my name is George"
sentence_string.split()
print(sentence_string)

# 4. 通過數字填充初始化列表
[0]*1000  # List of 1000 zeros
[8.2]*1000  # List of 1000 8.2's

# 5. 字典合併
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}

print(x)
print(y)
print(z)

# 6. 反轉字符串
name = "George"
name[::-1]

print(name[::-1])

# 7. 從函數返回多個值


def get_a_string():
    a = "George"
    b = "is"
    c = "cool"
    return a, b, c


sentence = get_a_string()
(a, b, c) = sentence


# 8. 列表解析式
a = [1, 2, 3]
# Create a new list by multiplying each element in a by 2
b = [num*2 for num in a]

# 9. 遍歷字典

m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for key, value in m.items():
    print('{0}: {1}'.format(key, value))

# 10. 同時遍歷列表的索引和值
m = ['a', 'b', 'c', 'd']
for index, value in enumerate(m):
    print('{0}: {1}'.format(index, value))

# 11. 初始化空容器
a_list = list()
a_dict = dict()
a_map = map()
a_set = set()

# 12. 刪除字符串兩端的無用字符
name = "  George "
name_2 = "George///"
name.strip()  # prints "George"
name_2.strip("/")  # prints "George"
# 13. 列表中出現最多的元素
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key=test.count))

# 14. 檢查對象的記憶體使用情況
x = 1
print(sys.getsizeof(x))

# 15. 將 dict 轉換為 XML


def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem
