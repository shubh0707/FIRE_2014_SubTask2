import mechanize,re
from bs4 import BeautifulSoup
br1 = mechanize.Browser()
br1.set_proxies({'http':'172.16.1.22:3128'})
br1.set_handle_robots(False)
br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
f = open('movie_links.txt','r').read()
f = f.split('\n')
for i in range(846,len(f)):
	desc = f[i]
	link = desc.split('<-->')[0]
	name = desc.split('<-->')[1].replace('?','')
	string = br1.open(link,None).read()
	soup = BeautifulSoup(string.decode('utf-8', 'ignore'))
	dialogue_list = soup.find_all('div',attrs = {"class" : "dialogueBoxEnglishRight"})
	g = open(name+'.txt','w')
	for i in range(len(dialogue_list)):
		dialogue_list[i] = dialogue_list[i].string
		g.write(dialogue_list[i].replace('...','')+"\n")
	g.close()
	print(name)

	