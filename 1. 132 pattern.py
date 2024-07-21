#  see web
#%%
class solution:
    def find132pattern(self, num):
        index = {}
        seq = [231]
        for pos, i in enumerate(num):
            if seq and i==seq[-1]:
                index[i]=pos
                seq.pop()
        
        return index[1]<index[3]<index[2]
