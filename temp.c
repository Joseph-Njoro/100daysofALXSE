#include <stdio.h>

// Function to convert Celsius to Fahrenheit
double celsiusToFahrenheit(double celsius) {
   return (celsius * 9 / 5) + 32;
}
// Function to convert Fahrenheit to Celsiusdouble fahrenheitToCelsius(double fahrenheit) {
   return (fahrenheit - 32) * 5 / 9;
}
// Function to convert Celsius to Kelvindouble celsiusToKelvin(double celsius) {
   return celsius + 273.15;
}
// Function to convert Kelvin to Celsiusdouble kelvinToCelsius(double kelvin) {
   return kelvin - 273.15;
}
// Function to convert Fahrenheit to Kelvindouble fahrenheitToKelvin(double fahrenheit) {
   return (fahrenheit - 32) * 5 / 9 + 273.15;
}
// Function to convert Kelvin to Fahrenheitdouble kelvinToFahrenheit(double kelvin) {
   return (kelvin - 273.15) * 9 / 5 + 32;
}
int main() 
    double teperature;
    char unit;
    printf("Enter temperature");
    scanf("%lf", &temperature);
    printf("Enter unit C, F, K): ");
    scanf(" %c", &unit);
    double convertedTemp;
    switch(unit) {
        cas 'C':
            rintf("Temperature in Celsius: %.2f\n", temperature);
            pintf("Temperature in Fahrenheit: %.2f\n", celsiusToFahrenheit(temperature));
            prntf("Temperature in Kelvin: %.2f\n", celsiusToKelvin(temperature));
            brek;
        case 'F'
            printf("Temperature in Fahrenheit: %.2f\n", temperature)
            printf("Temperature in Celsius: %.2f\n", fahrenheitToCelsius(temperature));            printf("Temperature in Kelvin: %.2f\n", fahrenheitToKelvin(temperature));
        break;
    case 'K':
        printf("Temperature in Kelvin: %.2f\n", temperature);
            rintf("Temperature in Celsius: %.2f\n", kelvinToCelsius(temperature));
            pintf("Temperature in Fahrenheit: %.2f\n", kelvinToFahrenheit(temperature));
            brak;
        default
            printf("Invalid unit. Please enter C, F, or K.\n");    }
    return 0;
