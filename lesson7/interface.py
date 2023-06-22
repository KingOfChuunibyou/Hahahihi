

# interface (template behavior)

class BaseTeacher:

    def teach(self):
        raise NotImplementedError
    
    def kucing(self):
        raise NotImplementedError


class BiologiTeacher(BaseTeacher):

    def teach(self):
        print('aaa')

    def kucing(self):
        print("aaa")

