import os.path  # 导入os.path模块

wordpath = r'E:/mr/test/pdf/list.docx'  # Word文档的路径
splitpath = os.path.splitext(wordpath)  # 分割Word文档的路径
pdfpath = splitpath[0] + '.pdf'  # 组合PDF文档的路径
print('生成的PDF文档路径：', pdfpath)
