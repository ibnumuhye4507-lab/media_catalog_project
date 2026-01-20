import sys
import os
import webbrowser
from lxml import etree

# ፋይሉ ያለበትን አድራሻ በደንብ ለማወቅ
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# የፕሮጀክቱን root folder (media_catalog_project) ወደ path መጨመር
sys.path.append(os.path.dirname(BASE_DIR))

# አድራሻዎችን በቋሚነት ማስተካከል
XML_PATH = os.path.join(BASE_DIR, "..", "data", "catalog.xml")
XSL_PATH = os.path.join(BASE_DIR, "..", "data", "full_catalog.xsl")
REPORT_PATH = os.path.join(BASE_DIR, "..", "report.html")

from src.repositories.catalog_repository import CatalogRepository
from src.services.catalog_manager import CatalogManager
from src.models.factory import MediaFactory

def show_menu():
    print("\n" + "="*30)
    print("   የሚዲያ ካታሎግ ማስተዳደሪያ")
    print("="*30)
    print("1. ሁሉንም ሚዲያዎች እይ")
    print("2. አዲስ መጽሐፍ ጨምር")
    print("3. አዲስ ፊልም ጨምር")
    print("4. HTML ሪፖርት አውጣ")
    print("5. ሴቭ አድርግና ውጣ")
    print("="*30)

def main():
    # repo ሲፈጠር ትክክለኛውን የ XML አድራሻ እንሰጠዋለን
    repo = CatalogRepository(XML_PATH)
    manager = CatalogManager()
    
    # ፋይሉ ካለ ዳታውን እንዲያነብ፣ ከሌለ ባዶ እንዲጀምር
    try:
        manager.set_items(repo.load_all())
    except Exception as e:
        print(f"ዳታውን መጫን አልተቻለም: {e}")
    
    while True:
        show_menu()
        choice = input("ምርጫዎን ያስገቡ (1-5): ")
        
        if choice == '1':
            items = manager.get_all()
            if not items:
                print("\nካታሎጉ ባዶ ነው።")
            else:
                for i, item in enumerate(items, 1):
                    type_name = item.__class__.__name__
                    print(f"{i}. [{type_name}] ርዕስ: {item.title}, ዓ.ም: {item.year}")

        elif choice == '2':
            title = input("የመጽሐፉ ርዕስ: ")
            year = input("የታተመበት ዓ.ም: ")
            author = input("ደራሲ: ")
            new_book = MediaFactory.create_media("book", title=title, year=year, author=author)
            manager.add_item(new_book)
            print("መጽሐፉ ተጨምሯል! (ለማስቀመጥ 5 ቁጥርን መጫን አይርሱ)")

        elif choice == '3':
            title = input("የፊልሙ ርዕስ: ")
            year = input("የወጣበት ዓ.ም: ")
            director = input("አዘጋጅ (Director): ")
            new_movie = MediaFactory.create_media("movie", title=title, year=year, director=director)
            manager.add_item(new_movie)
            print("ፊልሙ ተጨምሯል! (ለማስቀመጥ 5 ቁጥርን መጫን አይርሱ)")

        elif choice == '4':
            try:
                import webbrowser  # አውቶማቲክ እንዲከፍትልን
                if not os.path.exists(XML_PATH) or not os.path.exists(XSL_PATH):
                    print(f"\n no ስህተት: {XML_PATH} ወይም {XSL_PATH} አልተገኘም!")
                    continue
                
                dom = etree.parse(XML_PATH)
                xslt = etree.parse(XSL_PATH)
                transform = etree.XSLT(xslt)
                new_dom = transform(dom)
                
                with open(REPORT_PATH, "wb") as f:
                    f.write(etree.tostring(new_dom, pretty_print=True))
                
                print(f"\n ok ሪፖርቱ '{REPORT_PATH}' ተዘጋጅቷል!")
                
                # ይህ መስመር ነው አውቶማቲክ Chrome-ን የሚከፍተው
                webbrowser.open('file://' + os.path.realpath(REPORT_PATH))
                
            except Exception as e:
                print(f"\n ሪፖርት ማውጣት አልተቻለም: {e}")
        elif choice == '5':
            repo.save_all(manager.get_all())
            print("መረጃው ተቀምጧል (Saved)። ደህና ሁኑ!")
            break
        else:
            print("የተሳሳተ ምርጫ! እባክህ እንደገና ሞክር።")

if __name__ == "__main__":
    main()