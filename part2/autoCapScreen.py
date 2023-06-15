import subprocess
import pyautogui

# Hàm để chụp màn hình và lưu vào file ảnh
def capture_screen(file_path):
    subprocess.run(['adb', 'shell', 'screencap', '/sdcard/screenshot.png'])
    subprocess.run(['adb', 'pull', '/sdcard/screenshot.png', file_path])

# Hàm để click vào vị trí cụ thể trên màn hình
def click_position(x, y):
    subprocess.run(['adb', 'shell', 'input', 'tap', str(x), str(y)])

# Hàm để thực hiện kịch bản khi có đơn hàng mới
def process_new_order():
    # Lưu trạng thái màn hình hiện tại
    capture_screen('before.png')

    # Click vào đơn hàng
    click_position(500, 300)

    # Chụp màn hình và lưu vào file ảnh
    capture_screen('screenshot.png')

    # Thực hiện các thao tác khác trên đơn hàng (có thể tinh chỉnh phù hợp với những app khác)
    # ...

    # Quay trở lại trạng thái ban đầu
    click_position(700, 400)  # Ví dụ: Click vào nút "Quay lại"

    # Lưu trạng thái màn hình sau khi quay lại
    capture_screen('after.png')

# Thực hiện kịch bản khi có đơn hàng mới
process_new_order()
