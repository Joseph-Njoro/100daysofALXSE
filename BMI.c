#include <stdio.h>
#include <stdbool.h>

// Function to prompt the user to enter a positive float value
float promptFloat(const char *message) {
    float value;
    printf("%s", message);
    scanf("%f", &value);
    while (value <= 0) {
        printf("Please enter a positive value: ");
        scanf("%f", &value);
    }
    return value;
}

// Function to calculate BMI
float calculateBMI(float height, float weight) {
    return weight / (height * height);
}

// Function to interpret BMI and print the result
void interpretBMI(float bmi) {
    printf("Your BMI is: %.2f\n", bmi);
    if (bmi < 18.5) {
        printf("You are underweight.\n");
    } else if (bmi >= 18.5 && bmi < 25) {
        printf("Your weight is normal.\n");
    } else if (bmi >= 25 && bmi < 30) {
        printf("You are overweight.\n");
    } else {
        printf("You are obese.\n");
    }
}

int main() {
    // Prompt the user to enter their height and weight
    float height = promptFloat("Enter your height in meters: ");
    float weight = promptFloat("Enter your weight in kilograms: ");

    // Calculate BMI
    float bmi = calculateBMI(height, weight);

    // Interpret and print the result
    interpretBMI(bmi);

    return 0;
}