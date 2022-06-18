#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int main(){
    int myNum=23;
    string mystr;
    vector <int> arr={};

    cout<<"Enter: ";getline(cin,mystr);
    stringstream(mystr)>>myNum;
    cout<<myNum;

    cin.get();
    return 0;
}