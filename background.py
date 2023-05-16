from PIL import Image
import os
import random

# 颜色列表，颜色值应为 RGB 格式
colors = [
    (255, 204, 219),  # ffccdb
    (209, 209, 209),  # d1d1d1
    (188, 180, 235),  # bcb4eb
    (195, 210, 239),  # c3d2ef
    (184, 221, 229),  # b8dde5
    (225, 158, 236),  # e19eec
    (190, 229, 184),  # bee5b8
]

# 图像目录
image_dir = 'DB/bird_png'

# 遍历目录中的每一个图像
for filename in os.listdir(image_dir):
    if filename.endswith('.png'):  
        image_path = os.path.join(image_dir, filename)
        
        # 加载图像
        image = Image.open(image_path)

        # 随机选择一个颜色作为背景
        background_color = random.choice(colors)

        # 创建一个新的背景图像
        background = Image.new('RGB', image.size, background_color)

        # 合并图像和背景
        combined = Image.alpha_composite(background.convert('RGBA'), image.convert('RGBA'))

        # 保存新的图像，你可能想要改变保存的位置和文件名
        combined.save(f'DB/bird_with_bg/{filename}')
