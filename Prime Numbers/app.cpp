#include <iostream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;

int main(){
    vector<int> arr={};

    bool isPrime=true;
    int end;
    cout<<"Enter where to end: ";cin>>end;
    
    for (int i=2;i<end+1;i++){
        for (int j=2;j<i;j++){
            if(i%j==0){
                isPrime=false;
            }
        }
        if(isPrime==true){
            arr.push_back(i);
        }
        isPrime=true;
    }

    for (int i=0;i<arr.size();i++){
        cout<<arr[i]<<" ";
    }


    return 0;
}