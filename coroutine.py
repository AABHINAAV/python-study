def searcher():
    import time
    book = "hello everyone, it is not a function.....it is a coroutine."
    time.sleep(4)       # it is like starting time

    while True:
        text = (yield)      # takes one thing for searching
        if text in book:
            print('this text is in the book')
        else:
            print('this text is not in the book')

search = searcher()
next(search)
search.send('hello')
search.send('everyone')
search.send('function')
search.close()