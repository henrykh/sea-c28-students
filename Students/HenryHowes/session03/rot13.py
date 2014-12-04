def rot13(text):
    """return the given text encoded with the ROT13 encryption scheme"""
    return text.encode('rot_13')

if __name__ == '__main__':
    assert rot13(u"TeSt") == u"GrFg"
    assert rot13(u"Here: a string that's full 2 the brim of non-@lphas") == u"Urer: n fgevat gung'f shyy 2 gur oevz bs aba-@ycunf"
    print "Encoding successful"
