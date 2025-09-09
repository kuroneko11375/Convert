# DAT 文件編碼轉換工具

一個用於自動轉換 DAT 文件編碼格式的 Python 工具，特別適用於處理 EUC-TW 編碼的文件。

## 功能特色

- **圖形化檔案選擇**: 提供友善的檔案選擇對話框
- **雙模式操作**: 支援圖形介面選擇或自動搜尋模式
- **編碼轉換**: 將 EUC-TW 編碼轉換為 UTF-8 編碼
- **智慧檢測**: 自動搜尋當前目錄下的 DAT 文件
- **自動開啟**: 轉換完成後自動開啟結果文件
- **錯誤處理**: 完善的錯誤提示和處理機制
- **跨平台**: 使用內建的 iconv 工具確保轉換準確性

## 系統需求

- Python 3.x
- Windows 作業系統
- 內附的 iconv 執行檔及相關 DLL 文件

## 檔案結構

```
convert/
├── convert.py          # 主程式
├── LICENSE            # MIT 授權文件
├── README.md          # 說明文件
└── iconv/             # iconv 工具目錄
    ├── iconv.exe      # 編碼轉換執行檔
    ├── msys-2.0.dll   # 必要的動態連結庫
    ├── msys-iconv-2.dll
    └── msys-intl-8.dll
```

## 使用方法

程式提供兩種使用模式：

### 模式1: 圖形化檔案選擇 (推薦)

1. 執行程式：
```bash
python convert.py
```

2. 在選單中選擇 `1` 或直接按 Enter
3. 在彈出的檔案選擇視窗中選擇要轉換的 DAT 文件
4. 程式會自動轉換並顯示結果

### 模式2: 自動搜尋模式

1. 將 DAT 文件放置在與 `convert.py` 相同的目錄下
2. 執行程式並選擇 `2`
3. 程式會自動：
   - 搜尋目錄中的第一個 `.DAT` 文件
   - 將其從 EUC-TW 編碼轉換為 UTF-8 編碼
   - 生成同名的 `.txt` 文件
   - 自動開啟轉換後的文件

### 進階使用

程式也支援程式碼層級的自訂：

```python
from convert import convert_dat_to_text

# 自訂來源和目標編碼
convert_dat_to_text("specific_file.DAT", source_encoding='GB2312', target_encoding='UTF-8')

# 或者使用檔案選擇功能
from convert import select_file_and_convert
select_file_and_convert()
```

## 支援的編碼格式

- **來源編碼**: EUC-TW (預設), GB2312, Big5, ISO-8859-1 等
- **目標編碼**: UTF-8 (預設), UTF-16, ASCII 等

## 使用場景

這個工具特別適用於：

- 處理舊系統產生的 DAT 文件
- 轉換繁體中文編碼文件
- 批次處理編碼轉換作業
- 文件編碼標準化

## 範例

### 模式1: 使用檔案選擇視窗

```bash
python convert.py

# 輸出
DAT文件編碼轉換工具
==============================
1. 開啟檔案選擇視窗
2. 自動搜尋當前目錄的DAT文件
==============================
請選擇模式 (1/2，或直接按Enter使用模式1): 1

選擇的文件: C:/path/to/example_file.DAT
轉換成功: C:/path/to/example_file.DAT -> C:/path/to/example_file.txt
# 彈出成功訊息視窗並自動開啟 example_file.txt
```

### 模式2: 自動搜尋模式

假設當前目錄有一個名為 `example_file.DAT` 的文件：

```bash
python convert.py

# 選擇模式2後輸出
使用自動搜尋模式...
轉換成功: example_file.DAT -> example_file.txt
# 自動開啟 example_file.txt
```

## 錯誤處理

程式包含基本的錯誤處理機制：

- 如果找不到 DAT 文件，會顯示提示訊息
- 轉換過程中的錯誤會被靜默處理，避免程式崩潰
- 確保 iconv 工具路徑正確

## 注意事項

1. **檔案路徑**: 確保 `iconv/` 目錄與 `convert.py` 在同一層級
2. **權限問題**: 確保對目錄有讀寫權限
3. **編碼識別**: 如果來源文件不是 EUC-TW 編碼，請修改 `source_encoding` 參數
4. **檔案大小**: 大型文件轉換可能需要較長時間

## 開發歷史

```python
# 早期版本 - 手動指定文件
def convert_dat_to_text(dat_file, output_file, source_encoding='EUC-TW', target_encoding='UTF-8'):
    # 需要手動指定輸入和輸出文件名

# 現在版本 - 自動檢測
def convert_dat_to_text(source_encoding='EUC-TW', target_encoding='UTF-8'):
    # 自動檢測目錄中的 DAT 文件
```

## 授權資訊

本專案採用 MIT 授權條款，詳見 [LICENSE](LICENSE) 文件。


