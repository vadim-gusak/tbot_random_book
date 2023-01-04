from tbot_random_book.book import Book
import pook


TEST_URL = 'http://test.com'


@pook.on
def test_book():

    test_html = '''
    <html>
        <body>
            <h1>
                My_title
            </h1>
            <h2>
                Wow_author
            </h2>
            <img id="main-image-book" src="http://test.com/img">
            <div id="lenta-card__text-edition-escaped">
                Test description 
            </div>
        </body>
    </html>
    '''
    pook.get(
        TEST_URL,
        reply=200,
        response_body=test_html
    )

    book = Book(TEST_URL)

    assert book.image_link == "http://test.com/img"
    assert book.description == 'My_title\nWow_author\nTest description'


@pook.on
def test_book_errors():
    pook.get(
        TEST_URL,
        reply=301,
        response_body=''
    )

    book = Book(TEST_URL)

    assert book.description == 'Упс, что-то пошло не так. Попробуйте ещё раз.'
    assert book.image_link == ''

    pook.get(
        TEST_URL,
        reply=200,
        response_body=''
    )

    assert book.description == 'Упс, что-то пошло не так. Попробуйте ещё раз.'
    assert book.image_link == ''
