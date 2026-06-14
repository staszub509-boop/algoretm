
# voted = {} 
# def chek_voter(name):
#     if voted.get(name):
#         print('kick them out')
#     else:
#         voted[name] = True
#         print('let them vote')

cache = {}
def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = https://Google.com(url)
        cache[url] = data
        return data

get_page('example.com')