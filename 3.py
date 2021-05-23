class Nguoi():
    def getGender(self):
        return "unknown"
class nam( Nguoi):
    def getGender(self):
        return "nam"
class nu(Nguoi):
    def getGender(self):
        return "nu"
anam=nam()
anu=nu()
print(anam.getGender())
print(anu.getGender())
