import json
x =  '{ "name":"John", "age":30, "city":"New York"}'

 # parse x
y = json.loads(x)
print(y["age"])


x1 = {
  "name": "John",
  "age": 30,
  "city": "New York",
  "phone" : 134321403
}
print("\n")
y1 = json.dumps(x1)
print(y1)

# Writing to sample json
with open("Sample.json", "w") as outfile:
    outfile.write(y1)



## Reading json from a file
print("\n")
with open("sample.json", "r") as sudhanva:
    json_object = json.load(sudhanva)

print(json_object)
print(type(json_object))