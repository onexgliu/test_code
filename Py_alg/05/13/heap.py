''''
函数名称：heapify
功能：调整列表中的元素并保证以i为父结点的堆，并保证i是最大值
参数说明：heap：表示堆
          heap_len：表示堆的长度
          i：表示父结点的位置
'''


def heapify(heap, heap_len, i):
    '''
    给定某个结点的下标i，这个结点的父节点、左子结点、右子结点的下标都可以被计算出来。
    父结点：(i-1)//2
    左子结点：2*i + 1
    右子结点：2*i + 2  即：左子节点 + 1
    '''
    left = 2 * i + 1  # 左子结点位置
    right = 2 * i + 2  # 右子结点位置
    larger = i  # 每次最大值赋给变量larger
    if left < heap_len and heap[larger] < heap[left]:  # 左结点位置小于堆长度同时堆的最大值小于左子结点的值
        larger = left  # 此时将左结点位置给larger
    if right < heap_len and heap[larger] < heap[right]:  # 右结点位置小于堆长度同时堆的最大值小于右子结点的值
        larger = right  # 此时将右结点位置给larger
    if larger != i:  # 如果做了堆调整则larger的值等于左节点或者右节点的值
        heap[larger], heap[i] = heap[i], heap[larger]  # 这个时候做堆调整操作
        # 递归对各分支做调整
        heapify(heap, heap_len, larger)


def build_heap(heap):  # 构造一个堆，将堆中所有数据重新排序
    heap_len = len(heap)  # heapSize是堆的长度
    for i in range((heap_len - 2) // 2, -1, -1):  # 自底向上建堆
        heapify(heap, heap_len, i)


def heap_sort(heap):  # 将根节点取出与最后一位做对调，对前面len-1个节点继续进行堆调整过程。
    build_heap(heap)  # 调用函数创建堆
    # 调整后列表的第一个元素就是这个列表中最大的元素，将其与最后一个元素交换，然后将剩余的列表再递归的调整为最大堆
    for i in range(len(heap) - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heapify(heap, i, 0)


data = [96, 54, 88, 5, 10, 12]
print("原始数据为：")
for k in range(6):  # 遍历原有数据
    print('%4d' % data[k], end='')  # 输出结果
print('\n---------------------------')
print("排序之后的结果为：")
heap_sort(data)
for k in range(6):  # 遍历排序后数据
    print('%4d' % data[k], end='')  # 输出结果
