import datetime
from product import Product

def main():

    currentdatetime = datetime.datetime.utcnow()
    current_unixtimestamp = int(currentdatetime.timestamp())

    product_one = Product('Lenovo T410s',
        'Lenovo ThinkPad T410s Core i5 M560 2.66GHz 4GB RAM, WIN 10 14" AC ADAPTER',
        'The T410s provides a good companion for office use, that is well suited for business trips thanks to its 14.1 inch size and light weight.',
        'thinkbook-13x-gen-2-(13-inch-intel)',
        'https://www.lenovo.com/gb/en/p/laptops/thinkbook/thinkbookx/thinkbook-13x-gen-2-(13-inch-intel)/21atcto1wwgb2?cid=gb:sem|se|google|G-UK-SEM-COMMERCIAL-PUBLIC-CCF-LF-Shopping-PLA-Brand-Commercial|Brand-CommercialLaptops-Intel',
        '21ATCTO1WWGB2',
        799.95,
        849.95,
        0,
        False,
        4,
        current_unixtimestamp,
        current_unixtimestamp,
        1)


    product_two = Product('Lenovo T530',
        'Lenovo 530',
        'some long descrition',
        'thinkbook-530',
        'https://www.lenovo.com/gb/en/p/laptops/thinkbook/530',
        'X394UB83NJ',
        689.95,
        549.95,
        0,
        False,
        8,
        current_unixtimestamp,
        current_unixtimestamp,
        1)

    product_one.create(1000)
    # product_two.create(1001)
    
    product_two.create(1001)
    # product_one.title = "Sony 500"
    # print(product_one.update())
    # product_one.read_by_title("Lenovo T410s")
    # product_one.title = "Lenovo TUR"
    # print(product_one.update())
    # product_one.update()
    


    # product_one.read_by_title("Lenovo T530")

    print(product_one.list_all())




   # print("Does Product one instance of <<Circle>> class?")
    # print(isinstance(product_one, Circle))
   # print("Does Product one instance of <<Product>> class?")
    # print(isinstance(product_one, Product))


   # del product_one
   # del product_two

    #for p in Product.list_all():
    #    print(p)

    #print(Product._product_list)

if __name__ == '__main__':
    main()
