def bonAppetit(bill, k, b):
     s=sum(bill)
     ba=(s-bill[k])//2
     if ba==b:
        print("Bon Appetit")
     else:
        print(int(b-ba))
 
