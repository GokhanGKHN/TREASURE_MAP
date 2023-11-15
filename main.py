"""
Instructions
This is a difficult challenge. 💪

You are going to write a program that will mark a spot on a map with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what it looks like, notice the nesting:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']
Now it looks a bit more like the coordinates of a real map:

Map Coordinates Example

Your job is to write a program that allows you to mark a square on the map using a letter-number system.

List coordinates

So an input of A3 should place an X at the position shown below:

Exmaple location

First, your program must take the user input and convert it to a usable format.

Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
Example Input 1
B3
Example Output 1
Hiding your treasure! X marks the spot.
['⬜️', '️⬜️', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', 'X', '⬜️️']
Example Input 2
B1
Example Output 2
Hiding your treasure! X marks the spot.
['⬜️', 'X', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', '⬜️️', '⬜️️']
Hints
See if this List method helps you: https://www.w3schools.com/python/ref_list_index.asp

Remember that nested Lists in Python are accessed from outside to inside. e.g. In the List below:

list = [['A', 'B, 'C'], 'E', 'F', 'G']
E is list[1] C is list[0][2]

Check your formatting. This is correctly formatted:
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']
vs.

Incorrectly formatted (missing a space before 'X and extra space after the X and extra space before the comma):

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️','X ' , '⬜️']

"""






line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
# Your code below
#Aşağıda önce position üzerinden gelen girdiyi lower metodu ile 0.indisini örneğini B3 için (b) yi küçük harf yapalım. 
letter = position[0].lower()
#Daha sonra abc dizisi oluşturuyoruz. 
abc = ["a", "b", "c"]
#Ekteki harita x yatay endekste ABC dikey endekste 123 olduğu için x ve y ayrı değişkenler oluşturuyoruz. 
#letter değişkenine kullanıcıdan alldığımız letter'ı yani (b)'nin abc dizisinde bulunduğu konumu index metodu-
#ile bulduktan sonra konumdaki indisi yani (b) 1.indekste, 1'i letter_index'e atıyoruz. 
letter_index = abc.index(letter)
#Kullanıcıdan aldığımız position verisinin birinci index'sini yani B3'ün 3'nü bir eksiterek number_index atıyoruz
# Burada neden -1 çünkü index 0'dan başlar kullanıcı ise bu bilgiyi bilmez. :D 
number_index = int(position[1]) - 1
#Son map dizisindeki konuma X değerini yazabilmek için letter_index'deki değeri 1 position girdisindeki birinci 
# indisi yani 3 map dizisinde konumlandırıp bu konuma X değerini atıyoruz. 
# Yazım parçalayıp tekrar birleştirmekle ilgili bir programı kavrayabilmek için önce parçlayıp sonra birleştirmek gerekir. 
map[number_index][letter_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")