from math import sqrt



class point():

    def __init__(self,x=0,y=0):
        self.x=x 
        self.y=y 

    def move_to(self,x,y):
        """
        docstring
        """
        self.x=x 
        self.y=y

    def move_by(self,x,y):
        """
        docstring
        """
        self.x +=x
        self.y +=y
     

    def distance(self,other):
        """
        docstring
        """
        dx=self.x-other.x
        dy=self.y-other.y
        return sqrt(dx**2+dy**2)
        
    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))
def main():
    """
    docstring
    """
    P1=point(5,9)
    P2=point()
    print(P1)
    print(P2)
    P2.move_to(3,9)
    print(P2)
    print(P1.distance(P2))
   
if __name__ == '__main__':
    main()
   