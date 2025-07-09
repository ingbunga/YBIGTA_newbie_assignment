from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Callable


"""
TODO:
- SegmentTree 구현하기
"""


T = TypeVar("T")
U = TypeVar("U")


class SegmentTree(Generic[T, U]):
    # 구현하세요!
    def __init__(self, 
                 data: list[T], 
                 converter: Callable[[T], U], 
                 merger: Callable[[U, U], U], 
                 defaultValue: Callable[[], U],
                 update = True):
        '''
        segment tree 생성자

        - data: 대상 리스트
        - converter: 리스트 값을 트리의 노드 타입으로 바꾸는 함수
        - merger: 두 트리의 노드를 하나의 노드로 합치는 함수
        - defaultValue: 트리 노드의 기본 값을 생성하는 함수
        - update: 초기 업데이트 여부, 특이 케이스를 위한 변수
        '''
        self.data = data
        self.converter = converter
        self.merger = merger
        self.defaultValue = defaultValue

        size = 1
        while size < len(data):
            size <<= 1
        self.tree = [defaultValue() for _ in range(2*size)]
        self.tree_size = size

        if update:
            for i in range(len(data)):
                self.update(i, data[i])


    def update(self, idx: int, value: T):
        '''
        값 수정

        - idx: 수정하고자 하는 인덱스
        - value: 수정 후 값
        '''
        self.data[idx] = value
        target = self.tree_size + idx
        self.tree[target] = self.converter(value)
        while target > 1:
            target //= 2
            self.tree[target] = self.merger(self.tree[target*2], self.tree[target*2+1])


    def query(self, l: int, r: int):
        '''
        질의 함수, l~r 구간의 트리의 노드를 합쳐 반환.

        - l: 왼쪽 인덱스
        - r: 오른쪽 인덱스
        '''

        def tree_merge(l: int, r: int, idx: int, coverage: int):
            if r - l == coverage - 1:
                return self.tree[idx]
            
            result = self.defaultValue()
            half_coverage = coverage // 2
            div_point = idx * coverage - self.tree_size + half_coverage

            if div_point <= r:
                result = self.merger(result, tree_merge(max(l, div_point), r, 2*idx+1, half_coverage))
            if l <= div_point - 1:
                result = self.merger(result, tree_merge(l, min(r, div_point - 1), 2*idx, half_coverage))
            return result
        
        return tree_merge(l, r, 1, self.tree_size)


            






