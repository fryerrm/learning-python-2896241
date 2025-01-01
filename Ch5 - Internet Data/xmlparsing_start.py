# 
# Example file for parsing and processing XML
# LinkedIn Learning Python course by Joe Marini
#

# import xml.dom.minidom as MD
import xml.etree.ElementTree as ET

def get_skills(xml_file):
    # use the parse() function to load and parse an XML file
#    doc = MD.parse(xml_file)
    
    # print out the document node and the name of the first child tag
#    print("Doc name:", doc.nodeName, "\nFirst Child:", doc.firstChild.tagName)


    try:
        # parse XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()
        print(tree.findall("skill"), root)

        #iterate through each person element in the XML
        for person in root.findall("person"):
            print("------------")
            firstname = person.find("firstname").text
            lastname = person.find("lastname").text
            print("Skills for", firstname, lastname,":")

            for skill in person.findall("skill"):
                print(skill)
            print("------------")
        print("-End List-")

    except Exception as e:
        print("Could not parse file:", xml_file)

      
    # create a new XML tag and add it into the document

  

if __name__ == "__main__":
    get_skills("samplexml.xml")

