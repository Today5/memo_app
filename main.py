from datetime import date
import json
import os

FILE_NAME = "memos.json"

# メモの読み込み
def load_memos():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("ファイルが破損しているため、メモを初期化します。")
    return []

# メモの保存
def save_memos(memos):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(memos, file, ensure_ascii=False, indent=4)
    except IOError:
        print("メモの保存に失敗しました。")

# メモ表示
def display_memo(memos):
    print("メモ一覧:")
    if not memos:
        print("メモが空です。")
    else:
        for i, entry in enumerate(memos, start=1):
            print(f"{i}, {entry['content']} - 日付: {entry['date']}")

# メモ入力
def input_memo(memos):
    while True:
        input_memo = input("メモを入力してください。(終了するには 'exit' と入力): ")
        if input_memo.lower() == "exit":
            print("終了します。")
            break
        now = date.today()
        memo_entry = {"content": input_memo, "date": str(now)}
        memos.append(memo_entry)
        save_memos(memos)
        print("メモが追加され、保存されました。")

# メモ削除
def delete_memo(memos):
    while True:
        display_memo(memos)
        index = input("削除したいメモの番号を入力してください (終了するには 'exit' と入力): ")
        if index.lower() == "exit":
            print("削除処理を終了します。")
            break
        if index.isdigit():
            del_index = int(index) - 1
            if 0 <= del_index < len(memos):
                del memos[del_index]
                save_memos(memos)
                print("メモを削除し、保存しました。")
            else:
                print("無効な番号です。もう一度試してください。")
        else:
            print("無効な入力です。数字を入力してください。")

# メモ検索
def search_memo(memos):
    if not memos:
        print("メモが空です。検索するメモがありません。")
        return
    while True:
        search = input("検索したい単語を入力してください (終了するには 'exit' と入力): ").strip()
        if search.lower() == "exit":
            print("検索を終了します。")
            break
        results = [memo for memo in memos if search.lower() in memo["content"].lower()]
        if results:
            print("\n該当するメモ:")
            for i, memo in enumerate(results, start=1):
                print(f"{i}. {memo['content']} - 日付: {memo['date']}")
        else:
            print("該当するメモはありません。")

# メイン関数
def main():
    memos = load_memos()
    while True:
        print("\nメモ帳アプリ")
        print("1: メモを追加する")
        print("2: メモを削除する")
        print("3: メモを検索する")
        print("4: メモを表示する")
        print("5: 終了する")

        index = input("実行したい機能を選択してください: ")
        if index == "1":
            input_memo(memos)
        elif index == "2":
            delete_memo(memos)
        elif index == "3":
            search_memo(memos)
        elif index == "4":
            display_memo(memos)
        elif index == "5":
            save_memos(memos)
            print("終了します。")
            break
        else:
            print("無効な選択です。もう一度選んでください。")

if __name__ == "__main__":
    main()