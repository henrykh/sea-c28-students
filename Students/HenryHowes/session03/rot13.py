def rot13(text):
    return text.encode('rot_13')

if __name__ == '__main__':
    assert rot13(u"TeSt") == u"GrFg"
    print "Encoding successful"
