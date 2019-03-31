import re

# split by \n
HTML_REGEX = {
    'para': (r'(.+)', r'<p>\g<1></p>'),
    'strong': (r'_{2}(.*)_{2}', r'<strong>\g<1></strong>'),
    'em': (r'_{1}(.*)_{1}', r'<em>\g<1></em>'),
    'list':(r'^\* (.*)', r'<li>\g<1></li>'),
    'h6': (r'^\#{6} (.*)', r'<h6>\g<1></h6>'),
    'h5': (r'^\#{5} (.*)', r'<h5>\g<1></h5>'),
    'h4': (r'^\#{4} (.*)', r'<h4>\g<1></h4>'),
    'h3': (r'^\#{3} (.*)', r'<h3>\g<1></h3>'),
    'h2': (r'^\#{2} (.*)', r'<h2>\g<1></h2>'),
    'h1': (r'^\#{1} (.*)', r'<h1>\g<1></h1>'),
}
TEST_TAG_LIST = re.compile(r'^\* (.*)')
TEST_TAG_HEADER = re.compile(r'^\#')

def parse_markdown(markdown):
    """ parse given markdown code and return html """

    ret = ""
    # a stack used to hold list items
    stack_list = []

    lines = markdown.split("\n")
    for line in lines:

        skip_tags = []

        #
        # test tags
        #
        is_header = TEST_TAG_HEADER.search(line)
        is_list = TEST_TAG_LIST.search(line)

        #
        # apply filters
        #
        if is_list:
            skip_tags.extend(['para', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        if is_header:
            skip_tags.extend(['para', 'strong', 'em', 'list'])

        #
        # process line
        #
        for (tag_name, tag_regex) in HTML_REGEX.items():
            (rstr, repl) = tag_regex
            if tag_name not in skip_tags:
                line = re.sub(rstr, repl, line)

        #
        # result handling
        #
        if is_list and not stack_list:
            # start of list: if we are in list, and haven't been before
            stack_list.append("<ul>")
            stack_list.append("</ul>")
        if is_list and stack_list:
            # continuing list: if we are in list, and have been before
            stack_list.insert(-1, line)
        elif not is_list and stack_list:
            # end of list: if we aren't in list, but have been before
            ret += "".join(stack_list)
            stack_list = []
        elif not is_list:
            # if not list, proceed normally
            ret += line

    # if end of list
    if stack_list:
        ret += "".join(stack_list)
        stack_list = []

    return ret
