def measurements(measurements):
    def area(a_list):
        return a_list[0] * a_list[1]

    def perimeter(a_list):
        return 2 * (a_list[0] + a_list[1])

    def area_square(a_list):
        return a_list[0] * a_list[0]

    def perimeter_square(a_list):
        return 4 * a_list[0]

    if len(measurements) == 1:
        return ("Perimeter = " + str(perimeter_square(measurements)) + " Area = " + str(area_square(measurements)))
    elif len(measurements) == 2:
        return ("Perimeter = " + str(perimeter(measurements)) + " Area = " + str(area(measurements)))


if __name__ == '__main__':
    print(measurements([2.1, 3.4]))
