# imports here if necessary
from random_thousand import random_thousand
from nose.tools import assert_raises, assert_almost_equal
# lets create some tests!
def test_defined_range():
    """create a test that throws an appropriate exception if upper_bound is less than lower_bound
    """
    nose.tools.assert_raises(ValueError, generate_values(), [], [2.0, 1.0])
    nose.tools.assert_raises(ValueError, generate_values(), [], [10.0, 1.0])
    nose.tools.assert_raises(ValueError, generate_values(), [], [200.0, 3.0])
    nose.tools.assert_raises(ValueError, generate_values(), [], [0.01, 0.001])

def test_length():
    """make sure that the function returns the right number of values (we wanted 1000)
    """
    assert len(generate_values()) == 1000
    assert len(generate_values(0.0, 1.0)) == 1000
    assert len(generate_values(1.0, 100.0)) == 1000
    assert len(generate_values(3.0, 20.0)) == 1000

def test_boundaries():
    """create a test that checks that every value of the return is within an expected range. 
    """
    #Test this for a few different ranges. (Hint: you may need to make another method to help you do this)
    assert _test_boundaries_helper(generate_values(0.0, 1.0), 0.0, 1.0) == True
    assert _test_boundaries_helper(generate_values(-1.0, 1.0), -1.0, 1.0) == True
    assert _test_boundaries_helper(generate_values(-5.0, -1.0), -5.0, -1.0) == True
    assert _test_boundaries_helper(generate_values(-1.0, -100.0), -1.0, -100.0) == True

def _test_boundaries_helper(array, lower_bound, upper_bound):
    """iterates through an array to check if all values are within the lower and upper bound range of floats
    """
    for n in array:
        if n < lower_bound or upper_bound < n:
            return False
    return True

def test_uniform_distribution1():
    """test that the median value is roughly the value that is halfway between the lower and upper boundary.
    """
    nose.tools.assert_almost_equal(_get_mean(generate_values(0.0, 1.0)), get_mean([0.0, 1.0]))
    nose.tools.assert_almost_equal(_get_mean(generate_values(-1.0, 1.0)), get_mean([-1.0, 1.0]))
    nose.tools.assert_almost_equal(_get_mean(generate_values(-50.0, 1.0)), get_mean([-50.0, 1.0]))
    nose.tools.assert_almost_equal(_get_mean(generate_values(0.0, 100.0)), get_mean([0.0, 100.0]))

def _get_mean(list):
    """calculates and returns average from list of floats
       also works for 1-dimmensional numpy arrays
    """
    ave = 0.0
    for n in list:
        ave += n
    return ave / len(list)

def test_uniform_distribution2():
    """create a test that will show that the mean value is roughly the median value. 
    """
    #This can be done either with nose.tools.assert_almost_equal or by checking 
    # that the mean is within a small range centered on the median.
    arr1 = generate_values(0.0, 1.0)
    nose.tools.assert_almost_equal(arr1.mean(), arr1.median())
    arr2 = generate_values(-1.0, 1.0)
    nose.tools.assert_almost_equal(arr2.mean(), arr2.median())
    arr3 = generate_values(-50.0, 1.0)
    nose.tools.assert_almost_equal(arr3.mean(), arr3.median())
    arr4 = generate_values(0.0, 100.0)
    nose.tools.assert_almost_equal(arr4.mean(), arr4.median())

def test_return_type():
    """create a test that assures the return value type is a numpy array
    """
    nose.tools.assert_is_instance(generate_values(0.0, 1.0), np.ndarray)
    nose.tools.assert_is_instance(generate_values(-1.0, 1.0), np.ndarray)
    nose.tools.assert_is_instance(generate_values(-50.0, 1.0), np.ndarray)
    nose.tools.assert_is_instance(generate_values(0.0, 100.0), np.ndarray)

# The next test is very challenging, requiring you to look into matplotlib documentation
# As a result, this next test is optional
def test_uniform_distribution3():
    # create a histogram plot of the random values. Make sure that the smallest histogram bin is
    # roughly the same size of the largest histogram bin. Choose a bin count large enough to show
    # a reasonable amount of detail, but no so many that the bins look sparse.