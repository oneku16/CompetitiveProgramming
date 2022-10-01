import qrcode

link='https://steamuserimages-a.akamaihd.net/ugc/789735785470197226/943B3F0E6784306E47301F905E0B3B605354F8E6/?imw=512&amp;imh=395&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true'
path='D:\\Programming\\CompetitiveProgramming\\chill\\test.png'



img = qrcode.make(link)	
img.save(path)