
from adblockparser import AdblockRules
class EasyCompare:
    def DataAnnalises(self, javaData,javaScriptData):
        self.JavaList = javaData
        self.JavaScriptList = javaScriptData


trackers = []
easytrackerlist = []
privacytrackerlist = []
cookietrackerlist = []
socialtrackerlist = []
annoyanctrackerlist = []

with open("reddit_javascript_2.txt", encoding="utf8") as cookies:
    datalist = cookies.readlines()

with open("easylist.txt", encoding="utf8") as easylist:
    easytrackers = easylist.readlines()
easyrules = AdblockRules(easytrackers)

with open("easyprivacy.txt", encoding="utf8") as privacylist:
    privacytrackers = privacylist.readlines()
privacyrules = AdblockRules(privacytrackers)

with open("easycookie.txt", encoding="utf8") as cookielist:
    cookietrackers = cookielist.readlines()
cookierules = AdblockRules(cookietrackers)

with open("easysocial.txt", encoding="utf8") as sociallist:
    socialtrackers = sociallist.readlines()
socialrules = AdblockRules(socialtrackers)

# with open("easyannoyance.txt", encoding="utf8") as annoyanclist:
# annoyanctrackers = annoyanclist.readlines()
# annoyancrules = AdblockRules(annoyanctrackers)


print("easy-list:")
for data in datalist:
    if easyrules.should_block(data):
        easytrackerlist.append(data)
    if privacyrules.should_block(data):
        privacytrackerlist.append(data)
    if cookierules.should_block(data):
        cookietrackerlist.append(data)
    if socialrules.should_block(data):
        socialtrackerlist.append(data)

print(easytrackerlist)
print(len(easytrackerlist))

print("privacy-list:")
print(privacytrackerlist)
print(len(privacytrackerlist))

print("cookie-list:")
print(cookietrackerlist)
print(len(cookietrackerlist))

print("social-list:")
print(socialtrackerlist)
print(len(socialtrackerlist))

print("cookie-list:")
print(cookietrackerlist)
print(len(cookietrackerlist))

print("annoyanc-list:")
# for data in datalist:
# if annoyancrules.should_block(data):
#     annoyanctrackerlist.append(data)

# print(annoyanctrackerlist)
# print(len(annoyanctrackerlist))