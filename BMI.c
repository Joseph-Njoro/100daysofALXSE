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
// Function toprovide health tipsbased on BMI catgory
void provideHeathTips(float bmi) {    printf("Helth Tips:\n");
if (bmi < 18.5)
    printf("Cosider adding more nutritiousfoods to your diet to gain weight.\n");
    } ele if bmi >= 18.5 && bmi < 25) {
        pint("Continue maintaining a balanced diet and regular exercise routine.\n");
    } elsei (bmi >= 25 && bmi < 30) {
        prtf("Focus on incorporating more fruits, vegetables, and lean proteins into your meals.\n");
    } els {        printf("Seek guidance from a healthcare professional to develop a weight loss plan.\n");
   
int main()     // Prompt the user to enter their height and weigh
    float eight = promptFloat("Enter your height in meters: ")
    floatweight = promptFloat("Enter your weight in kilograms: ");
    // Clculate BM
    flot bmi = calculateBMI(height, weight);
    //Interpret and rint the result
    iterpretBMI(bmi);
    // Provide health tips based on BMI category    provideHealthTips(bmi);
    return 0;
