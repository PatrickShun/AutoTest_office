import easyocr

# 创建对象
reader = easyocr.Reader(['ch_sim','en'])

# 读取图片
result = reader.readertext('test.jpg')

# 显示结果
result
