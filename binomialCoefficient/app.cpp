#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int factorial(int num1);
int binCoef(int num1, int num2);

int main(void)
{
    int number1;
    int number2;

    cout << "Enter 1st number: ";
    cin >> number1;
    cout << "Enter 2nd number: ";
    cin >> number2;

    cout << "The binary Coefficient is: " << binCoef(number1, number2);
    cin >> number2;

    cin.get();
    return 0;
}

int factorial(int num1)
{
    int res = 1;
    for (int i = 1; i < num1 + 1; i++)
    {
        res *= i;
    }
    return res;
}
int binCoef(int num1, int num2)
{
    int diff = num1 - num2;
    int res = (factorial(num1)) / (factorial(num2) * factorial(diff));
    return res;
}