import main


def test_square():
    square = main.Square()

    assert square.is_inside(2, 1) == False


def test_monte_carlo_area_calculator():
    square = main.Square()

    MCA_calculator = main.MonteCarloAreaCalculator(square)
    allowed_error = 0.01
    true_area = 0.25
    calced_area = MCA_calculator.calc_area()
    print(f"calculated area = {calced_area}, true area = {true_area}")
    assert (
        calced_area < true_area + allowed_error
        and calced_area > true_area - allowed_error
    )
