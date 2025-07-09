from lib import SegmentTree
import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


def main() -> None:
    # 구현하세요!
    n = int(input())
    seg_tree = SegmentTree([0] * 1000001, lambda x: x, lambda x, y: x+y, lambda: 0, False)
    
    def best_candy(rank: int, idx = 1) -> int:
        if idx >= seg_tree.tree_size:
            return idx - seg_tree.tree_size
        
        left_amount = seg_tree.tree[2*idx]
        if left_amount >= rank:
            return best_candy(rank, 2*idx)
        else:
            return best_candy(rank - left_amount, 2*idx+1)

    for _ in range(n):
        query = list(map(int, input().split()))
        if query[0] == 2:
            _, taste, amount = query
            seg_tree.update(taste, seg_tree.data[taste] + amount)
        else:
            _, rank = query
            best_taste = best_candy(rank)
            seg_tree.update(best_taste, seg_tree.data[best_taste] - 1)
            print(best_taste)
            



if __name__ == "__main__":
    main()