# movies=["star","GOT","GLC"]
# print(movies)
# print(len(movies))
# movies.append("KOK")
# print(movies)
# movies.pop()
# print(movies)
# movies.insert(0,"Twilight")
# print("This a  new inserted item")
# print(movies)
# movies.remove("Twilight")
# print("A item has been removed")
# print(movies)
# movies.append("coolio")
# print(movies)
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman", ["Michael Palin", ["John Cleese",
["Terry Gilliam", ["Eric Idle", "Terry Jones"]]]]]]
#print(movies)
#print(movies[4][1][3])
# for i in movies:
#     if (isinstance(i,list)):
#         for j in i:
#             if (isinstance(j,list)):
#                 for k in j:
#                     print(k)
#             else:
#                 print(j)          
#     else:
#         print(i)


def mylistFunction(my_list):
    for i in my_list:
        if(isinstance(i,list)):
            mylistFunction(i)
        else:
            print(i)

mylistFunction(movies)