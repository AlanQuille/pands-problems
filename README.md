Weekly tasks
=======

2-bmi.py
-------
The script is designed to calculate body mass index or BMI.

This script sets the variables **weight** and **height** using the user's input. The user's input is first converted to floating point numbers using the **float** function.

The height is converted from cm to m<sup>2</sup> using the following formula:

 **height** = (**height**/100)<sup>2</sup>

The body mass index (**bmi**) is then calculated and returned using the following formula: 

**bmi** = **weight**/**height**

The function then returns bmi formatted to two decimal places using the **round** function.

3-secondstring.py
-------
The script is designed to take a sentence the user inputs, turn it backwards and take only every second letter starting from the last character and ending with the first one. So for instance "Backwards" becomes "srwc"

This script sets the variable **input_string** using the user's input. The input is first converted to a string using the **str** function.

The **output_string** variable is set using a slice of the string **input\_string**. The slice goes from the last letter to the first letter in steps of 2 backwards.

The resulting string **output_string** is printed to the screen using the **print** function.


4-collatz.py
-------

This script is designed to take a positive integer and either divide it by two if it is even or multiply it by three and add 1 otherwise. In either case the result is printed to the screen. This continues until the positive integer becomes 1.

This script sets the variable **any\_pos\_int** using the user's input. The input is first convert to an integer using the **int** function.

The script runs an if statement which runs as follows:

 If **any\_pos\_int** is not an integer, the user is informed using the **print** function which prints a warning to the screen. If **any\_pos_int** is an integer then **any\_pos\_int** is printed to the screen with a blank space afterwards and a while loop is run. 

This loop terminates if **any\_pos\_int** becomes equal to 1. In the loop, it checks whether **any\_pos\_int** divides evenly into 2 (i.e. is an even number). If it does, it divides **any\_pos\_int** by 2 and converts it to an integer using the **int** function. If it does not divide evenly into 2, then **any\_pos_int** is trebled and 1 is added to the result, which is then converted to an integer.

Before the loop terminates **any\_pos_int** is printed to the screen with a blank space afterwards.


5-weekday.py
-------

This script uses the **datetime** class in python to get the current day as a number between 0 and 6 and then tells the user whether that corresponds to a weekday or not.

Two lists are created which contain integers from 0-4 and 5-6. These correspond to weekdays (where 0 is Monday and 4 is Friday) and weekend days (5 is Saturday and 6 is Sunday).

The **today** and **weekday** functions in the **datetime** class are used to get the current date and then convert that date into a number betwen 0 and 6, which indicates what day it is in the week.

The programme then uses an **if** statement to check whether that is in the weekday list or the weekend day list. If it is the former, then it prints "Yes, unfortunately today is a weekday." Otherwise it prints "It is the weekend, yay!"


6-squareroot.py
-------
This script takes input from the user, converts it to a floating point number and gets the absolute value of it so that strings and non-positive numbers will be rejected. The result is set as the variable **pos**.

The **pos** variable is used as the first argument for the **newton\_root** function from the module **functions** (described in the **functions.py** section at the bottom of this file). 

The **newton\_root** function will find the approximate square root for **pos**. The second argument is the number of iterations for which the **newton\_root** function will run, in this case 5. 


The result is rounded to 1 decimal place using the **round** function and set as the variable **result**


This string is then printed to the screen: "The square root of **pos** is approx. ". **result** is printed to the screen directly after this string.



functions.py
--------

**newton_root**(input, iterations) 

This function gets the square root of the variable input and employs the Newton-Raphson method for finding approximate roots to the following equation:

 f(x) = x<sup>2</sup>-**input**. 

This is identical to approximating the square root of **input**. The formula employed for the Newton-Raphson method in its general form is:

x<sub>n+1</sub> = x<sub>n</sub> - f(x<sub>0</sub>)/f'(x<sub>n</sub>)

...where x<sub>n</sub> is the n<sup>th</sup> approximation, x<sub>0</sub> is the initial guess, f(x<sub>0</sub>) is the function f at the intial guess, f'(x<sub>n</sub>) is the derivative of the function at the n<sup>th</sup> approximation. In this case:

f'(x) = 2x

To get an initial guess for the Newton-Raphson method, **input** is divided by 4 and set as the variable **init**.

The Newton-Raphson method is employed for **iterations** number of iterations  using the following formula in a **while** loop: 

**init** = **init** -((**init**<sup>2</sup> - **input**)/(2 **init**))

 This loop terminates when the variable **i** reaches **iterations**. Just before the loop terminates, **i** is incremented so that **i** will evantually reach **iterations** and the function will not be stuck in an endless loop. 

The function then returns **init** which is the approximate square root of **input**



