class Body:
   html = '<body></body>'
     
   def getTag(self):
      return self.html

class Br(Body):
   html = '<br>'
   
class Hr(Body):
   html =' <hr>'

class Sub(Body):
   html = '<sub>'

class Div(Body):
   html = '<div></div>'

class Span(Body):
   html = '<span></span>'

class P(Body):
   html = '<b></b>'

from abc import ABC, abstractmethod
class AbstractFactory():
   @abstractmethod
   def create_tag(self, type):pass
     
class NotPairTagFactory(AbstractFactory):
   def create_tag(self, type):
      keyNameClass = type.capitalize()
      dictClasses = globals()
      return dictClasses[keyNameClass]()

class PairTagFactory(AbstractFactory):
   def create_tag(self, type):
      keyNameClass = type.capitalize()
      dictClasses = globals()
      return dictClasses[keyNameClass]()

obj_body = NotPairTagFactory()
singleTag = ['br','hr','sub']

for temp in singleTag:
   print(obj_body.create_tag(temp).getTag())



obj_body = PairTagFactory()
pairTag = ['div','span','p']

for temp in pairTag:
   print(obj_body.create_tag(temp).getTag())