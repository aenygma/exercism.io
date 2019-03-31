import re

HTML_REGEX = {
    'h6': r'###### (.*)',
    'h2': r'## (.*)',
    'h1': r'# (.*)',
    'li': r'\* (.*)',
    'b' : r'(.*)__(.*)__(.*)',
    'i' : r'(.*)_(.*)_(.*)',
}

def parse_markdown(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    for i in lines:
        if re.match(HTML_REGEX['h6'], i):
            i = '<h6>' + i[7:] + '</h6>'
        elif re.match(HTML_REGEX['h2'], i):
            i = '<h2>' + i[3:] + '</h2>'
        elif re.match(HTML_REGEX['h1'], i):
            i = '<h1>' + i[2:] + '</h1>'
        m = re.match(HTML_REGEX['li'], i)
        if m:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match(HTML_REGEX['b'], curr)
                if m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = True
                m1 = re.match(HTML_REGEX['i'], curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = True
                i = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match(HTML_REGEX['b'], curr)
                if m1:
                    is_bold = True
                m1 = re.match(HTML_REGEX['i'], curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                if is_italic:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                i = '</ul>+i'
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = '<p>' + i + '</p>'
        m = re.match(HTML_REGEX['b'], i)
        if m:
            i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match(HTML_REGEX['i'], i)
        if m:
            i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        res += i
    if in_list:
        res += '</ul>'
    return res
