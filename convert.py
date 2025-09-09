# import subprocess
# import os

# def convert_dat_to_text(dat_file, output_file, source_encoding='EUC-TW', target_encoding='UTF-8'):
#     try:
#         iconv_path = os.path.join(os.path.dirname(__file__), 'iconv.exe')  
#         with open(output_file, 'w', encoding=target_encoding) as output:
#             subprocess.run([iconv_path, '-c', '-f', source_encoding, '-t', target_encoding, dat_file], stdout=output, check=True)
#         print("轉換成功")
        
        
#         os.system(output_file)
#     except subprocess.CalledProcessError:
#         pass  

# # 使用示例
# dat_file = "example_file.DAT"
# output_file = "example_file.txt"
# convert_dat_to_text(dat_file, output_file)

import subprocess
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_dat_to_text(dat_file=None, source_encoding='EUC-TW', target_encoding='UTF-8'):
    """
    轉換DAT文件編碼
    
    Args:
        dat_file: 指定的DAT文件路徑，如果為None則自動搜尋
        source_encoding: 來源編碼格式
        target_encoding: 目標編碼格式
    """
    try:
        iconv_path = os.path.join(os.path.dirname(__file__), 'iconv', 'iconv.exe')
        
        if dat_file is None:
            # 獲取當前目錄下的所有文件列表
            files = os.listdir()
            # 選擇第一個 DAT 文件進行轉換
            dat_file = next((f for f in files if f.endswith('.DAT')), None)
        
        if dat_file and os.path.exists(dat_file):
            # 使用和輸入文件同名的輸出文件名
            output_file = os.path.splitext(dat_file)[0] + '.txt'
            with open(output_file, 'w', encoding=target_encoding) as output:
                subprocess.run([iconv_path, '-c', '-f', source_encoding, '-t', target_encoding, dat_file], stdout=output, check=True)
            print(f"轉換成功: {dat_file} -> {output_file}")
            os.system(f'"{output_file}"')  # 添加引號處理有空格的路徑
            return True
        else:
            print("未找到指定的 DAT 文件或當前目錄下沒有 DAT 文件")
            return False
    except subprocess.CalledProcessError as e:
        print(f"轉換過程中發生錯誤: {e}")
        return False
    except Exception as e:
        print(f"發生未預期的錯誤: {e}")
        return False

def select_file_and_convert():
    """
    開啟檔案選擇對話框並轉換選定的文件
    """
    # 建立隱藏的根視窗
    root = tk.Tk()
    root.withdraw()  # 隱藏主視窗
    
    # 開啟檔案選擇對話框
    file_path = filedialog.askopenfilename(
        title="選擇要轉換的DAT文件",
        filetypes=[
            ("DAT文件", "*.DAT"),
            ("所有文件", "*.*")
        ]
    )
    
    if file_path:
        # 顯示選擇的文件
        print(f"選擇的文件: {file_path}")
        
        # 執行轉換
        success = convert_dat_to_text(file_path)
        
        if success:
            messagebox.showinfo("轉換完成", f"文件轉換成功！\n\n來源文件: {os.path.basename(file_path)}\n輸出文件: {os.path.splitext(os.path.basename(file_path))[0]}.txt")
        else:
            messagebox.showerror("轉換失敗", "文件轉換過程中發生錯誤，請檢查文件格式和編碼設定。")
    else:
        print("未選擇任何文件")
    
    # 關閉根視窗
    root.destroy()

def main():
    """
    主程式：提供兩種使用模式
    """
    print("DAT文件編碼轉換工具")
    print("=" * 30)
    print("1. 開啟檔案選擇視窗")
    print("2. 自動搜尋當前目錄的DAT文件")
    print("=" * 30)
    
    try:
        choice = input("請選擇模式 (1/2，或直接按Enter使用模式1): ").strip()
        
        if choice == "2":
            # 模式2: 自動搜尋模式
            print("使用自動搜尋模式...")
            convert_dat_to_text()
        else:
            # 模式1: 檔案選擇模式 (預設)
            print("開啟檔案選擇視窗...")
            select_file_and_convert()
            
    except KeyboardInterrupt:
        print("\n程式已取消")
    except Exception as e:
        print(f"程式執行錯誤: {e}")

# 使用示例
if __name__ == "__main__":
    main()


# 範例文件: example_file.DAT
# 範例指令: iconv -f EUC-TW -t UTF-8 /path/to/example_file.DAT -o /path/to/example_file.txt
