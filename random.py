import random

# 資安情境選擇題列表，每個元素為一個包含問題和答案的字典
questions = [
    {
        "question": "以下哪個是常見的密碼攻擊方式？",
        "options": ["A. 雜湊攻擊", "B. 魚叉攻擊", "C. 中間人攻擊", "D. 網站劫持攻擊"],
        "answer": "A"
    },
    {
        "question": "以下哪個是一個安全的密碼？",
        "options": ["A. 123456", "B. mypassword", "C. P@ssw0rd", "D. abcdefg"],
        "answer": "C"
    },
    {
        "question": "以下哪個是一個常見的網路釣魚攻擊手法？",
        "options": ["A. 電子郵件攻擊", "B. 網站劫持攻擊", "C. 中間人攻擊", "D. 雜湊攻擊"],
        "answer": "A"
    },
    # 加入更多問題...
]

# 從問題列表中隨機選取指定數量的問題
num_questions = 5  # 要產生的問題數量
selected_questions = random.sample(questions, num_questions)

# 產生選擇題並輸出
for i, question in enumerate(selected_questions):
    # 輸出問題標題
    print(f"【{i+1}】{question['question']}（3 級難易度）")
    # 輸出選項
    for option in question['options']:
        print(option)
    # 輸出答案
    print(f"答案：{question['answer']}")
    print()
