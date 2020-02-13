from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from datetime import date,datetime

def makePDF(name,dob,hs,hsmark,cgpa,ph,email,li,we,sk1,sk2,sk3,im):
    img = Image.open("cvtemplate.jpg")
    photo = Image.open("prateekImg.jpeg")
    photo=photo.resize((130,130))
    img.paste(photo,(45,45))
   
    draw = ImageDraw.Draw(img)
    selectFont = ImageFont.truetype("Roboto-Black.ttf", size = 20)
    selectFont1 = ImageFont.truetype("Roboto-Black.ttf", size = 12)
    selectFont2 = ImageFont.truetype("Roboto-Black.ttf", size = 10)
    
    #for your refrence...
    # draw.text( (100,100), "X1", (0,0,0), font=selectFont1)
    # draw.text( (200,200), "X2", (0,0,0), font=selectFont1)
    # draw.text( (300,300), "X3", (0,0,0), font=selectFont1)
    # draw.text( (400,400), "X4", (0,0,0), font=selectFont1)
    
    draw.text( (190,100), str(name), (0,0,0), font=selectFont)
    draw.text( (50,215), str(dob), (0,0,0), font=selectFont1) 
    draw.text( (60,275), str(ph), (0,0,0), font=selectFont1)
    draw.text( (60,293), str(li), (0,0,0), font=selectFont1)
    draw.text( (55,255), str(email), (0,0,0), font=selectFont2)

    draw.text( (255,222), str(we), (0,0,0), font=selectFont1)
    draw.text( (235,355), str(sk1), (0,0,0), font=selectFont2)
    draw.text( (235,373), str(sk2), (0,0,0), font=selectFont2)
    draw.text( (235,391), str(sk3), (0,0,0), font=selectFont2)
    
    draw.text( (250,282), str(hs), (0,0,0), font=selectFont2)
    draw.text( (567,282), str(hsmark), (0,0,0), font=selectFont2)
    draw.text( (567,312), str(cgpa), (0,0,0), font=selectFont2)
    draw.text( (250,312), str("SRMIST"), (0,0,0), font=selectFont2)
    # (x,y) is the starting position for the draw object
    # text is the text to be entered
    # (r,g,b) represents the color eg (255,0,0) is Red
    # font is used to specify the Font object

    img.save( 'certi.pdf', "PDF", resolution=100.0)
    img.show()


if __name__=='__main__':
    makePDF("Prateek","09-19-1999","Kendriya Vidyalaya","99%","10.0","7807324699","kaistha.prateek03@gmail.com","li","we","sk1","sk2","sk3")
