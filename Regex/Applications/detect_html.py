# Hackerrank Detect HTML tags problem

from contextlib import redirect_stdout
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)

def main():
    N = int(input())

    html = ''.join(input() for _ in range(N))

    parser = MyHTMLParser()

    with open('out.txt', 'w') as out:
        with redirect_stdout(out):
            print(parser.feed(html))

    with open('out.txt') as out:
        seen = {line.strip() for line in out}
        print(';'.join(sorted(x for x in seen if x != 'None')))

if __name__ == '__main__':
    main()