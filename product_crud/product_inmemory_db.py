class ProductInMemoryDb:
    product_list=[]

    def __init__(self,data:dict):
        self.data = data
        
    def add(data:dict | None) -> int:
        product_list.append(data)
        return 1
    
    def update(data:dict | None) -> int:
        for item in cls.product_list:
            if item['id']==id:
                item.update(data)
                return 1

    def find_by_id(id:int) -> dict:
        next(item for item in product_list if item['id']==id else {})

    def remove(data:dict) -> int:
        for item in cls.product_list:
            if item['id']==id:
                dict.remove(item)
