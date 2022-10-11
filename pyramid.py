import turtle as tr 
import random 

def rectangle(p, l):
    for x_sisi in range(4): 
        if x_sisi % 2 == 0: 
            tr.forward(p)   
            tr.left(90)     
        else:               
            tr.forward(l)   
            tr.left(90)    
            
tr.speed(0)                  
tr.bgcolor('#008000')         
tr.colormode(255)             
tr.title("Candi Warna-Warni")

batu_bawah = int(tr.numinput("Input", "Jumlah batu bata pada lapisan paling bawah:", 1, minval=1, maxval=25))       
batu_atas = int(tr.numinput("Input", "Jumlah batu bata pada lapisan paling atas:", 1, minval=1, maxval=batu_bawah)) 
p_batu = int(tr.numinput("Input", "Panjang satu buah batu bata (piksel):", 1, minval=1, maxval=35))                
l_batu = int(tr.numinput("Input", "Lebar satu buah batu bata (piksel):", 1, minval=1, maxval=25))                   

length = -((batu_bawah * p_batu) / 2)                      
height = -(((batu_bawah - batu_atas + 1) * l_batu) / 2)    

tr.up()                  
tr.goto(length, height)  

count = 0 
for i in range(batu_bawah, batu_atas - 1, -1):
    x, y = tr.pos()
    tr.pd()
    for j in range(i):
        if (i == batu_bawah or i == batu_atas) or (j == 0 or j == i - 1): 
            tr.color("black", "#BC4A3C")
            tr.begin_fill()
        else: 
            r = random.randint(0,255)  
            g = random.randint(0,255)  
            b = random.randint(0,255)  
            while (r == 188 and g == 74 and b == 60): 
                r = random.randint(0,255)
                g = random.randint(0,255)
                b = random.randint(0,255)
            tr.color("black", (r, g, b)) 
            tr.begin_fill() 
        rectangle(p_batu, l_batu) 
        tr.end_fill() 
        tr.fd(p_batu) 
        count += 1 
    tr.up() 
    tr.goto(x + p_batu/2, y + l_batu) 

tr.goto(0, height - 50)
tr.pd()
tr.write(("\nCandi warna-warni dengan " + str(count) + " batu bata"), False, align="center", font= ('Calibri', 15, 'normal'))
tr.up()

tr.hideturtle()
tr.exitonclick()
