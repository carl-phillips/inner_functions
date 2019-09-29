def measurements(measurements):
    def area(a_list):
        return a_list[0] * a_list[1]

    def perimeter(a_list):
        return 2 * (a_list[0] + a_list[1])

    print("Perimeter = " + str(perimeter(measurements)) + " Area = " + str(area(measurements)))


if __name__ == '__main__':
    measurements([2.1, 3.4]) 
