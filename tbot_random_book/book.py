from requests import get, exceptions
from bs4 import BeautifulSoup


GOOD_STATUS_CODE_LIMIT = 299
ERROR = 'Упс, что-то пошло не так. Попробуйте ещё раз.'


def load_book(url: str) -> dict | None:
    result = dict()

    try:
        resp = get(url, allow_redirects=True)
        if resp.status_code > GOOD_STATUS_CODE_LIMIT:
            raise exceptions.RequestException
    except exceptions.RequestException:
        return None

    soup = BeautifulSoup(resp.content.decode('utf-8', 'ignore'), 'lxml')
    result['title'] = soup.find('h1').text.strip() if soup.find('h1') else ''
    result['author'] = soup.find('h2').text.strip() if soup.find('h2') else ''
    result['description'] = str(
        soup.find(id='lenta-card__text-edition-escaped').text.strip()
    ) if soup.find(id='lenta-card__text-edition-escaped') else ''
    result['img'] = soup.find(id="main-image-book")['src'] \
        if soup.find(id="main-image-book") else ''

    return result


class Book(object):

    def __init__(self, url: str):
        self.book = load_book(url)

    @property
    def description(self) -> str:
        if self.book is None:
            return ERROR

        result = '\n'.join(
            [
                self.book.get('title', ''),
                self.book.get('author', ''),
                self.book.get('description', '')

            ]).strip()

        return result if result else ERROR

    @property
    def image_link(self) -> str | None:
        return self.book.get('img') if self.book else ''
