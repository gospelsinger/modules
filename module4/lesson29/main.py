class MyDict:
    def __init__(self):
        self.dict_keys = []
        self.dict_values = []

    def __getitem__(self, key):
        if key not in self.dict_keys:
            return None
        return self.dict_values[self.dict_keys.index(key)]

    def __setitem__(self, key, value):
        if not isinstance(key, (int, float, str, tuple)):
            raise TypeError(f"unhashable type: '{type(key).__name__}'")

        if key in self.dict_keys:
            self.dict_values[self.dict_keys.index(key)] = value
        else:
            self.dict_keys.append(key)
            self.dict_values.append(value)

    def __delitem__(self, key):
        if key in self.dict_keys:
            pos = self.dict_keys.index(key)
            del self.dict_keys[pos]
            del self.dict_values[pos]

    def __contains__(self, key):
        return key in self.dict_keys

    def keys(self):
        return self.dict_keys

    def values(self):
        return self.dict_values

    def items(self):
        return list(zip(self.dict_keys, self.dict_values))

    def __str__(self):
        return "{" + ", ".join([f"{k}: {v}" for k, v in self.items()]) + "}"


my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict.items())  # Вернет [('name', 'Alice'), ('age', 30)]
print(my_dict['name'])  # Вернет 'Alice'
print(my_dict['city'])  # Вернет None
print(my_dict)  # Вернет {name: Alice, age: 30}
print('city' in my_dict)  # Вернет False
print('age' in my_dict)  # Вернет True
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']
print(my_dict.items())  # Вернет [('name', 'Alice')]