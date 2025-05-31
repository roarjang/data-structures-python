import time

###  ─────────────────────────────────────────────
# Node 클래스 정의 (Linked List용)
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Node 클래스 정의 (Binary Tree용)
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

###  ─────────────────────────────────────────────
# 연결 리스트 생성
def create_linked_list(values):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 연결 리스트 출력
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end= " -> ")
        current = current.next
    print("None")

###  ─────────────────────────────────────────────
# 이진 트리 출력 (중첩 구조 시각화)
def print_tree(root, level=0):
    if root is not None:
        print_tree(root.right, level + 1)
        print('     ' * level + + f'-> {root.value}')

# 샘플 이진 트리 생성
def generate_sample_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root

###  ─────────────────────────────────────────────
# 성능 측정용 데코레이터
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} 실행 시간: {time.time() - start:.6f}초")
        return result
    return wrapper