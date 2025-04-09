from selene import browser, be, have, by


def test_positive_search(url_browser, conf_browser):
    browser.element('[id=searchbox_input]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id=web_content_wrapper]').should(have.text('yashaka/selene'))

   # assert browser.should()


def test_negative_search(url_browser, conf_browser):
    browser.element('[id=searchbox_input]').should(be.blank).type('}}||||<<?????').press_enter()
    browser.element('[id=web_content_wrapper]').should(have.text('По запросу }}||||<<????? не найдены результаты'))


# browser.open('https://duckduckgo.com/')
# browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
# browser.element('html').should(have.text('yashaka/selene'))
