#include <stdio.h>
#include <stdbool.h>

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

float calculateBMI(float height, float weight) {
    return weight / (height * height);
}

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

void provideHealthTips(float bmi) {
    printf("Health Tips:\n");
    if (bmi < 18.5) {
        printf("Consider adding more nutritious foods to your diet to gain weight.\n");
    } else if (bmi >= 18.5 && bmi < 25) {
        printf("Continue maintaining a balanced diet and regular exercise routine.\n");
    } else if (bmi >= 25 && bmi < 30) {
        printf("Focus on incorporating more fruits, vegetables, and lean proteins into your meals.\n");
    } else {
        printf("Seek guidance from a healthcare professional to develop a weight loss plan.\n");
    }
}

int main() {
    float height = promptFloat("Enter your height in meters: ");
    float weight = promptFloat("Enter your weight in kilograms: ");

    float bmi = calculateBMI(height, weight);

    interpretBMI(bmi);

    provideHealthTips(bmi);

    return 0;
}