#include <bits/stdc++.h>

using namespace std;

class IdentifyingWood {
    public:
        string check(string s, string t) {
            int m = -1;
            for (int i = 0; i < t.size(); i++) {
                bool found = 0;
                for (int j = m + 1; j < s.size(); j++) {
                    if (t[i] == s[j]) {
                        m = j;
                        found = 1;
                        break;
                    };
                };
                if (!found) return "Nope.";
            };
            
            return "Yep, it's wood.";
        }
};

int main() {
    IdentifyingWood x;
    cout<<x.check("abcd", "a");

    return 1;
};
