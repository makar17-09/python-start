h=100
p=0
y=20
i=250
def collideRectRect (x, y, w, h, x2, y2, w2, h2):
  # работает правильно, даже если rectMode стоит CENTER
    if (x + w >= x2) and  (x <= x2 + w2) and  (y + h >= y2) and (y <= y2 + h2):
        return True
    else:
        return False
def setup():
    
      size(500,500)
def draw():
    global h,p,y,i
    a=loadImage("123.jpg")
    image(a,0,0,498,498)
    s=loadImage("12.jpg")
    image(s,h,p,20,20)
    f=loadImage("88.jpg")
    image(f,y,i,30,30)
    g=loadImage("3333.jpg")
    image(g,460,420,20,20)
    
    collide1=collideRectRect( y,i,30,30,h,p,20,20)
    if collide1:
        h=100
        p=0
    collide2=collideRectRect(460,420,20,20, h,p,20,20) 
    if collide2:
        textSize(50);
        fill(255,0,0)
        text(u"победа",250,250)
        
    if keyPressed:
        if key=="d":
            h=h+2
        if key=="a":
            h=h-2
        if key=="s":
            p=p+2
        if key=="w":
            p=p-2
    y=mouseX
    i=mouseY

               
            
        
