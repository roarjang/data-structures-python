import sys
import os

# 현재 파일 기준으로 상위 디렉토리로 이동 후, etc 폴더 경로 추가
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
etc_dir = os.path.join(parent_dir, 'etc')

sys.path.append(etc_dir)

from helper_functions import ListNode, create_linked_list, print_linked_list

head = create_linked_list([1, 2, 3, 4])
print_linked_list(head)