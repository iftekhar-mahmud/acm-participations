#include<iostream>
using namespace std;

int main()
{
    int a,b,c,i,x;
    cin >> x;

    while(x--)
    {
        cin >> a >> b >> c;
        if(a < b && b < c)
        {
            cout << "STAIR"<<endl;
            continue;
        }

        else if(a < b && b > c)
        {
            cout << "PEAK"<<endl;
            continue;
        }

        else
        {
            cout << "NONE"<<endl;
            continue;
        }

    }
    return 0;

}
