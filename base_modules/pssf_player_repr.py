"""repr example"""


class Player(object):
    """A player in the game"""

    def __init__(self, id, name, keys):
        self.id = id
        self.name = name
        self.keys = keys

    def __repr__(self):
        """

        If a conversion is specified, the result of evaluating the expression is converted before formatting.
        Conversion '!r' calls repr()
        """
        # self can be a subclass
        cls = self.__class__.__name__
        return f'{cls}({self.id!r}, {self.name!r}, {self.keys!r})'


# Example
if __name__ == '__main__':
    # Loads logging only when this module is directly run
    import logging

    logging.basicConfig(level=logging.INFO, filename='game.log')

    p1 = Player(1, 'Parzival', {'copper', 'jade'})
    """
    %r only works in old-style % string formatting. It indeed converts the object to a 
    representation through the repr() function.
    """
    logging.info('p1 is %r', p1)
