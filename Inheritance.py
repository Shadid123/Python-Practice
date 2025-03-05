class Phone:
    def call(self):
        print("You can  call")
    def massage(self):
        print("You can send massage")
class Samsung(Phone):
    def photo(self):
        print("You can take photo")

s=Samsung()
s.call()
s.massage()
s.photo()