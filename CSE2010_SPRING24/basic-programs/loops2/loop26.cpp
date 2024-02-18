#include <iostream>
#include <string>
using namespace std;

int main() {
   string simonPattern;
   string userPattern;
   int userScore = 0; // Initialize userScore to 0

   cin >> simonPattern;
   cin >> userPattern;

   for (i = 0; i < simonPattern.length(); ++i) { // Iterate over the length of simonPattern
      if (simonPattern[i] == userPattern[i]) { // If characters match at the same index
         userScore++; // Increment userScore
      } else { // If there's a mismatch
         break; // Exit the loop
      }
   }

   cout << "userScore: " << userScore << endl; // Output the userScore

   return 0;
}
