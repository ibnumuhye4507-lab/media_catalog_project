import sys
import os
import webbrowser
from lxml import etree
from tkinter import messagebox
import tkinter as tk

# የ tkinter ዋና መስኮት እንዳይታይ መደበቅ
root = tk.Tk()
root.withdraw()

# Directory setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(BASE_DIR))

XML_PATH = os.path.join(BASE_DIR, "..", "data", "catalog.xml")
XSL_PATH = os.path.join(BASE_DIR, "..", "data", "full_catalog.xsl")
REPORT_PATH = os.path.join(BASE_DIR, "..", "report.html")

from src.repositories.catalog_repository import CatalogRepository
from src.services.catalog_manager import CatalogManager
from src.models.factory import MediaFactory

def show_menu():
    print("\n" + "="*35)
    print("      MEDIA CATALOG MANAGER")
    print("="*35)
    print("1. View All Media Items")
    print("2. Add New Book")
    print("3. Add New Movie")
    print("4. Generate HTML Report")
    print("5. Search Media by Title")
    print("6. Delete Media by Title")
    print("7. Save and Exit")
    print("="*35)

def main():
    repo = CatalogRepository(XML_PATH)
    manager = CatalogManager()
    
    try:
        manager.set_items(repo.load_all())
    except Exception as e:
        print(f"Error loading data: {e}")
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            items = manager.get_all()
            if not items:
                print("\nThe catalog is empty.")
            else:
                for i, item in enumerate(items, 1):
                    type_name = item.__class__.__name__
                    print(f"{i}. [{type_name}] {item.title} ({item.year})")

        elif choice == '2' or choice == '3':
            m_type = "book" if choice == '2' else "movie"
            
            # --- Title Validation with Pop-up ---
            while True:
                title = input(f"Enter {m_type.capitalize()} Title: ")
                if any(c.isalpha() for c in title):
                    break
                else:
                    messagebox.showwarning("Invalid Input", "Title cannot be numbers only! Please use letters.")
                    print("⚠️ Error: Title must contain letters.")

            # --- Year Validation (Max 2018 E.C) ---
            while True:
                year = input(f"Enter {m_type.capitalize()} Year (E.C): ")
                if year.isdigit() and int(year) <= 2018:
                    break
                print("⚠️ Error: Year must be a number and <= 2018 E.C!")

            if m_type == "book":
                author = input("Author: ")
                new_item = MediaFactory.create_media("book", title=title, year=year, author=author)
            else:
                director = input("Director: ")
                new_item = MediaFactory.create_media("movie", title=title, year=year, director=director)
            
            manager.add_item(new_item)
            print(f"{m_type.capitalize()} added successfully!")

        elif choice == '4':
            try:
                if not os.path.exists(XML_PATH) or not os.path.exists(XSL_PATH):
                    print(f"Error: XML or XSL file not found!")
                    continue
                dom = etree.parse(XML_PATH)
                xslt = etree.parse(XSL_PATH)
                transform = etree.XSLT(xslt)
                new_dom = transform(dom)
                with open(REPORT_PATH, "wb") as f:
                    f.write(etree.tostring(new_dom, pretty_print=True))
                print(f"Report generated: {REPORT_PATH}")
                webbrowser.open('file://' + os.path.realpath(REPORT_PATH))
            except Exception as e:
                print(f"Report error: {e}")

        elif choice == '5':
            query = input("Enter title to search: ")
            results = manager.search_by_title(query)
            if results:
                print(f"\n--- Found {len(results)} item(s) ---")
                for i, item in enumerate(results, 1):
                    print(f"{i}. [{item.__class__.__name__}] {item.title} ({item.year})")
            else:
                print(f"No results found for '{query}'")

        elif choice == '6':
            title_to_delete = input("Enter the EXACT title to delete: ")
            success = manager.delete_item_by_title(title_to_delete)
            if success:
                print(f"Successfully deleted: '{title_to_delete}'")
            else:
                print(f"Media with title '{title_to_delete}' not found.")

        elif choice == '7':
            repo.save_all(manager.get_all())
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()