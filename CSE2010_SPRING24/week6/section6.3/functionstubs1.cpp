#include <iostream>
using namespace std;

int GetUserNum() {
   cout << "FIXME: Finish GetUserNum()" << endl;
   return -1;
}

int ComputeAvg(int num1, int num2) {
   cout << "FIXME: Finish ComputeAvg()" << endl;
   return -1;
}

int main() {
   int userNum1;
   int userNum2;
   int avgResult;

   userNum1 = GetUserNum();
   userNum2 = GetUserNum();

   avgResult = ComputeAvg(userNum1, userNum2);

   cout << "Avg: " << avgResult << endl;

   return 0;
}
