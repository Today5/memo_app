from datetime import date

memos = []

#リストを表示する
def display_memo(memos):
    print("メモ一覧:")
    for i, entry in enumerate(memos, start=1):
        print(f"{i}, {entry['content']} - 日付:{entry['date']}")
    while True:
        index = input("終了する場合はexitと入力してください").strip()
        if index.lower() != "exit":
            print("終了する場合はexitと入力してください")
        else:
            print("終了します。")
            break



#メモ入力を受け付ける
def input_memo(memos):
    while True:
        input_memo = input("メモを入力してください。(終了するにはexitと入力):")
        #今日の日付を変数に代入

        if input_memo.lower() == "exit":
            print("終了します。")
            break

        #今日の日付を辞書に格納
        now = date.today()
        memo_entry = {"content": input_memo, "date":str(now)}

        #メモリストに追加する
        memos.append(memo_entry)



#削除機能
def delete_memo(memos):
    while True:
        index = input("削除したいメモの番号を入力してください(終了する場合はexitと入力してください):")
        #終了処理を行うか判断する
        if index.lower() == "exit":
            print("削除処理を終了します。")
            break
        #数字かどうか判断し削除するindexを指定する
        if index.isdigit():
            del_index = int(index) - 1
            #有効なインデックスの範囲か確認する
            if 0 <= del_index < len(memos):
                del memos[del_index]
                if memos:
                    display_memo(memos)
                else:
                    print("メモが空です")
            else:
                print("無効な番号です。もう一度試してください")
        else:
            print("無効な入力です。数字を入力してください")

#検索機能
def search_memo(memos):
    if not memos:
        print("メモがからです。検索するメモがありません")
        return
    while True:
        search = input("検索したい単語を入力してください(終了する際はexitと入力):").strip()
        #exit が入力された場合
        if search.lower() == "exit":
            print("検索を終了します。")
            break

        #入力された値が存在するか確認する
        results = [memo for memo in memos if search.lower() in memo["content"].lower()]

        if results:
            print("\n該当するメモ")
            for i, memo in enumerate(results, start=1):
                print(f"{i}. {memo['content']} - 日付：{memo['date']}")
        else:
            print("該当するメモはありません。")

#UI表示を行う
def main():
        while True:
            print("\nメモ帳アプリ")
            print("1:メモを追加する")
            print("2:メモを削除する")
            print("3:メモを検索する")
            print("4:メモを表示する")
            print("5:終了する")

            index = input("実行したい機能を選択してください:")
            if index == "1":
                input_memo(memos)
            elif index == "2":
                delete_memo(memos)
            elif index == "3":
                search_memo(memos)
            elif index == "4":
                display_memo(memos)
            elif index == "5":
                print("終了します")
                break
            else:
                print("無効な選択です。もう一度選んでください")

if __name__ == "__main__":
    main()