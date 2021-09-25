class Children():

  is_adult = False

  def __init__(self, name, surname, age):
    self.name = name
    self.surname = surname
    self.age = age

  @property
  def complete_name(self):
    return "{} {}".format(self.name, self.surname)

  @complete_name.setter
  def complete_name(self, name_surname):
    name, surname = name_surname.split(" ")
    self.name = name
    self.surname = surname