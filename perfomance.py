import random


def print_random():
    # 0～1億の範囲で100万個のランダムな整数リストを生成
    large_list = [random.randint(0, 10**8) for _ in range(10**6)]

    # large_list をセットに変換（検索を高速化）
    large_set = set(large_list)

    # 0～1億の範囲で100個のランダムな整数リストを生成
    small_list = [random.randint(0, 10**8) for _ in range(100)]

    # small_list の要素が large_set にすべて含まれているかをチェック
    if all(num in large_set for num in small_list):
        print("Found:", small_list)


# 実行部分
if __name__ == "__main__":
    print_random()
