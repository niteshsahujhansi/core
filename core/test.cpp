#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int t = 0;
    cin >> t;
    while(t--)
    {
        int n = 0;
        cin >> n;
        vector<int> v(n);
        for (int i=0; i<n; ++i)
        {
            cin >> v[i];
        }
        vector<int> pgcd(n);
        pgcd[0] = v[0];
        for (int i=1; i<n; ++i)
        {
            pgcd[i] = __gcd(pgcd[i-1], v[i]);
        }
        vector<int> sgcd(n);
        sgcd[n-1] = v[n-1];
        for (int i = n-2; i>=0; --i)
        {
            sgcd[i] = __gcd(sgcd[i+1], v[i]);
        }
        int se = 0;
        for (int i=0; i<n; ++i)
        {
            if (i==0 && sgcd[1]> 1)
            {
                se++;
            }
            else if (i==n-1 && pgcd[n-2]>1)
            {
                se++;
            }
            else if (__gcd(pgcd[i-1], sgcd[i+1])>1)
            {
                se++;
            }
        }
        cout << se << '\n';
    }
}