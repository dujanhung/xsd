from lxml import etree
import sys
def main():
 if len(sys.argv)<2:
  print("✨ usage")
  print(f"🪜 {sys.argv[0]} <schema.xsd>")
  return 1
 return 0
if __name__=="__main__":
 sys.exit(main())