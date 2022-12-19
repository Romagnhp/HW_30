class Tag:
   __html = ''
   __htmlEnd = ''

   def __init__(self, html, htmlEnd):
      self.__html = html
      self.__htmlEnd = htmlEnd
     
   def getTag(self):
      return self.__html

   def getTagEnd(self):
      return self.__htmlEnd

class TagBr(Tag):
   def __init__(self):
      Tag.__init__(self, "<br>", "")

class TagHr(Tag):
   def __init__(self):
      Tag.__init__(self, "<hr>",  "")

class TagSub(Tag):
   def __init__(self):
      Tag.__init__(self, "<sub>", "")

class TagDiv(Tag):
   def __init__(self):
      Tag.__init__(self, "<div>", "</div>")

class TagSpan(Tag):
   def __init__(self):
      Tag.__init__(self, "<span>", "</span>")

class TagB(Tag):
   def __init__(self):
      Tag.__init__(self, "<b>", "</b>")

from abc import ABC, abstractmethod
class AbstractFactory():
   @abstractmethod
   def createTag_1(self):pass
   @abstractmethod
   def createTag_2(self):pass
   @abstractmethod 
   def createTag_3(self):pass
     
class NotPairTagFactory(AbstractFactory):
   def createTag_1(self):
      return TagBr()
   def createTag_2(self):
      return TagHr()
   def createTag_3(self):
      return TagSub()

class PairTagFactory(AbstractFactory):
   def createTag_1(self):
      return TagDiv()
   def createTag_2(self):
      return TagSpan()
   def createTag_3(self):
      return TagB()

listOfClass_1 = [NotPairTagFactory().createTag_1(), NotPairTagFactory().createTag_2(), NotPairTagFactory().createTag_3()]
for temp in listOfClass_1:
   print(temp.getTag())

listOfClass_2 = [PairTagFactory().createTag_1(), PairTagFactory().createTag_2(), PairTagFactory().createTag_3()]
for temp in listOfClass_2:
   print(temp.getTag(), temp.getTagEnd())