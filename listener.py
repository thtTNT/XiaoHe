class Listener:

    def __init__(self):
        self.funcs = []

    def fire(self, e_type, e_obj):
        for node in self.funcs:
            if node.l_type == e_type:
                func = node.l_func
                func(e_obj)

    def add_listener(self, l_type, l_func):
        self.funcs.append(ListenNode(l_type, l_func))


class ListenNode:

    def __init__(self, l_type, l_func):
        self.l_type = l_type
        self.l_func = l_func
