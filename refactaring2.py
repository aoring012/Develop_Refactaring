def repeat_string(input_str: str, horizontal: int, vertical: int) -> str:
    # 文字数のチェック
    if not (5 <= len(input_str) <= 10):
        raise ValueError("入力文字列は5文字以上10文字以下でなければなりません")

    # 文字の内容チェック (アルファベットのみ)
    if not input_str.isalpha():
        raise ValueError("入力文字列はアルファベットのみでなければなりません")

    # 横に繰り返し
    repeated_horizontal = input_str * horizontal

    # 縦に繰り返し
    result = "\n".join([repeated_horizontal for _ in range(vertical)])

    return result


# 動作確認用
if __name__ == "__main__":
    try:
        input_str = input("文字列を入力してください（5～10文字のアルファベットのみ）：")
        horizontal = int(input("横に繰り返す回数を入力してください："))
        vertical = int(input("縦に繰り返す回数を入力してください："))

        result = repeat_string(input_str, horizontal, vertical)
        print("結果:")
        print(result)
    except ValueError as e:
        print(f"エラー: {e}")
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")
