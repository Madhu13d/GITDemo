ItemsInCart =0
#2 items will be added to cart

if ItemsInCart != 2:#   raise Exception("Products Cart could not matching")
    pass

assert(ItemsInCart ==0)
#try, catch
# here we are printing user customized message
try:
    with open('filelog.txt','r') as reader:
        reader.read()

except:
    print("Some how I reached this block because there is failure in try block")

# Here we are printing the message which python has thrown
try:
    with open('test.txt','r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up resources")
