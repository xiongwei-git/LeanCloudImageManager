#encoding:UTF-8
import leancloud
import json
import urllib
import os

#--------Basic------------#
leancloud.init('fdsm1bi25mz0fdkmbtg3k2vnc8z105b3wkkmylvuy8pso1t5', '6n82f5lljlmamtoxpu4b8jspufqg2lc1c9h7ztmpol176dl1')
from leancloud import Object
from leancloud import LeanCloudError
from leancloud import Query


#----------Constant----------------#
className = 'AllPictures'
saveClassName = 'PythonTestData'
allPictures = Object.extend(className)
savePath = 'D://image//1-499//photo//'
allPictureUrlFile = '1-499.txt'


#--------Method------------#

#--------Save Data---------#
def saveDataDemo():
    pythonData= Object.extend(saveClassName)
    python_data = pythonData()
    python_data.set('name', 'xiongwei')
    try:
        python_data.save()
        print('save success')
    except LeanCloudError, e:
        print e


def queryOneData(dataId):
    query = Query(allPictures)
    pictureItem = query.get(dataId)
    print pictureItem.get('image_src')

def queryOneDataByPosition(position):
    query = Query(allPictures)
    query.equal_to('position', position)
    pictures = query.find()
    if len(pictures) > 0:
      return pictures[0].get('image_src')
    return ""

#download#
def gDownloadWithFilename(url):
    print("start download img "+ url)
    try:
        fileName = gGetFileName(url)
        print("start download img name is"+ fileName)
        if url==None:print("url error")
        if url=="" :print("url error")
        webdata = urllib.urlopen(url)
        data = webdata.read()
        file=open(savePath + fileName,'wb+')
        file.write(data)
        file.close()
        print("download img success"+ url)
    except IOError:
        print("download img failed:"+ url)



def WriteDataToFile(data):
    try:
        file=open(savePath + allPictureUrlFile,'w+')
        file.write(data)
        file.write("\n")
        file.close()
        print("write img url success"+ data)
    except IOError:
        print("write img url error"+ data)
        
    
#---------------get name------------------#
def gGetFileName(url):
    if url==None: return None
    if url=="" : return ""
    arr=url.split("/")
    name = arr[len(arr)-1]
    return name
    # if name.endswith(".jpg"):return name
    # if name.endswith(".JPG"):return name.replace("JPG","jpg")
    # if name.endswith("jpeg"):return name.replace("jpeg","jpg")
    # if name.endswith("JPEG"):return name.replace("JPEG","jpg")
    # return name+".jpg"




#--------Main------------#
if __name__ == '__main__':
  print('''      *************************************
      **	  Welcome to Ted Python	  **
      **	 Created on  2015-06-25	  **
      **	   @author: Ted		   **
      *************************************''')
  #queryOneData('556ea641e4b005426cff3032')
  #queryOneDataByPosition(1)
# file=open(savePath + allPictureUrlFile,'w+')
# for num in range(1,500):
#   #print("get url at "+str(num))
#   imageurl = queryOneDataByPosition(num)
#   print("get url = "+ imageurl)
#   if len(imageurl) > 0:
#     file.write(imageurl)
#     file.write("\n")
#     #WriteDataToFile(imageurl)
#     #gDownloadWithFilename(imageurl)
#   else:
#     print(str(num)+" image url is null~~~~~~~~~~~~")
# file.close()

for num in range(1,2):
  imageurl = queryOneDataByPosition(num)
  print("get url = "+ imageurl)
  fileName = gGetFileName(imageurl)
  checkFile = savePath+fileName
  if os.path.exists(checkFile):
        message = 'OK, the  file "%s" exists.'
  else:
        message = 'Sorry, I cannot find the "%s" file.'
  print message % fileName