#include <iostream>
#include <iomanip>
#include <string>


using namespace std;

string convert24To12(int hours, int minutes)
{
    string ampm;
    if (hours >= 12)
    {
        if (hours > 12)
            hours -= 12;
        ampm = "PM";
    }
    else
    {
        if (hours == 0)
            hours = 12;
        ampm = "AM";
    }
    return to_string(hours) + ":" + to_string(minutes) + " " + ampm;
}

int main()
{
    int hours, minutes, T;
    cin >> T;
    while(T--)
    {
        cin >> hours;
        cout << ":";
        cin >> minutes;

        if (hours >= 0 && hours <= 23 && minutes >= 0 && minutes <= 59)
        {
            cout << convert24To12(hours, minutes) << endl;
        }
    }
    return 0;
}
