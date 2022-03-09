# Class defines
class Array:
  def __init__(self, list):
    self.list = list

  def value(self):
    return self.list

  def push(self, item):
    self.list.append(item)

    return Array(self.list)

  def map(self, callback):
    values = []
    for index in range(len(self.list)):
      values.append(callback(self.list[index], index))

    return Array(values)

  def forEach(self, callback):
    for index in range(len(self.list)):
      callback(self.list[index], index)

    return

  def find(self, callback):
    for item in self.list:
      if not not callback(item):
        return item

  def filter(self, callback):
    values = []
    for item in self.list:
      if not not callback(item):
        values.append(item)

    return Array(values)

  @staticmethod
  def isArray(value):
    arrayTypes = [list, set, tuple]
    return type(value) in arrayTypes

class Object:
  def __init__(self, object):
    self.object = object
  
  def value(self):
    return self.object

  @staticmethod
  def keys(object):
    return [key for key in object]

  @staticmethod
  def values(object):
    return [object[key] for key in object]

  @staticmethod
  def entries(object):
    return [[key, object[key]] for key in object]

people = Array([
  {
    "name": "Bernardo",
    "age": 20,
    "city": "Novo Hamburgo"
  },
  {
    "name": "Gabriel",
    "age": 22,
    "city": "Novo Hamburgo"
  },
  {
    "name": "Camila",
    "age": 19,
    "city": "São Leopoldo"
  }
])

print("Everyone: ")
people.forEach(
  lambda item, index:  
    print(Object.entries(item))
)

Bernardo = people.find(lambda person: person["name"] == "Bernardo")
print("\nBernardo: ")
print(Bernardo)

NHPeople = people.filter(lambda person: person["city"] == "Novo Hamburgo")
print("\nNH people: ")
NHPeople.forEach(lambda item, index: print(item))

NHPeople.push({
  "name": "Julia",
  "age": 25,
  "city": "Novo Hamburgo"
})

print("\nNew NH People: ")
NHPeople.forEach(lambda item, index: print(item))

# Ternary Operation
def isInteger(value):
  return "Is an integer" if type(value) == int else "Is not an integer"

isInteger(5) # Is an integer
isInteger("Hello, world") # Is not an integer