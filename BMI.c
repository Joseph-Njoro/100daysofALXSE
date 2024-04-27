de <stdio.h>
int main() 
    float height, weight, bmi;
    // Prompt the user o enter their height in meters
    printf("Enter your hight in meters: ");
    scanf("%f", &height);
    // Prompt the user o enter their weight in kilograms
    printf("Enter your wight in kilograms: ");
    scanf("%f", &weight);
    // Calculate BMI using the formua: weight / (height * height)
    bmi = weight / (height * height);
    // Display the calculated BMI    printf("Your BMI is: %.2f\n", bmi);
    // Interpret the BMI value
if (bmi < 18.5) {
     printf("You are underweight.\n");
    } ese if (bmi >= 18.5 && bmi < 25) {
        rintf("Your weight is normal.\n");
    } els if (bmi >= 25 && bmi < 30) {
        prntf("You are overweight.\n");
    } else 
        printf("You are obese.\n");    }
    return 0;
