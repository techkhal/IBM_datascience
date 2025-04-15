import os
import subprocess

def process_folder(folder_path, script_path, workers):
    """
    Duyệt qua tất cả các file TXT trong folder_path và gọi script cũ (script_path)
    cho mỗi file. Mỗi file sẽ được chạy riêng với tham số là đường dẫn file và số lượng worker.
    """
    # Lấy danh sách tất cả file có đuôi .txt trong folder
    txt_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.txt')]
    
    if not txt_files:
        print("Không tìm thấy file TXT nào trong folder.")
        return

    for txt_file in txt_files:
        input_file = os.path.join(folder_path, txt_file)
        print(f"Đang xử lý file: {input_file}")
        # Giả sử script cũ của bạn nhận tham số: input_file và số worker
        # Ví dụ: python domain_checker_selen.py input_file workers
        cmd = ["python", script_path, input_file, str(workers)]
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Lỗi khi xử lý file {input_file}: {e}")

if __name__ == "__main__":
    folder_path = input("Nhập đường dẫn folder chứa các file TXT: ").strip()
    script_path = input("Nhập đường dẫn script domain check cũ (vd: domain_checker_selen.py): ").strip()
    workers = input("Nhập số lượng worker (ví dụ: 4): ").strip()

    process_folder(folder_path, script_path, workers)
    print("Hoàn thành xử lý tất cả các file TXT trong folder.")
