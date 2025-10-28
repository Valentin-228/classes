class Group:
    pupils = True
    scholl_name = 42
    director = "Mariyvanna"


class PrimaryGroup(Group):
    max_age = 11
    min_age = 6
    building_section = 'left'

class HightGroup(Group):
    max_age = 18
    min_age = 14

first_a = PrimaryGroup()
eleven_a = HightGroup()


