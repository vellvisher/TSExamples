import os
import re
from typing import List, Set, Dict, Tuple, Optional

CURRENT_DIRECTORY = "."
EXAMPLES_DIRECTORY = "examples"
TYPESCRIPT_EXTENSION = ".ts"

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
<div class="container-fluid">
        <h1>{0}</h1>
<hr>
{1}
</div>
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

    # example name is of format helloWorld
    def __init__(self, exampleName: str):
        assert(not exampleName.endswith(TYPESCRIPT_EXTENSION))
        tsFileHyphen = exampleName[0] + re.sub(r'(?<!^)(?=[A-Z])', '-', exampleName[1:]).lower()
        self.path = "examples/{}".format(tsFileHyphen)

        tsFileLinkHeading = exampleName[0].upper() + re.sub(r'(?<!^)(?=[A-Z])', ' ', exampleName[1:])
        self.title = tsFileLinkHeading + " Example"
        self.linkName = tsFileLinkHeading

""" Returns the TypeScript files in |dirPath|. """
def tsFiles(dirPath: str) -> List[str]:
    tsFiles = []
    for f in os.listdir(dirPath):
        if f.endswith(TYPESCRIPT_EXTENSION):
            tsFiles.append(f)
    return tsFiles

def readContents(file: str) -> str:
    with open(file, 'r') as f:
        return f.read()

def readLines(file: str) -> List[str]:
    with open(file, 'r') as f:
        return f.readlines()

""" Note that path should not have html extension. """
def buildHtmlLink(title: str, path: str) -> str:
    return '<a class="btn-lg btn-primary"  href="{}.html">{}</a>'.format(path, title)

def buildIndex(tsFiles: List[str]) -> HtmlPage:
    index = HtmlPage()
    index.title = "TypeScript Examples"
    index.path = "index"
    index.content = ""

    # List of sorted file names without number
    iterOrder:List[Tuple[int, str]] = []
    for tsFile in tsFiles:
        iterOrder.append(splitIndexAndExampleName(tsFile))

    iterOrder = sorted(iterOrder)

    for (_, htmlFileName) in iterOrder:
        tsPage = ExampleHtmlPage(htmlFileName)
        index.content += buildHtmlLink(tsPage.linkName, tsPage.path)
        index.content += '\n'

    return index

# Takes 11-helloWorld.ts and returns (11, helloWorld)
def splitIndexAndExampleName(tsFile: str) -> Tuple[int, str]:
    num, fileName = tsFile.split("-", 1)
    num, exampleName = (num, fileName[:-3])
    return (int(num), exampleName)

def formatExample(content: str) -> str:
    return "<br />".join(content.split("\n"))

def buildExample(tsFile: str) -> HtmlPage:
    _, htmlFileName = splitIndexAndExampleName(tsFile)
    example = ExampleHtmlPage(htmlFileName)
    example.content = ""
    index = 0
    for line in readLines(tsFile):
        if line.startswith("//"):
            if index > 0:
                example.content += "</code>"
            example.content += "<h6>" + line[3:] + "</h6>\n<code>"
        else:
            example.content += line + "<br>"
        index += 1

    example.content += "</code>"
    return example

def writeWebPage(page: HtmlPage):
    with open(page.path + ".html", "w") as p:
        p.write((HTML_TEMPLATE.format(page.title, page.content)))

writeWebPage(buildIndex(tsFiles(CURRENT_DIRECTORY)))

os.makedirs(EXAMPLES_DIRECTORY, exist_ok = True)

for tsFile in tsFiles(CURRENT_DIRECTORY):
    writeWebPage(buildExample(tsFile))
