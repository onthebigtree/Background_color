import os

# 目录
image_dir = 'DB/bird_png'
png_files = [f for f in os.listdir(image_dir) if f.endswith('.png')]

# 按文件名排序
png_files.sort()

# 从1开始的编号
counter = 1

for filename in png_files:
    # 构造旧文件的完整路径
    old_file = os.path.join(image_dir, filename)
    
    # 构造临时文件名
    temp_file = os.path.join(image_dir, f'temp_{counter}.png')
    
    # 首先重命名文件为临时文件名
    os.rename(old_file, temp_file)
    print(f'Renamed {old_file} to {temp_file}')
    
    # 更新编号
    counter += 1

# 现在所有的文件都有了一个临时的文件名，我们可以安全地重命名它们为最终的文件名

# 重置编号
counter = 1

# 获取所有的临时文件
temp_files = [f for f in os.listdir(image_dir) if f.startswith('temp_')]

# 按文件名排序
temp_files.sort()

for filename in temp_files:
    # 构造旧文件（临时文件）的完整路径
    old_file = os.path.join(image_dir, filename)
    
    # 构造新文件名
    new_file = os.path.join(image_dir, f'{counter}.png')
    
    # 重命名文件
    os.rename(old_file, new_file)
    print(f'Renamed {old_file} to {new_file}')
    
    # 更新编号
    counter += 1
