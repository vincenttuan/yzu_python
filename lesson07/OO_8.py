class DictDemo:
    def __init__(self):
        self.dict = {}

    def __getitem__(self, item):
        return self.dict[item]

    def __setitem__(self, key, value):
        self.dict[key] = value

    def __len__(self):
        return len(self.dict)

d = DictDemo()
d['h'] = 180
d['w'] = 60

print(d['h'], d['w'], len(d))