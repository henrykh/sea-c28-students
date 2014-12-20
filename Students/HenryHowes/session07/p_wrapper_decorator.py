def p_wrapper(func):
    def wrapped_string(string):
        return '<p> {} </p>'.format(string)
    return wrapped_string
