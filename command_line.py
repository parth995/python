#!/usr/bin/env python3

from urllib.request import urlopen
import sys

def fetch_words(url):
    """ used to fetch words from URL 
    
    Args:
        url: The URL of UTF-8 text document

    Returns:
        A list of strings words from document.
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
    # \print(line_words)
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_words(story_words):
    for word in story_words:
        print(word)


def main(url):
    words = fetch_words(url)
    print_words(words)


if __name__ == '__main__':
    main(sys.argv[1])