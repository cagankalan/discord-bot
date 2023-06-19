import pymongo
import gridfs
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection["dark_humor"]
col = db['meme']

fs = gridfs.GridFS(db)

image = col.find_one({"name":"myTestSet"})['images'][0]

gOut = fs.get(image['imageID'])

img = np.frombuffer(gOut.read(), dtype=np.uint8)

img = np.reshape(img, image['shape'])

#IMAGE SHOWLAMAYA YARIYOR
plt.imshow(img, interpolation='nearest')
print("type of plt is : ",type(plt))
plt.show()

"""
img = cv2.imread('1.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print("type of img is : ",type(img))

imageString = img.tostring()
imgID = fs.put(imageString, encoding = "utf-8")

meta = {
    'name': 'myTestSet',
    'images': [
        {
            'imageID': imgID,
            'shape': img.shape,
            'dtype': str(img.dtype)
        }
    ]
}

col.insert_one(meta)

"""
"""
# Show the image data in a subplot
fig, ax = plt.subplots(1, 5)

for a in ax:
    a.imshow(img, interpolation='none')
# Show the figure on the screen
fig.show()

fs = gridfs.GridFS(db)

stored = fs.put(thedata, filename="testimage")

outputdata = fs.get(stored).read()

outputfilename = "/Users/cagankalan/development/discord-bot/hahahayoucantkillme/deneme.jpeg"
output = open(outputfilename,"w")
output.write(outputdata)

output.close()
"""

"""
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["dark_humor"]

img = Image.open("1.jpeg")
mycol = mydb['memes']

fs = GridFS(mydb)

stored = fs.put(img)
"""