def book_movie_ticket():
    balance=2000

    try:
        ticket=int(input("enter tickets :"))
        print("price per ticket :",balance/ticket)
    except ZeroDivisionError:
        print("money is 0")
    except ValueError:
        print("enters numbers only")
book_movie_ticket()