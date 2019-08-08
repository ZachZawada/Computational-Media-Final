'''

Name:               Zach Zawada
Current Date:       5/09/2019
Sources Consulted:  A book called Coding with Processing.py and 
                    and the chapter slides. 

By submitting this work, I attest that it is my 
original work and that i did not violate the
University of Mississippi academic policies 
set forth in the M book

ReadMe:  This program has bees that rotate around a flower.  The bees can also 
          increase rotation speed based on any incoming sound.  

'''
add_library("sound")

growP = 45    
growPit = 35
growPitH = 5     
shrink = 10
rayAngle = 0.0

cloudx = []
beeList = []

soundLevel = 0

spin = 0

def setup():
    global mic, vol
        
    size(1000, 1000)
    frameRate(60)
        
    mic = AudioIn(this,0)
    vol = Amplitude(this)
    
    #start the mic
    mic.start()
    
    #Connect the mic to the volume analyzer
    vol.input(mic)
    
    for i in range(3000):
        cloudx.append(random(-50000, 1000))    #clouds start off window from the left

def draw():
    global rayAngle, growP, growPit, growPitH, shrink, spin 
    global soundLevel
    global val

    background('#7DCAFC')   #Sky color for the background
    frameRate(60)
    #Dark green for ground
    rectMode(CORNER)
    noStroke()
    fill(15, 152, 62)
    rect(0,700, 1000,500)
    
    # takes a sound level and puts it to a variable
    # maps a partcular integer variable into a 2D range rather than a 1D
    soundLevel += map(vol.analyze(), 0, 1, 1, 50)
    
####################################################################################
    #Grass
####################################################################################
    fill(0)
    strokeWeight(1)
    for i in range(20, 400,8):
        line(i, 40, i+60, 80)
        
    
####################################################################################        
    #Flower
####################################################################################        

    # translate(mouseX,mouseY)
    #beginning of the flower scaling
    pushMatrix()
    scale(1.2)
            
####################################################################################
    #Flower stem
####################################################################################

    #light green
    
    translate(-100,-100)
    stroke(2, 229, 79)
    strokeWeight(8)
    line(500,500, 500,880)
    # translate(500, 600)
    
    
    ellipseMode(CENTER)

####################################################################################
    #Secondary Petals
####################################################################################
    
    pushMatrix()
    #increase the petal size and translate it
    scale(1.5)
    translate(-166,-350)
    strokeWeight(4)
    stroke(255,232,18,240)
    fill(222,204,0)
    ellipse(520,685, constrain(growP,45,250), constrain(growP,45,250))  #Top-Right
    ellipse(520,735, constrain(growP,45,250), constrain(growP,45,250))  #Bottom-Right
    ellipse(480,685, constrain(growP,45,250), constrain(growP,45,250))  #Top-Left
    ellipse(480,735, constrain(growP,45,250), constrain(growP,45,250))  #Bottom-Left
    
    # ellipse(520,685, 45,45)  #Top-Right
    # ellipse(520,735, 45,45)  #Bottom-Right
    # ellipse(480,685, 45,45)  #Top-Left
    # ellipse(480,735, 45,45)  #Bottom-Left

    
####################################################################################
    #Sun flower Petals
