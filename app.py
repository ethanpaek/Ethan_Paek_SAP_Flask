"""
Ethan Paek
October 20th, 2020

This is Ethan Paek's Amazingly Awesome Flask App!

Please refer to the following for this app's URL paths:
/<int:number> will display integers from 1 to that number
/<int:number>/odd will display only odd numbers in that range
/<int:number>/even will display only even numbers in that range
/<int:number>/prime will display only prime numbers in that range
"""

from flask import Flask, render_template

app = Flask(__name__)


# Note: I was planning to use this first commented-out function for code re-usability.
# However, I realized that it would actually require more computation time and take up more memory!

# def generate_num_list(num_input):
#     """
#     This will generate a list of numbers between 1 and num_input
#     :param num_input: <int> an integer whose value is greater than zero
#     :return: a list of numbers between 1 and num_input
#     """
#     # need to check if input number is less than 1!
#     if num_input < 1:
#         return "There aren't any numbers to print since yours is less than 1!"
#
#     # now we can simply append everything between 1 and the number's value to a list
#     num_list = []
#     for num in range(1, num_input + 1):
#         num_list.append(num)
#     return num_list


@app.errorhandler(404)
def page_not_found(e):
    """
    This function will return a 404 error code, indicating that we did not provide an integer for the parameter
    """
    return "You did not enter a valid number. Please try again!", 404


@app.route('/')
def home():
    """
    This is our basic homepage!
    :return: str
    """
    return "Welcome to Ethan Paek's Amazingly Awesome Flask App!"


@app.route('/<int:number>')
def number_list(number):
    """
    This URL path is designed to print out every number from 1 to the number's value
    :param number: <str> user input for any number of their choosing
    :return: a string with an error message or all numbers between 1 and the number's value
    """
    # numbers = generate_num_list(number)

    # need to check if input number is less than 1!
    if number < 1:
        return "There aren't any numbers to print since yours is less than 1!"

    # append everything between 1 and the number's value to a list
    numbers = []
    for num in range(1, number + 1):
        numbers.append(num)

    # return the HTML template to print out number list
    return render_template("number.html", numbers=numbers)


@app.route('/<int:number>/odd')
def odd_number_list(number):
    """
    This URL path is designed to print out every odd number from 1 to the number's value
    :param number: <str> user input for any number of their choosing
    :return: a string with an error message or all odd numbers between 1 and the number's value
    """
    # numbers = generate_num_list(number)

    # need to check if input number is less than 1!
    if number < 1:
        return "There aren't any numbers to print since yours is less than 1!"

    numbers = []
    for num in range(1, number + 1):
        # only append numbers that do not evenly divide by 2
        if num % 2 == 1:
            numbers.append(num)

    return render_template("number.html", numbers=numbers)


@app.route('/<int:number>/even')
def even_number_list(number):
    """
    This URL path is designed to print out every even number from 1 to the number's value
    :param number: <str> user input for any number of their choosing
    :return: a string with an error message or all even numbers between 1 and the number's value
    """
    # numbers = generate_num_list(number)

    # need to check if input number is less than 1!
    if number < 1:
        return "There aren't any numbers to print since yours is less than 1!"

    numbers = []
    for num in range(1, number + 1):
        # only append numbers that evenly divide by 2
        if num % 2 == 0:
            numbers.append(num)

    return render_template("number.html", numbers=numbers)


@app.route('/<int:number>/prime')
def prime_number_list(number):
    """
    This URL path is designed to print out every prime number from 1 to the number's value
    :param number: <str> user input for any number of their choosing
    :return: a string with an error message or all prime numbers between 1 and the number's value
    """
    # numbers = generate_num_list(number)

    # need to check if input number is less than 2!
    if number < 2:
        return "There aren't any numbers to print since yours is less than 2! (One is not a prime. I know, it's weird)"

    numbers = []

    # to find our prime numbers, we can use the Sieve of Eratosthenes
    # Source: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode
    sieve = [True] * (number + 1)
    for i in range(2, number + 1):
        # if sieve is true for a given number, we can add it to our list!
        if sieve[i]:
            numbers.append(i)
            # we set any multiples within our range to false (so we don't add them to the list)
            for j in range(i, number + 1, i):
                sieve[j] = False

    return render_template("number.html", numbers=numbers)


if __name__ == '__main__':
    # By default, this will run on port 5001 in Docker
    app.run(host='0.0.0.0', debug=True)
