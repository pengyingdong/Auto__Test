import yaml
from utils.YamlUtil import YamlReader

# # 导入yaml包
#
# with open("./data.yml", "r", encoding="utf8") as f:
#     # 打开文件
#     r = yaml.safe_load(f)
#     # 使用yaml读取文件
#     print(r)
# # 输入这个文件内容

# with open("./data.yml", "r", encoding="utf8") as f:
#     # 打开文件
#     r = yaml.safe_load_all(f)
#     # 使用yaml读取多个文档
#     for i in r:
#         print(i)
#     # 循环(遍历)打印
res = YamlReader("./data.yml").data_all()
print(res)
