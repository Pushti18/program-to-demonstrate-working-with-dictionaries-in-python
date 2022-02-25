//07. Write a program to demonstrate working with dictionaries in python.
brand = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for k, v in brand.items():
  if(k == 'year'):
    print(v)