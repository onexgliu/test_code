class HashTable:# 创建哈希表
    def __init__(self):
        self.size = 11# 哈希表长度
        self.throw = [None] * self.size# 哈希表数据键初始化
        self.data = [None] * self.size# 哈希表数据值初始化

    # 假定最终将有一个空槽，除非 key 已经存在于  self. throw中。 它计算原始
    # 哈希值，如果该槽不为空，则迭代 rehash 函数，直到出现空槽。如果非空槽已经包含 key，
    # 则旧数据值将替换为新数据值。
    def put(self, key, value):#输出键值
        hashvalue = self.hashfunction(key, len(self.throw))#创建哈希值
        if self.throw[hashvalue] is None:
            self.throw[hashvalue] = key# 将key值给哈希表的throw
            self.data[hashvalue] = value# 将value值给哈希表的data
        else:
            if self.throw[hashvalue] == key:
                self.data[hashvalue] = value

            else:
                nextslot = self.rehash(hashvalue, len(self.throw))
                while self.throw[nextslot] is not None and self.throw[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.throw))

                if self.throw[nextslot] is None:
                    self.throw[nextslot] = key
                    self.data[nextslot] = value
                else:
                    self.data[nextslot] = value

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def hashfunction(self, key, size):
        return key % size

    # 从计算初始哈希值开始。如果值不在初始槽中，则 rehash 用
    # 于定位下一个可能的位置。
    def get(self, key):
        startslot = self.hashfunction(key, len(self.throw))
        data = None
        found = False
        stop = False
        pos = startslot
        while pos is not None and not found and not stop:
            if self.throw[pos] == key:
                found = True
                data = self.data[pos]
            else:
                pos = self.rehash(pos, len(self.throw))
                # 回到了原点，表示找遍了没有找到
                if pos == startslot:
                    stop = True
        return data

    # 重载载 __getitem__ 和 __setitem__ 方法以允许使用 [] 访问
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key, value)



H = HashTable()# 创建哈希表
H[16] = "红"# 给哈希表赋值
H[28] = "橙"
H[32] = "黄"
H[14] = "绿"
H[56] = "青"
H[36] = "蓝"
H[71] = "紫"


print("key的数据是：",H.throw)# 输出键key
print("value的数据是：",H.data)# 输出值value
print("结果是:",H[28])# 根据key=28查value
print("结果是:",H[71])# 根据key=71查value
print("结果是:",H[93])# 根据key=93查value
