class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None

    # 新增節點 (Push)
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"新增節點: {data}")

    # 刪除節點 (Pop)
    def pop(self):
        if self.top is None:
            print("堆疊裡為空,無法POP.")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        print(f"拋出的節點: {popped_data}")
        return popped_data

    # 查看堆疊 (Display)
    def display(self):
        current = self.top
        print("堆疊裡從頂至底部為:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    stack = LinkedStack()
    
    # 嘗試從空堆疊中刪除節點
    print("嘗試從空堆疊中刪除節點:")
    stack.pop()
    print()
    #分行好進行分類
    
    # 新增節點
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    
    # 移除節點
    stack.pop()
    stack.display()
    
    # 清空堆疊後再次測試
    stack.pop()
    stack.pop()
    stack.pop()