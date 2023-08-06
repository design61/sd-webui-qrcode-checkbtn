# sd-webui-qrcode-checkbtn
这是一个针对Stable Diffusion web UI开发的一个二维码检测功能，能让你快速检查生成的图片二维码时候可以识别，免去手机扫码

## 效果展示
1. 无图状态
<img alt="Screenshot" src="https://github.com/design61/sd-webui-qrcode-checkbtn/blob/main/image/1.gif">

2. 识别成功
<img alt="Screenshot" src="https://github.com/design61/sd-webui-qrcode-checkbtn/blob/main/image/3.gif">

3. 识别失败
<img alt="Screenshot" src="https://github.com/design61/sd-webui-qrcode-checkbtn/blob/main/image/2.gif">

## 安装方法
1. 打开 `扩展` 选项卡.
2. 打开 `从网址安装` 选项卡.
3. 在 `扩展的 git 仓库网址` 输入 `https://github.com/design61/sd-webui-qrcode-checkbtn.git`.
4. 点击 `安装` 按钮.
5. 等待安装，直到出现 `Use Installed tab to restart` 的提示.
6. 重启你的web UI.

## 功能记录
2023.8.6
1. 支持t2i
2. 支持i2i

## 说明:
1. 解码方案使用的是openCV.js，和微信扫码使用的解码方案很接近
2. 从leidenglai/opencv-js-qrcode移植并重写，非常感谢 @leidenglai 的工作和研究。
