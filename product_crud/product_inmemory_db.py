class ProductInMemoryDb:
    ''' Product In Memory Class'''
    product_list:list=[]

    def __init__(self,data:dict):
        self.data = data
        
    def add(data:dict=None) -> int:
         if data is None:
            data = self.data
        self.product_listdb.append(data)
        return 1
    
    def update(self,data:dict=None) -> int:
        for item in self.product_list:
            if item['id']==id:
                if data is None:
                    data = self.data
                item.update(data)
                return 1
        return 0

    def find_by_id(id:int) -> dict:
        next(item for item in product_list if item['id']==id)  

    def remove(data:dict) -> int:
        for item in cls.product_list:
            if item['id']==id:
                dict.remove(item)
