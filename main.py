class Body:
   __html = '<body></body>'

   def __init__(self, html):
      self.__html = html
     
   def getTag(self):
      return self.__html

class TagBr(Body):
   def __init__(self):
      Body.__init__(self, "<br>")

class TagHr(Body):
   def __init__(self):
      Body.__init__(self, "<hr>")

class TagSub(Body):
   def __init__(self):
      Body.__init__(self, "<sub>")

class TagDiv(Body):
   def __init__(self):
      Body.__init__(self, "<div></div>")

class TagSpan(Body):
   def __init__(self):
      Body.__init__(self, "<span></span>")

class TagP(Body):
   def __init__(self):
      Body.__init__(self, "<b></b>")

from abc import ABC, abstractmethod
class AbstractFactory():
   @abstractmethod
   def getTagBr(self):pass
   @abstractmethod
   def getTagHr(self):pass
   @abstractmethod 
   def getTagSub(self):pass
   @abstractmethod   
   def getTagDiv(self):pass
   @abstractmethod
   def getTagSpan(self):pass
   @abstractmethod
   def getTagP(self):pass
     
class NotPairTagFactory(AbstractFactory):
   def getTagBr(self):
      return TagBr()
   def getTagHr(self):
      return TagHr()
   def getTagSub(self):
      return TagSub()

class PairTagFactory(AbstractFactory):
   def getTagDiv(self):
      return TagDiv()
   def getTagSpan(self):
      return TagSpan()
   def getTagP(self):
      return TagP()

temp  = NotPairTagFactory()  
tag_1 = temp.getTagBr()
tag_2 = temp.getTagHr()
tag_3 = temp.getTagSub()

print(tag_1.getTag())
print(tag_2.getTag())
print(tag_3.getTag())

temp = PairTagFactory()
tag_1 = temp.getTagDiv()
tag_2 = temp.getTagSpan()
tag_3 = temp.getTagP()

print(tag_1.getTag())
print(tag_2.getTag())
print(tag_3.getTag())