# Scan_Receipt
**Doc - trich xuat thong tin hoa don ban hang GFood** 
# part 1
***thư viện hỗ trợ: pytesseract***

Trích xuất thông tin từ ảnh chụp màn hình hóa đơn G**bFood
![Screenshot_2023-04-02_17-40-49](https://github.com/DcViet/Scan_grabReceipt/assets/111166640/b694820b-8cd8-4f53-92ee-aa3f30a5f284)

# part 2
- Sử dụng thiết bị chạy android 11 để **tự động** thao tác chụp ảnh màn hình.
- Mã nguồn scrcpy:
```
  https://github.com/Genymobile/scrcpy.git
```
  *Phương thức kết nối TCP/IP (wireless) : [https://github.com/Genymobile/scrcpy/pull/646](https://github.com/Genymobile/scrcpy/blob/master/doc/device.md)*
  
# Triển :
- Tài liệu chính thức của Adb (Android Debug Bridge)

![title](https://raw.githubusercontent.com/mzlogin/awesome-adb/master/assets/title.png)

lệnh ADB 

1. Cài đặt ứng dụng trên thiết bị Android:
```
adb install path/to/grab.apk
```

2. Gỡ bỏ ứng dụng khỏi thiết bị Android:
```
adb uninstall package-name
```

3. Chạy ứng dụng trên thiết bị Android:
```
adb shell am start -n com.grabtaxi.passenger/com.grabtaxi.passenger.activities.SplashActivity
```
4. Chụp ảnh màn hình 
```
adb shell screencap /namtran/screenshot.png
```
chèn thời gian hiện tại vào tên file ảnh:
```
adb shell screencap -p /namtran/screenshot_$(date +'%Y%m%d_%H%M%S').png
adb pull /sdcard/screenshot_$(date +'%Y%m%d_%H%M%S').png
```

Thao tác trong ứng dụng 

```
danh sách EventID :
3: Bấm nút HOME
4: Bấm nút quay lại
5: Gọi
6: Kết thúc cuộc gọi
24: Tăng âm lượng
25: Giảm âm lượng
26: Bật tắt điện thoại
27: Mở Camera
64: Mở browser
66: Enter
67: Backspace
207: mở danh bạ
220: tăng độ sáng
221: giảm độ sáng
277: cut
278: copy00
279: paste
```

Sử dụng thư viện **PyAutoGui**
```
PyAutoGUI là một thư viện Python mạnh mẽ cho phép tương tác với giao diện người dùng máy tính. Đây là một công cụ hữu ích để thực hiện tự động hóa các thao tác trên màn hình, bao gồm chụp màn hình, di chuyển chuột, nhấp chuột, gõ phím và thao tác khác.

đây là một số tính năng và phương thức quan trọng của PyAutoGUI:

1. Chụp màn hình: có thể sử dụng phương thức `screenshot()` để chụp một ảnh của toàn bộ màn hình hoặc `screenshot(region=(x, y, width, height))` để chụp một vùng cụ thể trên màn hình.

2. Di chuyển chuột: có thể di chuyển chuột đến một vị trí cụ thể trên màn hình bằng cách sử dụng phương thức `moveTo(x, y)` hoặc di chuyển tới một đối tượng trên màn hình bằng cách sử dụng phương thức `locateCenterOnScreen(image)` để xác định vị trí của hình ảnh trên màn hình.

3. Nhấp chuột: có thể thực hiện các thao tác nhấp chuột bằng cách sử dụng phương thức `click(x, y)` để nhấp chuột vào một vị trí cụ thể trên màn hình hoặc `click()` để nhấp chuột vào vị trí hiện tại của chuột.

4. Gõ phím: PyAutoGUI có phương thức `typewrite(text)` để gõ phím một đoạn văn bản cụ thể. có thể gõ các phím đặc biệt như `enter`, `tab`, `ctrl`, `alt`, v.v.

5. Delay và tương tác thời gian thực: sử dụng hàm `time.sleep(seconds)` để tạo độ trễ giữa các thao tác, giúp đảm bảo rằng các thao tác được thực hiện trong thời gian chính xác.

```
kết hợp cùng adb
 - sử dụng subprocess.run() để chạy các lệnh adb từ python 
```
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


```
> Một số thông tin tham khảo 
- [github](https://github.com/mzlogin/awesome-adb/blob/master/README.en.md)
- [viblo](https://viblo.asia/p/su-dung-adb-de-tao-mot-so-automation-tool-thu-vi-tren-dien-thoai-android-4dbZNGXglYM)
- [stackoverflow](https://stackoverflow.com/questions/26586685/is-there-a-way-to-get-current-activitys-layout-and-views-via-adb)
