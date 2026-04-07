class flipkart:
    #class att
    discount = 10

    @classmethod
    def udatediscount(cls,new_discount):
        cls.discount=new_discount


    @staticmethod
    def wlcome():
        print('welcome to the flipkart')

    def myorder(sel,order_id):
        #instance att
        sel.order_id=order_id
        print(f"you have order these product with id:(self.order_id)")
