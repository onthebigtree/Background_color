import os
import json

# 创建一个包含1-11000所有整数的集合
missing_numbers = set(range(1, 10794))

# 图像目录
image_dir = 'DB/bird_png'

# 遍历目录中的每一个图像
for filename in os.listdir(image_dir):
    if filename.endswith('.png'):  # 假设图像是PNG格式
        # 获取文件名（不包括扩展名），并转换为整数
        number = int(os.path.splitext(filename)[0])
        
        # 从集合中移除这个编号
        missing_numbers.discard(number)

# 将 missing_numbers 转换为列表
missing_numbers_list = sorted(list(missing_numbers))


# 将列表保存为 JSON 文件
with open('bg_missing_numbers.json', 'w') as f:
    json.dump(missing_numbers_list, f)


# 打印缺失的编号
for number in sorted(missing_numbers):
    print(number)



'''
# .json 文件的目录
json_dir = 'DB/metadata'  # 你需要替换为实际的目录

# 遍历缺失的编号
for number in sorted(missing_numbers):
    # 构造 .json 文件的路径
    json_file = os.path.join(json_dir, f'{number}.json')
    
    # 如果文件存在，删除它
    if os.path.exists(json_file):
        os.remove(json_file)
        print(f'Removed {json_file}')


# 另一个文件夹路径
another_dir = 'DB/bird_with_bg'

# 删除另一个文件夹里面对应编号的.png文件
for number in missing_numbers:
    file_to_remove = os.path.join(another_dir, f'{number}.png')
    if os.path.exists(file_to_remove):
        os.remove(file_to_remove)

'''