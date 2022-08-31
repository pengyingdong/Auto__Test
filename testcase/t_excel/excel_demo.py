# 1.导入包，xlrd
import xlrd

# 2.常见workbook
book = xlrd.open_workbook("../../data/testdata.xls")
# 3.sheet对象
# 索引
sheet = book.sheet_by_index(0)
# 名称
# sheet = book.sheet_by_name("天气查询")
# 4.获取行数和列数
rows = sheet.nrows  # 行数
cols = sheet.ncols  # 列数
# 5.读取每行的内容
for r in range(rows):
    r_values = sheet.row_values(r)
    # print(r_values)
# 6.读取每列的内容
for c in range(cols):
    c_values = sheet.col_values(c)
    # print(c_values)

# 7.读取固定列的内容
print(sheet.cell(0, 0))
