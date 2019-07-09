import re
import urllib.request
import urllib
site="http://www.hurriyet.com.tr"
regex='<span class="news-title">(.+?)</span>'
comp= re.compile(regex)
htmlkod=urllib.urlopen(site).read()
titles=re.compile(regex)
htmlkod=urllib.urlopen(site).read()
titles=re.findall(comp,htmlkod)
i=1
for title in titles:
  print(str(i),title.decode("iso8859-9"))
  i+=1




  import socket

  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  server.bind((socket.gethostname(), 0))

  server.listen(5)

  print("{}:{} dinleniyor...".format(*server.getsockname()))

  while True:
    try:
      client, address = server.accept()
      print("{}:{} bağlandı".format(*address))
      print(client.recv(80))
      client.send("Merhaba !")
      client.close()
    except KeyboardInterrupt:
      break

  server.close()