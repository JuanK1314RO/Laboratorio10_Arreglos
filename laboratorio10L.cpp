#include <iostream>

using namespace std;

int main() {
  int n,i,x=0;
  cout << "Ingrese un numero: ";
  cin >> n;

  for (i=1; i<n-1; i++) {
    if (n % i == 0)
      x += i;
  } 
  if (n == x)
    cout << "Es un numero perfecto" <<endl;
  else 
    cout << "No es un numero perfecto" <<endl;
    
  printf("\n\n\n");system("PAUSE");
  return 0;
}
