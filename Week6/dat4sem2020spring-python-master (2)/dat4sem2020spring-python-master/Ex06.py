import multiprocessing as mp
import requests
import threading
import math
from concurrent.futures import ProcessPoolExecutor


class NotFoundException(Exception):
    pass


class Corona():
    def __init__(self, url_list):
        self.url_list = url_list
        self.filelist = []
        self.filelist_generator(self.url_list)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            file = self.filelist[self.index]
            with open(file) as file_object:
                contents = file_object.read()
        except IndexError:
            raise StopIteration
        self.index += 1
        return contents

    def download(self, url, filename):
        r = requests.get(url)
        if requests.status_codes == 404:
            raise NotFoundException()
        with open(filename, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=1024):
                fd.write(chunk)

    def multi_download(self, url_list):
        for url in url_list:
            thread = threading.Thread(
                target=self.download(url, "Book_{}.txt".format(url[-8: -5])))
            thread.start()
            thread.join()

    def filelist_generator(self, url_list):
        for url in url_list:
            self.filelist.append("Book_{}.txt".format(url[-8: -5]))

    def avg_vowels(self, text):
        vowels = 0
        words = 0
        for word in text:
            lword = word.lower()
            vowels += lword.count("a")
            vowels += lword.count("e")
            vowels += lword.count("i")
            vowels += lword.count("o")
            vowels += lword.count("u")
            vowels += lword.count("y")
            vowels += lword.count("æ")
            vowels += lword.count("ø")
            vowels += lword.count("å")
        words = len(text.split())
        return vowels / words

    def hardest_read(self):
        with ProcessPoolExecutor() as ppe:
            res = ppe.map(self.avg_vowels, self)
        return list(res)


url_list = ["https://www.gutenberg.org/cache/epub/1342/pg1342.txt",
            "https://www.gutenberg.org/cache/epub/27525/pg27525.txt",
            "https://www.gutenberg.org/cache/epub/10/pg10.txt",
            "https://www.gutenberg.org/cache/epub/20/pg20.txt"]
corona = Corona(url_list)
# corona.multi_download(url_list)
avg = []
avg.append(corona.avg_vowels(next(corona)))
avg.append(corona.avg_vowels(next(corona)))
avg.append(corona.avg_vowels(next(corona)))
avg.append(corona.avg_vowels(next(corona)))


print(corona.hardest_read())
