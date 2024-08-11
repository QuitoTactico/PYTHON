def shorten_number(suffixes, base):
    def filter(number : str):
        try:
            if not number.isdecimal(): return number
        except:
            return str(number)
        
        if len(suffixes) == 0: str(number)
        if not number: return ''

        power = 0
        number = int(number)
        while number > base and power < len(suffixes)-1:
            number = number // base
            power += 1
        return f'{number}{suffixes[power]}'

    return filter

filter1 = shorten_number(['','k','m'],1000)
filter1('234324') == '234k'
filter1('98234324') == '98m'
filter1([1,2,3]) == '[1,2,3]'
filter1('32424234223'), '32424m'

filter2 = shorten_number(['B','KB','MB','GB'],1024)
filter2('32') == '32B'
filter2('2100') == '2KB'
filter2('pippi') == 'pippi'


''' ???????????

def shorten_number(suffixes,base): t=lambda n, suf=suffixes,base=base,i=len(suffixes)-1: str(n) if type(n)!=str or not str.isdigit(n) else (lambda div: str(int(n)//div)+suffixes[i] if int(n)>=div else t(n,suf,base,i-1))(base**i); return t

'''