class foodorder:
    def show_order(self,restaurant_name,items,total_price):
        print("restaurant name:",restaurant_name)
        print("items :",items)
        print("total price",total_price)
r=input("enter the resturant name :").split(",")
i=input("enter the items :").split(",")
t=input("enter the total price :").split(",")
f=foodorder()
f.show_order(r,i,t)