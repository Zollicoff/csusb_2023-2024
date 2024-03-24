#include "LinkedListLibrary.h"
#include "VectorLibrary.h"
#include "BookNode.h"
#include "Book.h"
#include <fstream>
#include <iostream>
using namespace std;

void FillLibraries(LinkedListLibrary &linkedListLibrary, VectorLibrary &vectorLibrary) {
   ifstream inputFS; // File input stream

   BookNode* currNode;
   Book tempBook;

   string bookTitle;
   string bookAuthor;
   long long bookISBN;

   // Try to open file
   inputFS.open("books.txt");

   while(getline(inputFS, bookTitle)) {
      inputFS >> bookISBN;
      inputFS.ignore(1, '\n');
      getline(inputFS, bookAuthor);

      // Insert into linked list
      currNode = new BookNode(bookTitle, bookAuthor, bookISBN);
      linkedListLibrary.InsertSorted(currNode);

      // Insert into vector
      tempBook = Book(bookTitle, bookAuthor, bookISBN);
      vectorLibrary.InsertSorted(tempBook);
   }

   inputFS.close(); // close() may throw ios_base::failure if fails
}

int main () {
   // Create libraries
   LinkedListLibrary linkedListLibrary = LinkedListLibrary();
   VectorLibrary vectorLibrary;

   // Fill libraries with 100 books
   FillLibraries(linkedListLibrary, vectorLibrary);

   // Create new book to insert into libraries
   BookNode* currNode;
   Book tempBook;

   string bookTitle;
   string bookAuthor;
   long long bookISBN;

   getline(cin, bookTitle);
   cin >> bookISBN;
   cin.ignore();
   getline(cin, bookAuthor);

   // Insert into linked list
   // No need to delete currNode, deleted by LinkedListLibrary destructor
   currNode = new BookNode(bookTitle, bookAuthor, bookISBN);
   int linkedListOperations = linkedListLibrary.InsertSorted(currNode);
   cout << "Number of linked list book copy operations: " << linkedListOperations << endl;

   // Insert into VectorList
   tempBook  = Book(bookTitle, bookAuthor, bookISBN);
   int vectorOperations = vectorLibrary.InsertSorted(tempBook);
   cout << "Number of vector book copy operations: " << vectorOperations << endl;

   return 0;
}