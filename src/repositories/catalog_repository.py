import xml.etree.ElementTree as ET
import os
from src.models.media import Book, Movie
from src.models.factory import MediaFactory

class CatalogRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_all(self):
        """ከ XML ፋይል መረጃን ያነባል"""
        if not os.path.exists(self.file_path):
            return []
        
        try:
            tree = ET.parse(self.file_path)
            root = tree.getroot()
            items = []

            for elem in root:
                # የ XML መረጃውን ወደ dictionary እንቀይራለን
                data = {child.tag: child.text for child in elem}
                # በFactory አማካኝነት ኦብጀክቱን እንፈጥራለን
                item = MediaFactory.create_media(elem.tag, **data)
                if item:
                    items.append(item)
            return items
        except Exception as e:
            print(f"መረጃ ሲጫን ስህተት ተፈጥሯል: {e}")
            return []

    def save_all(self, media_items):
        """መረጃን ወደ XML ፋይል ሴቭ ያደርጋል"""
        try:
            # የ data ፎልደር ከሌለ እንዲፈጠር ማድረግ
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

            root = ET.Element("catalog")
            for item in media_items:
                # የ tag ስም መምረጥ
                if isinstance(item, Book):
                    tag = "book"
                elif isinstance(item, Movie):
                    tag = "movie"
                else:
                    continue

                media_elem = ET.SubElement(root, tag)
                ET.SubElement(media_elem, "title").text = str(item.title)
                ET.SubElement(media_elem, "year").text = str(item.year)
                
                # እንደየአይነቱ የተለየውን መረጃ እንጨምራለን
                if isinstance(item, Book):
                    ET.SubElement(media_elem, "author").text = str(item.author)
                elif isinstance(item, Movie):
                    ET.SubElement(media_elem, "director").text = str(item.director)
            
            tree = ET.ElementTree(root)
            with open(self.file_path, "wb") as f:
                tree.write(f, encoding="UTF-8", xml_declaration=True)
            print("መረጃው በ XML ፋይል ውስጥ ተቀምጧል!")
            
        except Exception as e:
            print(f"ሴቭ ሲደረግ ስህተት ተፈጠረ: {e}")