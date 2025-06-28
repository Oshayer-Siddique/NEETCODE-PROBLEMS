print("Boats to Save People")

def function(people , limit):

    people.sort()

    n = len(people)

    cnt  = 0

    i = 0
    j = n-1
    while(i <= j):
        if(people[i] + people[j] <= limit):
            i = i + 1
            j = j - 1            
            cnt = cnt+1
        else:
            j = j - 1
            cnt = cnt + 1
    return cnt


people = [5,1,4,2]
limit = 6

print(function(people = [1,3,2,3,2],limit = 3))

        
        
