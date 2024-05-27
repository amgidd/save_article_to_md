import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

"""
saves article from site as markdown file
input
- URL of the site
- tag and class of the article in DOM
output
- md file in current dir
"""

def parse_response(inp_URL: str, tag_to_search: str, class_to_search: str = None) -> tuple[str, "Tag"]:
    """
    request a response from site
    finds an article on html
    finds title of article, if not found title=title
    returns title and bs4 Tag of the article
    """
    soup = BeautifulSoup(requests.get(inp_URL).text, "html.parser")
    tag_content = soup.find(tag_to_search, class_ = class_to_search)

    for child in tag_content.descendants:
        if child.name in {'h1', 'h2', 'h3'}:
            title = child.text
            break
    else: title = 'title'

    return (title, tag_content)

def save(to_save: tuple[str, "Tag"], URL: str) -> None:
    """
    opens file named as title
    saves bs4 Tag as md to file
    """
    with open(to_save[0]+".md", "w") as f:
        f.write(markdownify(f"<a href={f"{URL}"}>source:</a>\n\n{to_save[1].__repr__() }", heading_style = "ATX"))

if __name__ == "__main__":
    inp_URL = input("Enter URL ")
    tag_to_search = input('Enter tag ')
    class_to_search = input('Enter class ')
    if not class_to_search:
        class_to_search = None
    texts = parse_response(inp_URL, tag_to_search, class_to_search)
    save(texts, inp_URL)
