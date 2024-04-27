tdio.h>int main() 
    flat height, weight, bmi;
    /pt the user o enter their height in meters
    rintf("Enter your hight in meters: ");nf("%f", &height);
    // Prompt the user o enter their weigt in kilograms
    printf("Enter your wight in kilogra);
    scanf("%f", &weight);
    // Calculate BMI using the formua:weight / (height * height)
    bmi = weight / (height * height  // Display the calculated BMI    printf("Your BMI is: %.2f\n", bmi);
    // Interpret the BMI valu
if (bmi < 18.5) {
     printf("You are undert.\n");
    } ese if (bmi >= 18.&& bmi < 25) {
        rintf("Your weiht is normal.\n");
    } els if (bmi >= & bmi < 30) {
        prntf("You e overweight.\n");
    } else
        printf("You are obese.\n");    }
    return 0;
