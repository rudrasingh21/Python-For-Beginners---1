class RemoteControl():
    def __init__(self):
        self.channels = ["HBO","ABC","ESPN","SAB"]
        self.index = -1
        #var for what channel you are right now

    def __iter__(self):
        return self     #iter method will return same object

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration

        return self.channels[self.index]

r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))



