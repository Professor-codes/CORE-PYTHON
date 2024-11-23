# keys method return a list of all the keys in dictionary
color = {
    "code1": "#FF00FF",
    "code2": "#8A2BE2",
    "code3": "#00FF7F",
}
print(color.keys())

# adding a new term
color["code4"] = "#DC143C"
print(color.keys())
color["code5"] = "#00FFFF"
print(color.keys())

# verify the new adding value
print(color["code4"])
print(color["code5"])



