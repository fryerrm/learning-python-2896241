# 
# Example file for parsing and processing HTML
# LinkedIn Learning Python course by Joe Marini
#

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        pos = self.getpos()
        print("Comment at line", pos[0], "character", pos[1], "comment:", data)

    def handle_starttag(self, tag, attrs):
        pos = self.getpos()
        print("Start tag at line", pos[0], "character", pos[1], "tag:", tag)
        if attrs.__len__() > 0:
            print ("\tAttributes:")
            for a in attrs:
                print ("\t", a[0],"=",a[1])

    def handle_data(self, data):
        if (data.isspace()):
            return
        pos = self.getpos()
        print("Data at line", pos[0], "character", pos[1], "data:", data)

def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()
    
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read() # read the entire file
        parser.feed(contents)    

if __name__ == "__main__":
    main()
  