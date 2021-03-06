class Glyphs(object):
    allowed_glyphs = frozenset()

    def __init__(self, *args):
        for arg in args:
            if arg in self.allowed_glyphs:
                setattr(self, arg, True)

    def __getattr__(self, name):
        # Any glyph we haven't assigned a value to, we don't have.
        if name in self.allowed_glyphs:
            return False
        object.__getattribute__(self, name)
