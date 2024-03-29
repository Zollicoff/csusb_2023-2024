#include <iostream>
using namespace std;

double CalcPyramidVolume(double baseLength, double baseWidth, double pyramidHeight) {
   double baseArea = baseLength * baseWidth;
   double pyramidVolume = baseArea * pyramidHeight * (1.0 / 3.0);
   return pyramidVolume;
}

int main() {
   double userLength;
   double userWidth;
   double userHeight;

   cin >> userLength;
   cin >> userWidth;
   cin >> userHeight;

   cout << "Volume: " << CalcPyramidVolume(userLength, userWidth, userHeight) << endl;

   return 0;
}
