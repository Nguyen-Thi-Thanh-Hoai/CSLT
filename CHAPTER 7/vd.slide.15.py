# st1=input("")
# while True:
#     st2=input()
#     if st2 not in st1:
#         break

original_string = "Hello ,       World!"
words = original_string.split()
no_space_string = "".join(words)
print(no_space_string)