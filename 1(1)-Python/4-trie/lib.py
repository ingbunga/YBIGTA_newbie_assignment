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