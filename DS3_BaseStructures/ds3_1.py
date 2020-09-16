

# https://blog.csdn.net/Darkman_EX/article/details/86486553

class Queue(object):

    def __init__(self):
        self.__item = []

    def is_empty(self):
        """判断队列是否为空"""
        return self.__item == []

    def in_queue(self, item):
        """进队"""
        self.__item.append(item)

    def out_queue(self):
        """出队"""
        return self.__item.pop(0)

    def size(self):
        """返回大小"""
        return self.__item.__len__()


if __name__ == '__main__':
    q = Queue()
    print(q.is_empty())

    q.in_queue(1)
    q.in_queue(2)
    q.in_queue(3)
    q.in_queue(4)
    print(q.is_empty())
    print(q.size())
    print(q.out_queue())
    print(q.out_queue())
    print(q.size())


# https://www.cnblogs.com/tianyb/p/10986769.html

class Stack(object):
    """栈"""
    def __init__(self):
        self.data = []

    def isEmpty(self):
        """判断是否空栈"""
        return self.data == []

    def peek(self):
        """返回栈顶元素"""
        return self.data[len(self.data) - 1]

    def size(self):
        """返回元素个数"""
        return len(self.data)

    def push(self, data):
        """入栈"""
        self.data.append(data)

    def pop(self):
        """出栈"""
        self.data.pop()

if __name__ == '__main__':
    # 以下为测试用例
    stack = Stack()
    print(stack.size())
    print("将0-10入栈")
    for i in range(11):
        stack.push(i)
    print("此时栈的大小为：", end=" ")
    print(stack.size())
    print("出栈3个")
    for i in range(3):
        stack.pop()
    print("此时栈的大小为：", end=" ")
    print(stack.size())
    # 栈菲空时输出栈顶元素，输出一个弹出一个
    while stack.isEmpty() is not True:
        print(stack.peek(), end=" ")
        stack.pop()