####################################################################################
    noStroke()
    #Yellow with some transparency
    fill(255, 232, 18)
    
    beginShape()
    vertex(575,710) #Right
    vertex(535,687)
    vertex(520,689)
    
    vertex(522,675) #Top
    vertex(500,635)
    vertex(477,675)
    vertex(479,689)
    
    vertex(465,687) #Left
    vertex(425,710)
    vertex(465,733)
    vertex(479,731)
    
    vertex(477,755) #Bottom
    vertex(500,785)
    vertex(522,755)
    vertex(520,731)
    vertex(535,733)
    endShape()
    
    
    # #Right Petal
    # arc(535,710, 75,45, HALF_PI,PI+HALF_PI,)
    # triangle(535,687, 575,710, 535,733)
    
    # #Left Petal
    # arc(465,710, 75,45, PI+HALF_PI, TWO_PI+HALF_PI)
    # triangle(465,687, 425,710, 465,733)
    
    # #Top Petal
    # arc(500,675, 45,75, 0, PI)
    # triangle(477,675, 500,635, 522,675)
    
    # #Bottom petal
    # arc(500,755, 45,75, PI,TWO_PI)
    # triangle(477,755, 500,785, 522,755)
    

    
    # fill(160, 82, 18)     #Dark Brown
    # ellipse(500,710, 35,35)
    # fill(193,100,12,200)  #Light Brown with Transparency
    # ellipse(500,700, 5,5)
    # ellipse(500,703, 5,5)
    # ellipse(500,705, 5,5)
    # ellipse(500,710, 5,5)
    # ellipse(497,700, 5,5)
    # ellipse(495,700, 5,5)
    # ellipse(490,700, 5,5)
    # ellipse(490,710, 5,5)
    # ellipse(490,705, 5,5)
    # ellipse(495,705, 5,5)
    # ellipse(487,710, 5,5)
    # ellipse(497,710, 5,5)
    # ellipse(503,697, 5,5)
    # ellipse(500,697, 5,5)
    # ellipse(497,697, 5,5)
    # popMatrix()
    
    fill(160, 82, 18)     #Dark Brown
    ellipse(500,710, constrain(growPit,35,250),constrain(growPit,35,250))
    fill(193,100,12,70)  #Light Brown with Transparency
    ellipse(500,700, constrain(growPitH,5,35.7), constrain(growPitH,5,35.7))
    ellipse(500,703, constrain(growPitH,5,35.7), constrain(growPitH,5,35.7))
    ellipse(500,705, constrain(growPitH,5,35.7), constrain(growPitH,5,35.7))
    ellipse(500,710, constrain(growPitH,5,35.7), constrain(growPitH,5,35.7))
    ellipse(497,700, constrain(growPitH,5,35.7), constrain(growPitH,5,35.7))
    ellipse(495,700, constrain(growPitH,5,35.7), constrain(growPitH,5,35.7))
    ellipse(490,700, constrain(growPitH,5,35.7), constrain(growPitH,5,35.7))
    ellipse(490,710, constrain(growPitH,5,35.7), constrain(growPitH,5,35.7))
    ellipse(490,705, constrain(growPitH,5,35.7), constrain(growPitH,5,35.7))
    ellipse(495,705, constrain(growPitH,5,35.7), constrain(growPitH,5,35.7))
    ellipse(487,710, constrain(growPitH,5,35.7), constrain(growPitH,5,35.7))
    ellipse(497,710, constrain(growPitH,5,35.7), constrain(growPitH,5,35.7))
    ellipse(503,697, constrain(growPitH,5,35.7), constrain(growPitH,5,35.7))
    ellipse(500,697, constrain(growPitH,5,35.7), constrain(growPitH,5,35.7))
    ellipse(497,697, constrain(growPitH,5,35.7), constrain(growPitH,5,35.7))
    popMatrix()
    
    popMatrix()
    
    
    
####################################################################################        
    #Sun
####################################################################################

    # pushMatrix()
    # #Sun-Rays
    # rectMode(RADIUS)
    # fill(255,253,196, 150)
    # rotate(rayAngle)
    # rect(0,-50, 2000,30) 
    # rect(0,100, 2000,30)
    # rect(0,200, 2000,30)
    # rayAngle += 0.025
    # popMatrix()
    
    fill(255, 250, 95) #Light-Yellow
    #ellipse(85, 100, 100,100)
    ellipse(0,0, 500,500)
    fill(255,251,173, 100)  #Light-Yellow with Transparency
    ellipse(0,0, 400,400)
    fill(255,251,173, 100)
    ellipse(0,0,345,345)
    ellipse(0,0,330,330)
    ellipse(0,0,315,315)
    ellipse(0,0,300,300)
    ellipse(0,0,285,285)
    ellipse(0,0,260,260)
    ellipse(0,0,245,245)
    

    
####################################################################################        
    #Clouds
####################################################################################        
   
    pushMatrix()
    fill(255,255,255, 80)
    for i in range(len(cloudx)):
        cloudx[i] += 0.5
        y = i * 0.35
        ellipse(cloudx[i], y*0.25, 75,25)
    popMatrix()
    
    
####################################################################################        
    #Bees
####################################################################################
    translate(480,530)
    
    pushMatrix()
    rotate(radians(soundLevel))
    # translate(40,40)
    # for i in range(35, width+ 40, 40):
    #     beeSpin(i, 110)
    beeSpin(50,50)
    beeSpin(125,10)
    beeSpin(0,-25)
      
    
    popMatrix()
    
    

def beeSpin(x, y):
    
    pushMatrix()
    # translate(500, 700)
    #wings
    fill(255)
    #stroke(255)
    noStroke()
    strokeWeight(1)
    ellipse(x-3, y-6, 12, 18)
    ellipse(x+8, y-6, 12, 18)
    # ellipse(397, 394, 12, 18)
    # ellipse(408, 394, 12, 18)
    
    #body in the center of the screen  
    stroke(0)
    fill(255, 255, 0)
    ellipse(x, y, 28, 18)
    # ellipse(400, 400, 28, 18)

    #eyes
    fill(0) 
    ellipse(x-2,y-2, 2,2)
    ellipse(x-7,y-2, 2,2)
    # ellipse(398,398, 2, 2) 
    # ellipse(393,398, 2, 2) 

    #brows 
    line(x-10,y-6, x-6,y-4)
    line(x-4,y-4, x+2,y-6)
    # line(390, 394, 394, 396)  
    # line(396, 396, 402, 394) 

    #stripe
    strokeWeight(5)
    line(x+4,y-7, x+4,y+7)
    # line(404, 393, 404, 407)
    popMatrix()                    
