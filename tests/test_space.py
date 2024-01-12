from lib.space import Space

"""
Space constructs with an id, soace_name and space_description, price, host_id
"""
def test_space_constructs():
    space = Space(1, "test_space_name", "test_space_description", 2, 1)
    assert space.id == 1
    assert space.space_name == "test_space_name"
    assert space.space_description == "test_space_description"
    assert space.price == 2
    assert space.host_id == 1
    

"""
We can format spaces to strings nicely
"""
def test_spaces_format_nicely():
    space = Space(1, "test_space_name", "test_space_description", 2, 1)
    assert str(space) == "Space(1, test_space_name, test_space_description, 2, 1)"
    # Try commenting out the `__repr__` method in lib/space.py
    # And see what happens when you run this test again.

"""
We can compare two identical spaces
And have them be equal
"""
def test_spaces_are_equal():
    space1 = Space(1, "test_space_name", "test_space_description", 2, 1)
    space2 = Space(1, "test_space_name", "test_space_description", 2, 1)
    assert space1 == space2
    # Try commenting out the `__eq__` method in lib/space.py
    # And see what happens when you run this test again.

