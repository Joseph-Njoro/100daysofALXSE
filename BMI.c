#include <stdio.h>

int main() {
    float height, weight, bmi;

    // Prompt the user to enter their height in meters
    printf("Enter your height in meters: ");
    scanf("%f", &height);

    // Prompt the user to enter their weight in kilograms
    printf("Enter your weight in kilograms: ");
    scanf("%f", &weight);

    // Calculate BMI using the formula: weight / (height * height)
    bmi = weight / (height * height);

    // Display the calculated BMI
    printf("Your BMI is: %.2f\n", bmi);

    // Interpret the BMI value
    if (bmi < 18.5) {
        printf("You are underweight.\n");
    } else if (bmi >= 18.5 && bmi < 25) {
        printf("Your weight is normal.\n");
    } else if (bmi >= 25 && bmi < 30) {
        printf("You are overweight.\n");
    } else {
        printf("You are obese.\n");
    }

    return 0;
}