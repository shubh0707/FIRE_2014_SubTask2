import mechanize,re
from bs4 import BeautifulSoup
br1 = mechanize.Browser()
br1.set_proxies({'http':'172.16.1.22:3128'})
br1.set_handle_robots(False)
br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
generic_url = 'http://www.filmyquotes.com/movies/list/'
L = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
f = open("movie_links.txt","w")
for i in L:
	alpha_movie_list_url = generic_url+i
	alpha_mov_list = br1.open(alpha_movie_list_url,None).read()
	soup = BeautifulSoup(alpha_mov_list.decode('utf-8', 'ignore'))
	movies_url_list = soup.find_all('li')
	movies_url_list = movies_url_list[8:]
	for l_tag in movies_url_list:
		movie_url = 'http://www.filmyquotes.com'+l_tag.a['href']
		movie_name = l_tag.string
		f.write(movie_url + "<-->" + movie_name + "\n")
	print(i)
f.close()
