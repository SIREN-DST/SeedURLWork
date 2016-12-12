import xml.sax
import sys

class WikiContentHandler(xml.sax.ContentHandler):
  def __init__(self):
    xml.sax.ContentHandler.__init__(self)
    self.var = 0
    self.title=''
    self.desc=''
 
  def startElement(self, name, attrs):
    if name=="Topic" and attrs["r:id"].startswith('Top/Computers/Security'):
      self.var+=1
    if self.var==1 and name=="link":
        print attrs["r:resource"]
    if name=="ExternalPage":
      self.var+=1
    if self.var>0 and name=="d:Title":
      self.var+=1
    if self.var>0 and name=="d:Description":
      self.var+=1
    if self.var>0 and name=="topic":
      self.var+=1
       
  def endElement(self, name):
    if name=="Topic":
      self.var=0
    if name=="ExternalPage":
      self.var=0
      self.title=''
      self.desc=''
    pass
 
  def characters(self, content):
    content=content.strip().encode('utf-8')00
    if self.var == 2:
      if content!='':
        self.title=content
    if self.var == 3:
      if content!='':
        self.desc=content
    if self.var == 4:
      if content.startswith("Top/Computers/Security"):
        print "#"
        print self.title
        print "##"
        print self.desc
    pass
      



def main(sourceFileName):
  source = open(sourceFileName)
  Handler=WikiContentHandler()
  xml.sax.parse(source,Handler)
  

if __name__ == "__main__":
  args=sys.argv
  main(args[1])

