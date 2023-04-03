import math

class Pagination:
    def __init__(self, items=[], pageSize = 10):
        self.items = items
        self.pagesize = pageSize
        self.startpoint = 0
        self.totalPages = math.ceil(len(items) / pageSize)
        self.currentPage = 1

    def getVisibleItems(self):
        return self.items[self.startpoint: self.startpoint + self.pagesize]

    def prevPage(self):
        if self.currentPage >1:
            self.startpoint -= self.pagesize
            self.currentPage -= 1
        return self

    def nextPage(self):
        if self.currentPage < self.totalPages:
            self.startpoint += self.pagesize
            self.currentPage +=1
        return self

    def firstPage(self):
        self.currentPage = 1
        self.startpoint = 0
        return self

    def lastPage(self):
        self.startpoint = self.pagesize * (self.totalPages - 1)
        self.currentPage = self.totalPages
        return self

    def goToPage(self,n):
        if n > self.totalPages:
            n = self.totalPages
        elif n <= 0:
            n = 1
        self.currentPage = n
        self.startpoint = self.pagesize*(n-1)
        return self

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(p.getVisibleItems())
p.nextPage().nextPage()
print(p.getVisibleItems())
print(p.totalPages)
print(p.currentPage)
p.goToPage(6)

print(p.getVisibleItems())