import time
starttime = time.time()
# for i in range(10):
#     # Code executed here
#     time.sleep(1)
#     print("hello")


while True:
    i = 1
    Text = "{}".format(i) 
    time.sleep(5.0 - ((time.time() - starttime) % 5.0))
    print(i)