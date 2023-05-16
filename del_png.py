import os

# 文件夹路径
folder_path = 'DB/bird_with_bg'  # 你需要替换为实际的路径

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 检查文件名是否以 '.png.png' 结尾
    if filename.endswith('.png.png'):
        # 去掉一个 '.png'
        new_filename = filename[:-4]
        
        # 构造旧文件和新文件的完整路径
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        
        # 重命名文件
        os.rename(old_file, new_file)
