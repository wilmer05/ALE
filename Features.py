class Features:
    
    def __init__(self, features_list = []):
        self.features_list = features_list

    def __hash__(self):
        #print len(self.features_list)
        return hash(str(self.features_list))

    def __iter__(self):
        return iter(self.features_list)
