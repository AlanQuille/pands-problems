Weekly tasks
=======

2-bmi.py
-------
The script is designed to calculate body mass index or BMI.

This script sets the variables **weight** and **height** using the user's input. The user's input is first converted to floating point numbers using the **float** function.

The height is converted from cm to m<sup>2</sup> using the following formula: height = (height/100)<sup>2</sup>

The body mass index (**bmi**) is then calculated and return using the following formula: bmi = weight/height

The function then returns bmi formatted to two decimal places using the **round** function.

3-secondstring.py
-------
The script is designed to take a sentence the user inputs, turn it backwards and take only every second letter starting from the last character and ending with the first one. So for instance "Backwards" becomes "srwc"

This script sets the variable **input_string** using the user's input. The input is first converted to a string using the **str** function.

The **output_string** variable is set using a slice of the string **input_string**. The slice goes from the last letter to the first letter in steps of 2 backwards.

The resulting string **output_string** is printed to the screen using the **print** function.


4-collatz.py
-------
This script sets the variable **any\_pos\_int** using the user's input. The input is first convert to an integer using the **int** function.

The script runs an if statement whcih runs as follows:

 If **any\_pos\_int** is not an integer, the user is informed using the **print** function which prints a warning to the screen. If **any\_pos_int** is an integer then **any\_pos\_int** is printed to the screen with a blank space afterwards and a while loop is run. 

This loop terminates if **any\_pos\_int** becomes larger than 1. In the loop, it checks whether **any\_pos\_int** divides evenly into 2 (i.e. is an even number). If it does, it divides **any\_pos\_int** by 2 and converts it to an integer using the **int** function. If it does not divide evenly into 2, then **any\_pos_int** is trebled and 1 is added to the result, which is then converted to an integer.

Before the loop terminates **any\_pos_int** is printed to the screen with a blank space afterwards.