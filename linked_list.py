#!/usr/bin/env python3
"""Python implementation of a linked list."""

from itertools import islice


class LinkedList:
    """
    Python implementation of a linked list.

    >>> ll = LinkedList()
    >>> ll
    LinkedList([])
    >>> ll.head
    >>> len(ll)
    0
    >>> ll = LinkedList('hello')
    >>> ll
    LinkedList(['h', 'e', 'l', 'l', 'o'])
    >>> ll.head
    Node('h', <"link">)
    >>> len(ll)
    5
    """

    # TODO: __delitem__, __setitem__

    def __init__(self, iterable=None):
        """Create a linked list from the given iterable."""
        self.head = None
        if iterable is not None:
            Node = self.__class__.Node  # alias
            it = iter(iterable)
            self.head = Node(next(it))
            # Build linked list
            node = self.head
            for value in it:
                new_node = Node(value)
                node.link = new_node
                node = new_node

    def __bool__(self):
        """Return True if self.head exists."""
        return self.head is not None

    def __iter__(self):
        """Traverse the linked list, yielding each value."""
        return (n.value for n in self.nodes())

    def __getitem__(self, index):
        """Enable slicing."""
        it = iter(self)
        try:
            return next(islice(it, index, index+1))
        except TypeError:
            try:
                return islice(it, index.start, index.stop, index.step)
            except AttributeError:
                fmt = 'linked list indices must be integers or slices, not {}'
                msg = fmt.format(type(index).__name__)
                raise TypeError(msg) from None

    # def __setitem__(self, index, value):
    #     for i, node in self.nodes():
    #         if i == index:

    def __len__(self):
        """Iterate over self and return the count."""
        return sum(1 for _ in self)

    def __repr__(self):
        """Make repr, including a list of all values."""
        r = '{}({!r})'.format(
            self.__class__.__name__,
            list(self),
            )
        return r

    def nodes(self):
        """Traverse the linked list, yielding each node."""
        next_node = self.head
        while next_node is not None:
            yield next_node
            next_node = next_node.link

    def pop(self):
        """Remove the node at 0 and get its value."""
        if self.head is None:
            raise IndexError('pop from empty linked list')
        value = self.head.value
        self.head = self.head.link
        return value

    def push(self, value):
        """Insert a node at 0 with the given value."""
        new_head = self.__class__.Node(value)
        new_head.link = self.head
        self.head = new_head

    def index(self, x, i=0, j=None):
        """
        Get first index where value "x" occurs, where i < index < j.

        Same as list.index, but for a linked list.
        """
        for e, value in enumerate(self):
            if e < i:
                continue
            if j is not None and e > j:
                continue
            if value == x:
                return e
        raise ValueError('{!r} is not in linked list'.format(x))

    class Node:
        """Linked list node."""

        def __init__(self, value, link=None):
            """
            Create node with the given value and link.

            "link" is the next node.
            """
            self.value = value
            self.link = link

        def __repr__(self):
            """Make repr, without the value of "link" to avoid recursion."""
            r = '{}({!r}, <"link">)'.format(
                self.__class__.__name__,
                self.value,
                )
            return r


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
