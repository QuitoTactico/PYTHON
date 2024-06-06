def acronymize(url:str):
    trash = ["the","of","in","from","by","with","and", "for", "or", "to", "at", "a"]
    url_list = url.split('-')
    url_list_filtered = [item for item in url_list if item not in trash]

    '''
    for i in trash:
        url = url.replace('-'+i, '').replace(i+'-', '')
    '''

    #url = url.replace('-', ' ')

    #url = ''.join(item.upper()[0] for item in url.split())
    url = ''.join(item.upper()[0] for item in url_list_filtered)
    return url


def generate_bc(url:str, separator:str):
    trash = ['.html', '.htm', '.php', '.asp', '/index']
    for i in trash:
        url = url.replace(i, '')
    
    url = url.split('#')[0].split('?')[0].split('://')[-1]

    url_list = [item for item in url.split('/')[1:] if item]
    if len(url_list) == 0:
        return '<span class="active">HOME</span>'

    names_list = [item.upper().replace('-',' ') if len(item) < 30 else acronymize(item) for item in url_list]

    res_list = ['<a href="/">HOME</a>']
    for i in range(len(url_list)):
        href = '/'.join(url_list[:i+1])+'/'
        if i != len(names_list)-1:
            res_list.append(f'<a href="/{href}">{names_list[i]}</a>')
        else:
            res_list.append(f'<span class="active">{names_list[i]}</span>')

    return f'{separator}'.join(res_list)


# -------------------------------- smart ones --------------------------------------

def generate_bc(url, separator):
    a, span = '<a href="%s/">%s</a>', '<span class="active">%s</span>'
    restricted = set("THE OF IN FROM BY WITH AND OR FOR TO AT A".split())
    def bc(menu):
        menu = menu.upper().replace('-', ' ')
        if len(menu) > 30: menu = ''.join(w[0] for w in menu.split() if w not in restricted)
        return menu or 'HOME'
    url = ''.join(url.strip('/').rpartition('//')[2].partition('/')[1:]) \
            .rsplit('?',1)[0].rsplit('#',1)[0].rsplit('.',1)[0].rsplit('/index')[0].split('/')
    return separator.join([a % ('/'.join(url[:i]), bc(m)) for i, m in enumerate(url[:-1], 1)] + [span % bc(url[-1])])


#------------------------------------- pretty one -------------------------------------------

def generate_bc(url: str, separator: str) -> str:
    """Split an url into breadcrumbs separated by given characters."""

    # HTML templates
    a, span = '<a href="%s/">%s</a>', '<span class="active">%s</span>'
    # Short common words
    restricted = set("THE OF IN FROM BY WITH AND OR FOR TO AT A".split())

    def format_bc(part: str, max_length: int = 30, home: str = 'HOME') -> str:
        """Format a breadcrumb part and shorten it if necessary."""

        formatted = (part or home).upper().replace('-', ' ')
        if len(formatted) > max_length:
            formatted = ''.join(word[0]
                                for word in formatted.split()
                                if word not in restricted)
        return formatted

    *path, active_class = (''.join(url.strip('/')
                                   .rpartition('//')[2]  # drop protocol
                                   .partition('/')[1:])  # drop host
                           .rsplit('#', 1)[0]  # drop anchor
                           .rsplit('?', 1)[0]  # drop query
                           .rsplit('.', 1)[0]  # drop extension
                           .rsplit('/index')[0]  # drop index
                           .split('/'))
    return separator.join([a % ('/'.join(path[:i]), format_bc(m))
                           for i, m in enumerate(path, 1)] +
                          [span % format_bc(active_class)])