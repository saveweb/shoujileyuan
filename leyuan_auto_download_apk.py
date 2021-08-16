html_id = int(input("请输入开始的HTML_ID:"))
html_max = int(input("请输入结束的HTML_ID:"))
apk_dir = './apk-' + str(html_id) + '~' + str(html_max) + '/'
html_max = html_max + 1


import os
import re
import wget
import shutil

while html_id < html_max:
	html_add = './html/' + str(html_id) + '.html'
	isfile_ = os.path.isfile(html_add)
	print(html_add + ":" + str(isfile_))#正在处理的ID
	if isfile_ == True:
		with open(html_add,'r',encoding='utf-8') as f:
			raw_html = f.read()
		# 读取文件到变量 raw_html
		from parsel import Selector
		selector = Selector(raw_html)
		try:
			apk_raw = selector.css('.btn')
			url = apk_raw.xpath('.//@href').get()#href获取apk链接
			apk_dir_in = apk_dir + str(html_id) + '/'
			if not os.path.exists(apk_dir_in):
					os.makedirs(apk_dir_in)#不存在文件夹就新建文件夹
			print(url)
			file_name = wget.download(url)
			if not os.path.isfile(apk_dir_in + file_name):
				shutil.move(file_name, apk_dir_in)#存在即移动
			else:
				os.remove(file_name)#不存在即删除
			html_id = html_id + 1
		except:
			html_id = html_id + 1
	else:
		html_id = html_id + 1


#以下用于删除空文件夹
def del_emp_dir(path):
    for (root, dirs, files) in os.walk(path):
        for item in dirs:
            dir = os.path.join(root, item)
            try:
                os.rmdir(dir)  #os.rmdir() 方法用于删除指定路径的目录。仅当这文件夹是空的才可以, 否则, 抛出OSError。
                print(dir + ' removed!')
            except Exception as e:
                print('这真不是报错，文件已保留',e)
if __name__ == '__main__':
    dir = apk_dir
    del_emp_dir(dir)