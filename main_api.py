import qrcode
from PIL import Image, ImageDraw, ImageFont
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import StreamingResponse
from io import BytesIO

app = FastAPI()

def generate_qr_code(data, text=''):
    # 创建二维码对象
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    if text:
        img = img.convert("RGBA")
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("msyh.ttc", 20)
        except IOError:
            print("未找到指定的字体文件，使用默认字体。")
            font = ImageFont.load_default()
        
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = (img.width - text_width) // 2
        text_y = 10
        draw.text((text_x, text_y), text, font=font, fill='black')

    return img

@app.get("/generate_qr/")
async def generate_qr(token: str, data: str, text: str = Query(None)):
    # 在这里可以添加对 token 的验证逻辑
    if token != "your_secret_token":  # 替换为您自己的令牌验证逻辑
        raise HTTPException(status_code=403, detail="Invalid token")

    img = generate_qr_code(data, text)
    
    # 将图像保存到 BytesIO 对象中
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    return StreamingResponse(img_byte_arr, media_type="image/png")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)