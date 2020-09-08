import re
text = "https://www.i2tutorials.com/match-urls-using-regular-expressions-in-python/"
pattern = r"(http|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?"
print("Hello: ",text)
if re.match(pattern,text):
    print("Url: ",text)
else:
    print("Error")