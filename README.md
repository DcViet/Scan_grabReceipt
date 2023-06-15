# Scan_Receipt
**Doc - trich xuat thong tin hoa don ban hang GFood** 
# part 1
a***thư viện hỗ trợ: pytesseract***ư
\

Trích xuất thông tin từ ảnh chụp màn hình hóa đơn G**bFood
![Screenshot_2023-04-02_17-40-49](https://github.com/DcViet/Scan_grabReceipt/assets/111166640/b694820b-8cd8-4f53-92ee-aa3f30a5f284)

# part 2
- Sử dụng thiết bị chạy android 11 để **tự động** thao tác chụp ảnh màn hình.
- Mã nguồn scrcpy:
```
  https://github.com/Genymobile/scrcpy.git
```
  *Phương thức kết nối TCP/IP (wireless) : [https://github.com/Genymobile/scrcpy/pull/646](https://github.com/Genymobile/scrcpy/blob/master/doc/device.md)*
  
# 1 số bài viết tham khảo :
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
278: copy
279: paste
```


-https://github.com/mzlogin/awesome-adb/blob/master/README.en.md
-[https://viblo.asia/p/su-dung-adb-de-tao-mot-so-automation-tool-thu-vi-tren-dien-thoai-android-4dbZNGXglYM]
-[https://stackoverflow.com/questions/26586685/is-there-a-way-to-get-current-activitys-layout-and-views-via-adb]
