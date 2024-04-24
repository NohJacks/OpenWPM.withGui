import matplotlib.pyplot as plt

import numpy as np
from adblockparser import AdblockRules

class CookieComparator():
    def __init__(self, name):
        self.load_trackers()
        self.name = name

    def setDatalist(self, datalist):
        self.datalist = datalist

        ('{}.txt'.format(self.name))


    def load_trackers(self):
        self.trackers = []
        self.easytrackerlist = []
        self.privacytrackerlist = []
        self.cookietrackerlist = []
        self.socialtrackerlist = []
        self.annoyanctrackerlist = []

        with open("easylist.txt", encoding="utf8") as easylist:
            self.easytrackers = easylist.readlines()
        self.easyrules = AdblockRules(self.easytrackers)

        with open("easyprivacy.txt", encoding="utf8") as privacylist:
            self.privacytrackers = privacylist.readlines()
        self.privacyrules = AdblockRules(self.privacytrackers)

        with open("easycookie.txt", encoding="utf8") as cookielist:
            self.cookietrackers = cookielist.readlines()
        self.cookierules = AdblockRules(self.cookietrackers)

        with open("easysocial.txt", encoding="utf8") as sociallist:
            self.socialtrackers = sociallist.readlines()
        self.socialrules = AdblockRules(self.socialtrackers)

        # with open("easyannoyance.txt", encoding="utf8") as annoyanclist:
        # self.annoyanctrackers = annoyanclist.readlines()
        # annoyancrules = AdblockRules(self.annoyanctrackers)

    def compare(self):
        print("running compare.")
        "skal der self. på data og datalist?"
        for data in self.datalist:
            if self.easyrules.should_block(data):
                self.easytrackerlist.append(data)
            if self.privacyrules.should_block(data):
                self.privacytrackerlist.append(data)
            if self.cookierules.should_block(data):
                self.cookietrackerlist.append(data)
            if self.socialrules.should_block(data):
                self.socialtrackerlist.append(data)

        print("easy-list:")
        print(self.easytrackerlist)
        print(len(self.easytrackerlist))
        print(len(self.datalist))

        dataLen = len(self.datalist)
        easyLen = len(self.easytrackerlist)


        division_result1 = dataLen/easyLen

        proportion1 = division_result1 / (division_result1 + 1)

        proportion2 = 1 / (division_result1 + 1)

        # Create a pie chart

        labels = ['Length 1', 'Length 2']
        sizes = [proportion1, proportion2]
        colors = ['blue', 'red']
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
        plt.show()

        print("privacy-list:")
        print(self.privacytrackerlist)
        print(len(self.privacytrackerlist))

        print("cookie-list:")
        print(self.cookietrackerlist)
        print(len(self.cookietrackerlist))

        print("social-list:")
        print(self.socialtrackerlist)
        print(len(self.socialtrackerlist))

        print("cookie-list:")
        print(self.cookietrackerlist)
        print(len(self.cookietrackerlist))

