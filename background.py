from PIL import Image
import os

# 图像目录
image_dir = '/path/to/your/images'

# 遍历目录中的每一个图像
for filename in os.listdir(image_dir):
    if filename.endswith('.png'):  # 假设图像是PNG格式
        image_path = os.path.join(image_dir, filename)
        
        # 加载图像
        image = Image.open(image_path)

        # 创建一个新的背景图像
        background = Image.new('RGB', image.size, (255, 0, 0)) # (255, 0, 0) 是红色

        # 合并图像和背景
        combined = Image.alpha_composite(background.convert('RGBA'), image.convert('RGBA'))

        # 保存新的图像，你可能想要改变保存的位置和文件名
        combined.save(f'/path/to/save/new_images/{filename}')
