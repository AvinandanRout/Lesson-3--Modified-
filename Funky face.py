from turtle import *


class Face:


    def _init_(self. xpos, ypos):
        self.size = 98
        self.coord = (xpos, ypos)

        self.noseSize = 'small'


        def setSize(self, radius):
            self.size = radius


            def draw(self):
                self.goHome()
                pensize(3)
                speed(0)
                self.drawOutline()
                self.deawEye(135)
                self.DrawEye(45)
                self.deawMouth()
                self.drawNose()
                pensize(5)


#------------------------------------------------
#  Functions that are called from wth the class
#------------------------------------------------



    #  After drawing each part, turtle position
    # returns to centre. parts can be drawn in any order
    def goHome(self):
        penup()
        goto(self.coord)


        setheading(0)


def drawOutline(self):
    penup()
    # move turtle pen in forward direction
    forward(self.size)
    left(90)
    # drawa circle of given radius
    pendown()
    circle(self.size)
    # return  back to centre
    self.goHome()


    def drawEye(self, turn):
        penup()
        # turn turtle pen to given angle
        left(turn)
        # move turtle pen in forward direction
        forward(self.size / 2)
        
        def drawMouth(self):
            penup()
            # turn turtle pen to given angle
            right(135)
            # move turtle pen in forward direction
            forward(self.size/1.7)
            left(90)
            pendown()
            #drawa circle of given radius
            #but till given extent only
            circle(self.size/1.7,98)
            self.goHome()


            def drawNose(self):
                if self.noseSize == 'large' :
                    dot(self.size/2, "grey")
                elif self.noseSize == 'small' :
                    dot(self.size/6, "grey")
                else :
                    dot(self.size/4, "grey")
                    self.goHome()



                    # start of drawing code
                    # --------------------


                    f1 = Face(0, 0)
                    1.draw()


                    showturtle()
                    done()