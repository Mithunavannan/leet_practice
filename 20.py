characters = " '()', '[]', '{}' "

def isValid(self, s):
    if s.count(characters) != s.count(characters):
        return False
    return True