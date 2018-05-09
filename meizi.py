import urllib.request
import urllib.parse
import re
import os
import lxml

#请求链接
def request_function(url):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	}
	request = urllib.request.Request(url=url,headers=headers)
	return request

#获取响应页面
def response_function(request):
	response = urllib.request.urlopen(request)
	return response.read().decode()

#下载图片
def get_image_function(response):
	#匹配图片链接
	pertten=re.compile(r"""<li><a href="(.*?)" target="_blank"><img width='236' height='354' class='lazy' alt='(.*?)' src='http://i.meizitu.net/pfiles/img/lazy.png' data-original='.*?' /></a><span><a href=".*?" target="_blank">.*?</a></span><span class="time">.*?</span><span class="view">.*?</span></li>""",re.S)
	ret = pertten.findall(response)
	a = 0
	for image_data in ret:
		download_image(image_data,a)    #调用下载图片函数

# 下载图片
def download_image(image_data,a):

	# for image_data in ret:
	# 	# download_image(image_data)
	# print(image_data[0])
	# request_image = request_function()
	# response = urllib.request.urlopen(request)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	}
	request = urllib.request.Request(url=image_data[0],headers=headers)
	response_image = urllib.request.urlopen(request)

	#有的图片下载会报错跳过错误
	try:
		read_response_image=response_image.read().decode()
		#匹配图片信息
		pertten=re.compile(r""".*?<span class='dots'>…</span><a href='.*?'><span>(.*?)</span></a><a href='.*?'><span>.*?</span></a>.*?""",re.S)
		ret=pertten.findall(read_response_image)
		# print(ret[0])
		dirpath = './meizitu'
		if not os.path.exists(dirpath):
			os.mkdir(dirpath)
		# print(ret[0])
		for i in range(1,int(ret[0])+1):
			image_path = image_data[0]+'/'+str(i)+'/'
			# print(image_path)
			headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
		'Referer':image_data[0]+'/'+str(i),
	}
			request1 = urllib.request.Request(url=image_path,headers=headers)
			DL_image = urllib.request.urlopen(request1)
			RR_image=DL_image.read().decode()
			pertten1 = re.compile(r"""<div class="main-image"><p><a href=".*?" ><img src="(.*?)" alt=".*?" /></a></p>.*?</div>""",re.S)

			ret=pertten1.findall(RR_image)
			print(ret)
			#防盗链需要referer
			headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
		'Referer':image_data[0]+'/'+str(i),
	}
			request2 = urllib.request.Request(url=ret[0],headers=headers)
			open_image = urllib.request.urlopen(request2)
			# print(open_image)
			filepath = 'C:/Users/dell-ip/Desktop/HTML/爬虫/test3/meizitu'+'/'+image_data[1]+str(i)+'.jpg'
			print(filepath)
			with open(filepath,'wb') as fp:
				fp.write(open_image.read())

	except:
		a+=1
		print(a)

def main():
	start=int(input('起始页码'))
	end = int(input('终止页码'))
	# start = 1
	# end = 2
	url='http://www.mzitu.com/page/{}/'
	for page in range(start,end+1):
		full_url = url.format(page)       #拼接路径
		request=request_function(full_url)     #请求链接
		response = response_function(request)    #获取响应
		get_image = get_image_function(response)   #获取图片



if __name__ == '__main__':
	main()