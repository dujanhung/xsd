from lxml import etree
import urllib
import sys
import os
class Validator:
 def __init__(self):
  self.tmp_xsd=None
 def load_xsd(self,schema_source:str):
  try:
   if schema_source.startswith("http://") or schema_source.startswith("https://"):
    with urllib.request.urlopen(schema_source) as r:
     data=r.read()
    self.tmp_xsd=tempfile.NamedTemporaryFile(suffix=".xsd")
    self.tmp_xsd.write(data)
    self.tmp_xsd.flush()
    schema_path=self.tmp_xsd.name
   else:
    schema_path=schema_source
   tree=etree.parse(schema_path)
   etree.XMLSchema(tree)
   return True
  except Exception as e:
   print(e)
   return False
 def cleanup_cache(self):
  if self.tmp_xsd:
   self.tmp_xsd.close()
   self.tmp_xsd=None
def main():
 if len(sys.argv)<2:
  print("✨ usage")
  print(f"🪜 {sys.argv[0]} <schema.xsd>")
  return 1
 validator=Validator()
 result=validator.load_xsd(sys.argv[1])
 validator.cleanup_cache()
 if result:
  return 0
 return 1
if __name__=="__main__":
 os.exec(f"exit {main()}")