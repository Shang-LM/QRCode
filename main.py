import qrcode

def generate_qr_code(data, file_path='qrcode.png'):
    # 创建二维码对象
    qr = qrcode.QRCode(
        version=1,               # 控制二维码的大小，范围是1到40，数值越大尺寸越大
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # 容错率，L:7%, M:15%, Q:25%, H:30%
        box_size=10,             # 控制每个小格子的像素大小
        border=4,                # 控制边框的宽度
    )
    # 添加数据到二维码
    qr.add_data(data)
    qr.make(fit=True)
    
    # 生成二维码图像
    img = qr.make_image(fill='black', back_color='white')
    
    # 保存二维码到指定路径
    img.save(file_path)
    print(f"QR Code saved as {file_path}")

# 示例用法
if __name__ == "__main__":
    # 输入内容
    data = input("请输入要生成二维码的文本或URL: ")
    file_path = input("请输入保存二维码的文件名（例如 qrcode.png）: ")
    generate_qr_code(data, file_path)
