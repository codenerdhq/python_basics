# Author: CodeNerdHQ

class Square:
     def __init__(self, width):
         self.width = width

     def getWidth(self):
         return self.width

     def setWidth(self, width):
         self.width = width

     def getArea(self):
         return self.width * self.width