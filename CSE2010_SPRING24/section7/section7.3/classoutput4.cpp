#include <iostream>
using namespace std;

class Person {
   public:
      void SetFirstName(string firstNameToSet);
      void SetLastName(string lastNameToSet);
      string GetFullName();
   private:
      string first;
      string last;
};

void Person::SetFirstName(string firstNameToSet) {
   first = firstNameToSet;
}

void Person::SetLastName(string lastNameToSet) {
   last = lastNameToSet;
}

string Person::GetFullName() {
   return first + "_" + last;
}

int main() {
   string firstName;
   string lastName;

   firstName = "May";
   lastName = "Kent";

   Person person1;

   person1.SetFirstName(firstName);
   person1.SetLastName(lastName);

   cout << person1.GetFullName();

   return 0;
}