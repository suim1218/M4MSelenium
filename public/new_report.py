import os

base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
result_dir = base_dir + "/report"
# print(result_dir)


lists = os.listdir(result_dir)
# print(lists)

# 重新按时间对目录下的文件进行排列
lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
# print('最新的文件为： ' + lists[-1])
file = os.path.join(result_dir, lists[-1])
print(file)
