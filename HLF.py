from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

toolkitID = ""
name = "Kathir T"
roomNo = "V-428"
regNo = "121101007"
year = "III"
branch = "EIE"
section = "A"
studPhone = "9480173922"
studEmail = "kathir.thaniyarasu@gmail.com"
parentName = "M N Thaniyarasu"
addressLine1 = "G-30, New Town"
addressLine2 = "Bhadravathi"
addressLine3 = "Karnataka"
parentPhone = "9480828922"
PINcode = "577301"
leavePurpose = "Meetup in Chennai"
departDate = "08/03/2019"
departDay = "Friday"
departTime = "1:00 PM"
arriveDate = "11/03/2019"
arriveDay = "Monday"
arriveTime = "8:00 AM"
nights = "3"
days = "3"


img = Image.open("1700x2300.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("osr.ttf", 32)

if len(toolkitID) != 0:
	draw.text((1310, 60),"Toolkit ID: " + toolkitID,(0,0,0),font=font)
draw.text((493, 180),name,(0,0,0),font=font)
draw.text((336, 250),roomNo,(0,0,0),font=font)
draw.text((968, 250),regNo,(0,0,0),font=font)
draw.text((256, 295),year,(0,0,0),font=font)
draw.text((681, 295),branch,(0,0,0),font=font)
draw.text((1208, 295),section,(0,0,0),font=font)
draw.text((515, 360),studPhone,(0,0,0),font=font)
draw.text((310, 418),studEmail,(0,0,0),font=font)
draw.text((433, 540),parentName,(0,0,0),font=font)
draw.text((400, 620),addressLine1,(0,0,0),font=font)
draw.text((400, 665),addressLine2,(0,0,0),font=font)
draw.text((400, 710),addressLine3,(0,0,0),font=font)
draw.text((545, 862),parentPhone,(0,0,0),font=font)
draw.text((1260, 862),PINcode,(0,0,0),font=font)
draw.text((547, 925),leavePurpose,(0,0,0),font=font)
draw.text((430, 1280),departDate,(0,0,0),font=font)
draw.text((756, 1280),departDay,(0,0,0),font=font)
draw.text((970, 1280),departTime,(0,0,0),font=font)
draw.text((430, 1340),arriveDate,(0,0,0),font=font)
draw.text((756, 1340),arriveDay,(0,0,0),font=font)
draw.text((970, 1340),arriveTime,(0,0,0),font=font)
draw.text((1375, 1210),nights,(0,0,0),font=font)
draw.text((1342, 1270),days,(0,0,0),font=font)


img.save('LeaveForm (filled).jpg')

print("Done")