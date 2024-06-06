def acronymize(url:str):
    trash = ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]
    for i in trash:
        url = url.replace(i, '')
    url = url.replace('-', ' ')

    url = ''.join(item.upper()[0] for item in url.split())
    return url


def generate_bc(url:str, separator:str):
    trash = ['.html', '.htm', '.php', '.asp', '/index']
    for i in trash:
        url = url.replace(i, '')
    
    url = url.split('#')[0].split('?')[0]

    url_list = url.split('/')[1:]
    names_list = [item.upper().replace('-',' ') if len(item) < 30 else acronymize(item) for item in url_list]

    res_list = ['<a href="/">HOME</a>']
    for i in range(len(url_list)):
        href = '/'.join(url_list[:i+1])+'/'
        if i != len(names_list)-1:
            res_list.append(f'<a href="/{href}">{names_list[i]}</a>')
        else:
            res_list.append(f'<span class="active">{names_list[i]}</span>')

    return f'{separator}'.join(res_list)
