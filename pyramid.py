def pyramid():
    another = 'yes'
    while another.lower() == 'yes':
        n = int(input('How many rows would you like the pyramid to have?' ))
        for i in range(n):
            pyramid_row = " " * (n - 1 - i) + 'X' * (1 + 2 * i)
            print(pyramid_row)
        another = input("Would you like to make another pyramid? ['Yes'/'No'] ")

pyramid()