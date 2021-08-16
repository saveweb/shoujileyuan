html_id = int(input("请输入开始的HTML_ID:"))
html_max = int(input("请输入结束的HTML_ID:"))
output_dir = './output-' + str(html_id) + '~' + str(html_max) + '/'
html_max = html_max +1

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
			jietu_raw = selector.css('.Qimgs')
			jietu_raw = jietu_raw.get()
			# 处理CSS选择
			pattern = re.compile('[a-zA-z]+://[^\s]*[jpg|JPG|png|PNG|gif|GIF|webp|WEBP]')
			jietu_list = pattern.findall(jietu_raw)
			# 正则输出链接 url_list
			output_dir_in = output_dir + str(html_id) + '/'
			if not os.path.exists(output_dir_in):
					os.makedirs(output_dir_in)#不存在文件夹就新建文件夹
			output_txt = output_dir_in + 'pic_url.txt'
			num = 0
			num_max = len(jietu_list)
			f = open(output_txt, "w")
			while num < num_max:
				url = jietu_list[num]#以字符串
				f.write(url + '\n')
				print(url + '\n')
				file_name = wget.download(url)
				if not os.path.isfile(output_dir_in + file_name):
					shutil.move(file_name, output_dir_in)
					print(file_name + '已下载!')
					num = num + 1
				else:
					os.remove(file_name)
					num = num + 1
			f.close()
			# 输出文件
			html_id = html_id + 1
		except:
			html_id = html_id + 2
	else:
		html_id = html_id + 1
