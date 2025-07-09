from lib import Trie
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