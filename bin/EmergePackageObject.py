#!/usr/bin/env python

class PackageObjectBase(object):

    def __init__(self, category=None, subpackage=None, package=None, enabled=False, version = ""):
        self.category = category
        self.subpackage = subpackage
        self.package = package
        self.enabled = enabled
        self.version = version

    def fullName(self):
        if self.subpackage:
            return "%s/%s/%s" % (self.category,self.subpackage,self.package)
        else:
            return "%s/%s" % (self.category,self.package)


    def __eq__(self, other):
        #print("eq", type(other), other)
        if isinstance(other, PackageObjectBase):
            if other.package == self.package and other.category == self.category and other.subpackage == self.subpackage:
                return True
        if isinstance(other, str):
            if other == self.package:
                return True
            if other == self.fullName():
                return True
        return False

    def __str__(self):
        return self.fullName()

    def __bool__(self):
        #print("bool:", self.enabled)
        return self.enabled
