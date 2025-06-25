print("Lemonade Change")

def function(bills):
    total = sum(bills)
    if total % 10 == 0:
        return False
    else:
        return True
    
bills = [5,10,5,5,20]
print(function(bills))
