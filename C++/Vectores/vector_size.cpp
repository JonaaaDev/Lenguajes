#include <iostream>
#include <vector>

using namespace std;

int main()
{
	vector<int> puntaje (5,3);
	
	int contador = 0;
	
	while (contador < puntaje.size()){
                    
        cout << puntaje[contador] << endl;
        contador++;
    }
	
}
