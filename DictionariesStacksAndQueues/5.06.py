def two_dicts_combiner(dict1, dict2):
    dict3 = dict1 | dict2
    return dict3


if __name__=='__main__':
   
   dict1 = {
      "name": "Barbara",
      "age": 21
   }

   dict2 = {
      "status": "student",
      "married": False,
      "interest": ["reading", "swimming"]
}
   
   person = two_dicts_combiner(dict1, dict2)
   for key, value in person.items():
       print(f"{key}: {value}")

