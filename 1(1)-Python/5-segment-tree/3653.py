from lib import SegmentTree
import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


def main() -> None:
    # 구현하세요!
    for _ in range(int(input())):
        n, m = map(int, input().split())
        movies = list(map(int, input().split()))
        movie_to_idx = [0]+list(range(n, 0, -1))
        list_end = n + m

        seg_tree = SegmentTree([0] + [1]*n + [0]*m, lambda x: x, lambda x, y: x + y, lambda: 0)
        
        ptr = n + 1
        results = []

        for movie in movies:
            results.append(seg_tree.query(movie_to_idx[movie], list_end) - 1)
            seg_tree.update(movie_to_idx[movie], 0)
            seg_tree.update(ptr, 1)
            movie_to_idx[movie] = ptr
            ptr += 1

        print(' '.join(map(str, results)))


        


if __name__ == "__main__":
    main()