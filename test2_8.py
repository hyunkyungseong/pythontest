import requests
url = 'http://bit.ly/2JnsHnT'
r = requests.get(url,stream=True).raw

# print(help(requests))

from PIL import Image 
img = Image.open(r)
img.show()
img.save('src.png')

print(img.get_format_mimetype)

BUF_SIZE = 1024
with open('src.png','rb') as sf , open('dst.png','wb') as df:   
    while True:
        data = sf.read(BUF_SIZE)
        if not data :
            break
        
        df.write(data)