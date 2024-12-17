import qrcode
from PIL import Image, ImageDraw, ImageFont

def generate_qr_code(data, text='', file_path='qrcode.png'):
    # 创建二维码对象
    qr = qrcode.QRCode(
        version=1,               # 控制二维码的大小
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # 容错率
        box_size=10,             # 控制每个小格子的像素大小
        border=4,                # 控制边框的宽度
    )
    # 添加数据到二维码
    qr.add_data(data)
    qr.make(fit=True)
    
    # 生成二维码图像
    img = qr.make_image(fill='black', back_color='white')

    # 如果用户输入了文字，则添加到二维码上
    if text:
        # 将二维码图像转换为PIL格式
        img = img.convert("RGBA")
        
        # 创建一个可以在上面绘图的对象
        draw = ImageDraw.Draw(img)
        
        # 设置字体和大小（确保使用支持中文的字体文件）
        try:
            # 替换为支持中文的字体文件路径，例如 "msyh.ttc" 或 "simhei.ttf"
            font = ImageFont.truetype("msyh.ttc", 20)  # 微软雅黑
        except IOError:
            print("未找到指定的字体文件，使用默认字体。")
            font = ImageFont.load_default()
        
        # 计算文字位置
        text_bbox = draw.textbbox((0, 0), text, font=font)  # 获取文本的边界框
        text_width = text_bbox[2] - text_bbox[0]  # 计算文本宽度
        text_height = text_bbox[3] - text_bbox[1]  # 计算文本高度
        text_x = (img.width - text_width) // 2
        text_y = 10  # 距离顶部10像素
        
        # 在二维码上绘制文字
        draw.text((text_x, text_y), text, font=font, fill='black')

    # 保存二维码到指定路径
    img.save(file_path)
    print(f"QR Code saved as {file_path}")

# 示例用法
if __name__ == "__main__":
    # 输入内容
    data = input("请输入要生成二维码的文本或URL: ")
    text = input("请输入要添加到二维码上的文字（留空则不添加）: ")
    file_path = input("请输入保存二维码的文件名（例如 qrcode.png）: ")
    generate_qr_code(data, text, file_path)