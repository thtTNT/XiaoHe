class Listener:

    def __init__(self):
        global funcs
        funcs = []

    def fire(self,eventObj):
        for func in funcs:
            funcasd = getattr(self,"fire")
