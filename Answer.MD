# 台科大資管 Python 考試作答區

---

## 基本資料

**學號：** B114099022
**系級：** 資管系大一  
**姓名：** 林文玄

---

## 一、 原始碼分析報告 (Static Analysis) (共8小題，每小題3分，總共24分)

### 1.1 變數與邏輯對照表

| 原始變數名稱 | 代表意義 (Business Logic) | 建議修正名稱 |
|---|---|---|
| Q1 l1 (in load_proc) | 代表載入程序的資料清單| 建議修正名稱為 data_list。| 
| Q2 d2 (in main) | 代表主函式中的日期資料| 建議修正名稱為 date_info|
| Q3 c_res (in check) |代表檢查結果|建議修正名稱為 check_result |

### 1.2 壞味道 (Code Smells) 診斷

請列出原程式碼中至少 5 個嚴重的設計問題，並說明為什麼不好：

- **Q1：** 缺乏清晰的變數命名，導致程式碼可讀性差。
- **Q2：** 函式過於冗長，應該拆分為更小的功能模組。
- **Q3：**過多的全域變數使用，增加了維護難度
- **Q4：**缺乏錯誤處理機制，可能導致程式在異常情況下崩潰。
- **Q5：**缺乏模組化設計，導致程式碼重複性高，難以重用與擴展。

---

## 二、 Vibe-Coding 協作紀錄 (共6小題，每小題3分，總共18分)

請記錄你如何引導 GitHub Copilot 進行重構。
重構的要求，請根據題目卷以及你發現的 Code Smells 來進行。

### 2.1 關鍵 Prompt 紀錄

請貼出你對 AI 下達過最有效的 3 個 Prompt：

```log
Prompt A： 
請將函式 `load_proc` 中的變數命名改為更具描述性的名稱，並確保符合 PEP 8 命名規範
Prompt B： 
請將主函式中的邏輯拆分為多個小函式，並確保每個函式只負責單一功能。
Prompt C：
請在程式中加入基本的錯誤處理機制，避免輸入錯誤導致程式崩潰。
```

### 2.2 AI 錯誤處理

1. AI 在撰寫過程中是否有出錯？（例如：漏寫了某個功能、語法錯誤）你是如何發現並請它修正的？
    AI 在重構過程中漏掉了檢查輸入資料格式的功能。
2. 發現的問題： (範例：AI 漏掉了 exit 時要印出分類統計的功能)
    執行程式時，輸入錯誤格式的資料導致程式崩潰。
3. 修正的對話： (範例：我告訴它「請在結束前迴圈遍歷 JSON 資料並計算分類總額」)
    我告訴它：「請在函式 check 中加入輸入格式檢查，若格式錯誤則回傳錯誤訊息。
---

## 三、 成果驗證與測試  (共2小題，每小題10分，總共20分)

確保你的 `modern_library.py` 功能正確。

### 3.1 測試結果驗證 (Terminal)

請貼上執行程式並輸入 show 後，顯示資料清單。(請從呼叫執行程式到結束程式完整的把操作對話複製到下框)

```log
=== 圖書管理系統 v1.0 ===
> add 深入淺出Python/978001/available
Success
> add 資料結構理論/978002/available
Success
> add 演算法實作/978003/available
Success
> add 重複測試書/978001/available
ISBN Exist
> borrow 978002
Updated
> show
書名: 深入淺出Python, ISBN: 978001, 狀態: available
書名: 資料結構理論, ISBN: 978002, 狀態: borrowed
書名: 演算法實作, ISBN: 978003, 狀態: available
> exit
系統關閉
PS C:\Users\pclab\Desktop\NTUST-0527-Final-master>
```

### 3.2 產出的資料檔案格式

請貼上重構後生成的 `books.json` 前幾行內容：

```json
[
  {
    "title": "XXX",
    "isbn": "XXX",
    "status": "XXX"
  }
]


深入淺出Python@@978001##available
資料結構理論@@978002##borrowed
演算法實作@@978003##available

```

---

## 四、 Git 提交紀錄 (Commit History)  (共2小題，總共13分)

### 4.1. 請執行 `git log --oneline` 並將 Commit 紀錄貼在此處，以證明你的開發流程(此小題6分)


```log
# fb02097 (HEAD -> master) v2


```

### 4.2. GitHub Repository 連結(此小題7分)
  
將專案推送到 GitHub (Public) 若提交到 Private 連結不給分。 請設定 Repository 名稱為 `學號-0527-Final` Ex: B11526748-0527-Final **請用 - 不是 _**

```log
# https://github.com/linw57844-dotcom/B11409022-0527-Final


```

希望這兩份 Markdown 格式能幫你省下不少排版時間！祝你的考試順利舉行！

最後請保留整份專案資料夾歐！
