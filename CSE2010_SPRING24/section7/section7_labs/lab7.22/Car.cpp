#include <iostream>
#include <iomanip>
#include <cmath>
#include "Car.h"
using namespace std;

void Car::SetModelYear(int userYear){
   modelYear = userYear;
}

int Car::GetModelYear() const {
   return modelYear;
}

// TODO: Implement SetPurchasePrice() function
void Car::SetPurchasePrice(int userPrice) {
   purchasePrice = userPrice;
}

// TODO: Implement GetPurchasePrice() function
int Car::GetPurchasePrice() const {
   return purchasePrice;
}

void Car::CalcCurrentValue(int currentYear) {
   double depreciationRate = 0.15;
   int carAge = currentYear - modelYear;
      
   // Car depreciation formula
   currentValue = purchasePrice * pow((1 - depreciationRate), carAge);
}

// TODO: Implement PrintInfo() function to output modelYear, purchasePrice, and currentValue
void Car::PrintInfo() const {
   cout << "Car's information:" << endl;
   cout << "  Model year: " << modelYear << endl;
   cout << "  Purchase price: $" << GetPurchasePrice() << endl;
   cout << "  Current value: $" << fixed << setprecision(0) << currentValue << endl;
}
