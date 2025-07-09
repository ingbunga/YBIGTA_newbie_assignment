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
- 일단 Trie부터 구현하기
- count 구현하기
- main 구현하기
"""


def count(trie: Trie, query_seq: str) -> int:
    """
    trie - 이름 그대로 trie
    query_seq - 단어 ("hello", "goodbye", "structures" 등)

    returns: query_seq의 단어를 입력하기 위해 버튼을 눌러야 하는 횟수
    """
    pointer = 0
    cnt = 0

    # children 에서 element를 body로 가진 index를 찾고 반환하는 함수
    for element in query_seq:
        if len(trie[pointer].children) > 1 or trie[pointer].is_end:
            cnt += 1

        new_index = trie.find_element_idx(trie[pointer].children, element) # 구현하세요!

        pointer = new_index

    return cnt + int(len(trie[0].children) == 1)


def main() -> None:
    lines: list[str] = sys.stdin.readlines()
    ptr = 0
    
    while ptr < len(lines):
        n = int(lines[ptr])
        ptr += 1
        words = [lines[i].rstrip() for i in range(ptr, ptr+n)]
        ptr += n

        trie: Trie = Trie()

        for word in words:
            trie.push(word)

        counts = [count(trie, word) for word in words]
        print(f'{sum(counts)/len(counts):.2f}')
    

if __name__ == "__main__":
    main()