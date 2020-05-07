import os
import re
from typing import List, Set, Dict, Tuple, Optional

CURRENT_DIRECTORY = "."

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
   <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
   <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>{0}</title>

    </head>
    <body>
        <h1>{0}</h1>
{1}
    </body>
</html>
"""
class HtmlPage:
    # relative path to the file without 'html'.
    path: str
    # sets html title and body heading
    title: str
    content: str

class ExampleHtmlPage(HtmlPage):
    linkName: str

    def __init__(self, tsFile):
        tsFileNoExtension = tsFile[2:-3]  # remove number and .swift

        tsFileHyphen = tsFileNoExtension[0] + re.sub(r'(?<!^)(?=[A-Z])', '-', tsFileNoExtension[1:]).lower()
        self.path = "examples/{}".format(tsFileHyphen)

        tsFileLinkHeading = tsFileNoExtension[0].upper() + re.sub(r'(?<!^)(?=[A-Z])', ' ', tsFileNoExtension[1:])
        self.title = tsFileLinkHeading + " Example"
        self.linkName = tsFileLinkHeading

""" Returns the TypeScript files in |dirPath|. """
def tsFiles(dirPath: str) -> List[str]:
    tsFiles = []
    for f in os.listdir(dirPath):
        if f.endswith(".ts"):
            tsFiles.append(f)
    return tsFiles

def readContents(file: str) -> str:
    with open(file, 'r') as f:
        return f.read()

""" Note that path should not have html extension. """
def buildHtmlLink(title: str, path: str) -> str:
    return '<a class="btn-lg btn-primary"  href="{}.html">{}</a>'.format(path, title)

def buildIndex(tsFiles: List[str]) -> HtmlPage:
    index = HtmlPage()
    index.title = "TypeScript Examples"
    index.path = "index"
    index.content = ""

    # Gets the correct order, 1, 2, ...
    # TODO(vaarnan): Will probably break for double digits, fix.
    for tsFile in reversed(tsFiles):
        tsPage = ExampleHtmlPage(tsFile)
        index.content += buildHtmlLink(tsPage.linkName, tsPage.path)
        index.content += '\n'

    return index

def formatExample(content: str) -> str:
    return "<br />".join(content.split("\n"))

def buildExample(tsFile: str) -> HtmlPage:
    example = ExampleHtmlPage(tsFile)
    example.content = "<pre>" + formatExample(readContents(tsFile)) + "</pre>"
    return example


def writeWebPage(page: HtmlPage):
    with open(page.path + ".html", "w") as p:
        p.write((HTML_TEMPLATE.format(page.title, page.content)))

writeWebPage(buildIndex(tsFiles(CURRENT_DIRECTORY)))

for tsFile in tsFiles(CURRENT_DIRECTORY):
    writeWebPage(buildExample(tsFile))

# for tsFile in tsFiles("."):
#     contents = readContents(tsFile)
#     parse
