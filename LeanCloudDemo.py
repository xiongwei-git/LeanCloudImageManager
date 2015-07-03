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
savePath = 'D://image//1-499//photo'
allPictureUrlFile = '1-499.txt'
errorPictureUrlFile = '1_499_error.txt'


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

def getOnePictureByPosition(position):
    query = Query(allPictures)
    query.equal_to('position', position)
    pictures = query.find()
    if len(pictures) > 0:
      return pictures[0]
    else:
      return None

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

def checkFileIsExit(position):
  imageurl = queryOneDataByPosition(position)
  print imageurl
  fileName = gGetFileName(imageurl)
  checkFile = savePath+fileName
  if os.path.exists(checkFile):
      message = 'OK, the  file "%s" exists.'
  else:
      message = 'Sorry, the  file "%s"  not exists.'
  print message % fileName

def checkFileIsExitAndRem(position):
  imageurl = queryOneDataByPosition(position)
  print imageurl
  fileName = gGetFileName(imageurl)
  checkFile = savePath+fileName
  if os.path.exists(checkFile):
      return ''
  else:
      errorFileInfo = str(num)+'--'+fileName
      return errorFileInfo
  


def changeServerFileName(position,newName):
  query = Query(allPictures)
  query.equal_to('position', position)
  pictures = query.find()
  pictureSelect =  pictures[0]
  pictureSelect.set('image_src', newName)
  pictureSelect.save()


'''
获得文件名称之前的url
'''
def getPreName(allUrl):
  index = allUrl.rfind('/')
  if index > 0:
    return allUrl[0:index+1]
  else:
    return ''

'''
获取文件类型后缀
'''
def getFileType(fileName):
  index = fileName.rfind('.')
  if index > 0:
    return fileName[index:len(fileName)]
  else:
    return '.jpg'


def getNewNameByPosition(position,oldName):
  prefix = '000_'
  if position > 99:
    prefix = str(position/100*100)+'_'
  return prefix+'20150703_00'+ str(position) + getFileType(oldName)

def renameLocalFileName(oldName,newName):
  oldFile = savePath +'//' + oldName
  if os.path.exists(oldFile):
    os.rename(os.path.join(savePath,oldName),os.path.join(savePath,newName))
    print 'the  file "%s" rename OK.' % oldName
    return True
  else:
    print 'the  file "%s" not exists' % oldName
    return False

  

#--------Main------------#
if __name__ == '__main__':
  print('''      *************************************
      **	  Welcome to Ted Python	  **
      **	 Created on  2015-06-25	  **
      **	   @author: Ted		   **
      *************************************''')

  '''
  修改文件名称
  '''
  query = Query(allPictures)
  for num in range(1,500):
      query.equal_to('position', num)
      pictures = query.find()
      if len(pictures) > 0:
        pictureSelect = pictures[0]
        imageurl = pictureSelect.get('image_src')
        if imageurl.find('00'+str(num)) > 0:
          print ''
        else:
            print imageurl
        # oldName = gGetFileName(imageurl)
        # newFileName = getNewNameByPosition(num,oldName)
        # newFileUrl = getPreName(imageurl) + newFileName
        # print newFileUrl
        # if renameLocalFileName(oldName,newFileName):
        #     pictureSelect.set('image_src', newFileUrl)
        #     pictureSelect.save()
        # else:
        #     print 'the server file change faild'
        





  # urlTest = queryOneDataByPosition(1)
  # print getPreName(urlTest)

  #renameLocalFileName('Test.jpg','Test1.jpg')


#////////////////////////////////////////////////#
  # errorFile=open(savePath + errorPictureUrlFile,'w+')
  # for num in range(1,500):
  #     noFileInfo = checkFileIsExitAndRem(num)
  #     if len(noFileInfo) > 0:
  #         errorFile.write(errorFileInfo)
  #         errorFile.write("\n")
  #     else:
  #         message = 'OK, the  file "%s" exists.'
  #         print message % str(num)
  # errorFile.close()
#////////////////////////////////////////////////#

  #checkFileIsExit(1)

  #changeServerFileName(290,'https://ununsplash.imgix.net/31/Traunsee-Toscana_2014-02-01.jpg')









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


# errorFile=open(savePath + errorPictureUrlFile,'w+')
# for num in range(69,70):
#   imageurl = queryOneDataByPosition(num)
#   #print("get url = "+ imageurl)
#   fileName = gGetFileName(imageurl)
#   checkFile = savePath+fileName
#   if os.path.exists(checkFile):
#       message = 'OK, the  file "%s" exists.'
#       print message % fileName
#   else:
#       errorFileInfo = str(num)+'--'+fileName
#       errorFile.write(errorFileInfo)
#       errorFile.write("\n")
#       print errorFileInfo
# errorFile.close()






# query = Query(allPictures)
# query.equal_to('position', 521)
# pictures = query.find()
# picture521 =  pictures[0]
# picture521.set('image_src', 'https://ununsplash.imgix.net/reserve/jiyO1PKSunXa5z1SVGBg_photo01_1.jpg')
# picture521.save()