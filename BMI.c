#include <stdio.h#include <stdbool.h>
// Function  propt the user to enter a positive float value
float promptFatconst char *message) {
    float val
    printf("s", mesge);
    scanf("f", &valu;
    while value <= 0)
        pintf("Please ente a poitive value: ");
        canf("%f", &value);    }   return value;
// Function to calculate BMIfloat calculateBMI(loat height, float weight) {   return weight / (height * height);
// Function tointerpret BMI nd print the resul
void interpretBI(float bmi) {    printf("YourBMI is: %.2f\n", bmi);
if (bmi < 18.5)
    printf("Yo are underweight.\n);
    } ele if bmi >= 18.5 && bmi < 5) {
        pint("Your weight is normal\n");
    } elsei (bmi >= 25 && bmi < 30) 
        prtf("You are overweight.\n")
    } els {        printf("You are obese.\n");   }
// Function toprovide health tipsbased on BMI category
void provideHeathTips(float bmi) {    printf("Health Tips:\n");
if (bmi < 18.5) 
    printf("Consider adding more nutritiousfoods to your diet to gain weight.\n");
    } ele if (bmi >= 18.5 && bmi < 25) {
        pintf("Continue maintaining a balanced diet and regular exercise routine.\n");
    } elseif (bmi >= 25 && bmi < 30) {
        pritf("Focus on incorporating more fruits, vegetables, and lean proteins into your meals.\n");
    } else {        printf("Seek guidance from a healthcare professional to develop a weight loss plan.\n");
   }
}
int main() 
    // Prompt the user to enter their height and weigh
    float height = promptFloat("Enter your height in meters: ")
    float weight = promptFloat("Enter your weight in kilograms: ");
    // Calculate BM
    float bmi = calculateBMI(height, weight);
    // Interpret and rint the result
    interpretBMI(bmi);
    // Provide health tips based on BMI category    provideHealthTips(bmi);
    return 0;
