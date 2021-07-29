from tag_manipulator import TagManipulator

'''
"java" must return ["java"]

"java, python" must return ["java", "python"]

" java" must return ["java"]

",java" must return ["java"]

"java," must return ["java"]

"java byte code, python" must return must return ["java byte code", "python"]

'''
def test_split_empty_string_result_empty_array():
    # arrange
    stringToSplit = ""
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult


def test_split_comma_empty_string_result_empty_array():
    # arrange
    stringToSplit = ","
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult


def test_split_one_string_result_array_of_one():
    # arrange
    stringToSplit = "java"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult


def test_split_one_string_with_splitter_result_array_of_one():
    # arrange
    stringToSplit = "java,"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult


def test_split_start_space_with_splitter_result_array_of_one():
    # arrange
    stringToSplit = " java"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult

def test_split_start_comma_space_with_splitter_result_array_of_one():
    # arrange
    stringToSplit = ", java"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult

def test_split_start_comma_space_with_splitter_result_array_of_one():
    # arrange
    stringToSplit = "java byte code, python"
    regex = ","
    expResult = ["java byte code", "python"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult