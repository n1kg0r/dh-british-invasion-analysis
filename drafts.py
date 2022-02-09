

def get_lyrics_by_artist():
    """Returns distance between two wikipedia articles.
    For more information, see readme.
    :param source_url: url of source article
    :param target_url: url of target article
    :return: calculated distance
    """
    base_path = 'https://www.azlyrics.com/lyrics'
    visited_urls = set()
    next_url = ''
    visited_pages_number = 0

    while (base_path + next_url != target_url):
        current_page = requests.get(source_url)
        visited_urls.add(source_url)
        visited_pages_number += 1
        soup = BeautifulSoup(current_page.content, "html.parser")

        first_paragraph = soup.find("div", {"class": "mw-parser-output"}).findChild("p", recursive=True)
        if soup.find("table") and soup.find("table").find("tbody") \
                and soup.find("table").find("tbody").parent.findNextSibling('p') \
                and not soup.find("table").find("tbody").parent.findPreviousSibling('p'):
            first_paragraph = soup.find("table").find("tbody").parent.findNextSibling('p')

        first_paragraph_urls = first_paragraph.findChildren('a', recursive=True)
        if len(first_paragraph_urls) > 0:
            all_visited = True
            for link in first_paragraph_urls:
                if link['href'].find("/wiki/") == -1:
                    continue
                if link['href'].find(".ogg") != -1:
                    continue
                # контроль имен ссылок:
                # print(link.text)
                if base_path + link['href'] not in visited_urls:
                    next_url = link['href']
                    all_visited = False
                    break
            if all_visited == True:
                return -1
        else:
            return None
        # контроль адресов ссылок:
        # print(next_url)
        source_url = base_path + next_url

    if base_path + next_url == target_url:
        return visited_pages_number
    else:
        return None


print(distance('https://ru.wikipedia.org/wiki/Git',
               'https://ru.wikipedia.org/wiki/%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0_%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F_%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%8F%D0%BC%D0%B8'))
print(distance('https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B5%D0%B4%D0%BC%D0%B5%D1%82',
               'https://ru.wikipedia.org/wiki/%D0%A4%D0%B8%D0%BB%D0%BE%D1%81%D0%BE%D1%84%D0%B8%D1%8F'))
print(distance('https://ru.wikipedia.org/wiki/%D0%93%D1%80%D0%B0%D0%B2%D0%B8%D1%82%D0%B0%D1%86%D0%B8%D1%8F',
               'https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0'))
print(distance('https://ru.wikipedia.org/wiki/%D0%A7%D0%B5%D0%BB%D0%BE%D0%B2%D0%B5%D0%BA',
               'https://ru.wikipedia.org/wiki/%D0%9D%D0%B0%D1%83%D0%BA%D0%B0'))
print(distance('https://ru.wikipedia.org/wiki/Bash',
               'https://ru.wikipedia.org/wiki/%D0%A6%D0%B8%D0%B2%D0%B8%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F'))