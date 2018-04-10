def isPalindrome(product):
    productString=str(product)
    for i in range(int(len(productString)/2)):
        if (productString[i]!=productString[len(productString)-1-i]):
            return False
    return True

product=0
answer=0
for i in range(100,999):
    for j in range(100,999):
        product=i*j
        if(isPalindrome(product) and (product>answer)):
            answer=product
print(answer)