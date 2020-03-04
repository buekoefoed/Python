import bs4
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_info(name):
    base_url = 'http://www.krak.dk'
    browser = webdriver.Firefox()
    browser.get(base_url)
    browser.implicitly_wait(3)

    # search_field = browser.find_element_by_tag_name('input')
    search_field = browser.find_element_by_name('searchQuery')
    search_field.send_keys(name)
    search_field.submit()

    sleep(3)
    # browser.implicitly_wait(3)

    link_to_persons = browser.find_elements_by_partial_link_text('Personer')
    print(link_to_persons)
    #print('PERSONS: ',link_to_persons)
    link_to_persons[0].click()

    sleep(3)

    page_source = browser.page_source

    soup = bs4.BeautifulSoup(page_source, 'html.parser')
    event_cells = soup.find_all('div', {'class': 'topBlock'})
    
    entries_str = []
    for e in event_cells:
        # print('cell: ',e)
        name = e.select('div h3 a')[0].text
        street = e.select('div>span:nth-child(1)')[0].text
        city = e.select('div>span:nth-child(2)')[0].text
        phone = e.select('span>span>div')[0].text
        samlet = '{}\n{}\n{}\n{}\n'.format(name,street,city,phone)
        #print(samlet)
        # print(element.text)
        entries_str.append(samlet)
    return entries_str

def save_to_file(content, out_path='./test.txt'):
    with open(out_path, 'w') as f:
        f.write(content)


if __name__ == '__main__':
    entries = get_info('Møller')
    save_to_file('\n\n'.join(entries))
