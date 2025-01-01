# Python code​​​​​​‌‌​​​‌‌​​​​‌‌​‌‌​‌‌​‌‌​​‌ below
# Use print("messages...") to debug your solution.

show_expected_result = True
show_hints = True

def is_palindrome(teststr):
    # Your code goes here.
    #return False

    finished = False
    capstring = str.upper(teststr)
    i = 0;
    j = len(capstring)-1;
    print("i, j, capstring",i,j,capstring)

    while i < j:
        print("In while loop, i, j, capstring", i, j, capstring)
        if str.isalpha(capstring[i]) :
            print("i is alpha", i, capstring[i])
        else :
            print("i is not alpha", i, capstring[i])
            i = i + 1
            continue

        if str.isalpha(capstring[j]) :
            print("j is alpha", j, capstring[j])
        else :
            print("j is not alpha", j, capstring[j])
            j = j -1
            continue
 
        print("see if capstring[i] equals capstring[j]", i, j, capstring)
        if capstring[i] == capstring[j] :
            print("yes...so far")
            i = i+1
            j=j-1
        else:
            print("no...return false")
            return(False)
    
    return(True)
    
name = input("Enter phrase: ")
result = is_palindrome(name)
print("Is a palindrome?", result)

