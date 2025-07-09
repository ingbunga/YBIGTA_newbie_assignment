from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push 구현하기
- (필요할 경우) Trie에 추가 method 구현하기
"""


T = TypeVar("T")


@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None
    children: list[int] = field(default_factory=lambda: [])
    is_end: bool = False


class Trie(list[TrieNode[T]]):
    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))

    def push(self, seq: Iterable[T]) -> None:
        """
        action: trie에 seq을 저장하기
        """
        # 구현하세요!
        tree_ptr = 0

        for value in seq:
            index = self.find_element_idx(self[tree_ptr].children, value)
            if index is not None:
                tree_ptr = index
            else:
                self.append(TrieNode(body=value))
                pos = len(self) - 1
                self[tree_ptr].children.append(pos)
                tree_ptr = pos
        
        if tree_ptr:
            self[tree_ptr].is_end = True
            

    # 구현하세요!
    def find_element_idx(self, children: list[int], element: T) -> Optional[int]:
        for i in range(len(children)):
            if self[children[i]].body == element:
                return children[i]
        return None


import sys


"""
TODO:
- 일단 lib.py의 Trie Class부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다...
"""


def main() -> None:
    # 구현하세요!
    trie: Trie = Trie()
    for _ in range(int(input())):
        trie.push(map(ord, input()))

    MOD = 1000000007

    factorial = [1, 1, 2]
    for n in range(3, 30):
        factorial.append((factorial[-1] * n) % MOD)

    stack = [0]
    result: dict[int, int] = {}

    # def get_number_of_cases(ptr: int):
    #     node = trie[ptr]
    #     y = factorial[len(node.children) + node.is_end]
    #     for child in node.children:
    #         y = (y * get_number_of_cases(child)) % MOD
    #     return y
    # 위 주석 처리된 재귀함수와 같은 동작을 하는 반복문
    while stack:
        ptr = stack[-1]
        node = trie[ptr]
        y = factorial[len(node.children) + node.is_end]

        child_not_calculated = False
        for child in node.children:
            if child not in result:
                stack.append(child)
                child_not_calculated = True
        
        if child_not_calculated:
            continue
        else:
            for child in node.children:
                y = (y * result[child]) % MOD
            result[ptr] = y
            stack.pop()

    print(result[0])


if __name__ == "__main__":
    main()