#include<string>
#include<vector>
#include<iostream>
#include<algorithm>
#include<queue>

using namespace std;


typedef long long ll;
typedef vector< pair< int, ll > > edges;


class QuadraticLaw {
    public:


    pair< int, ll > bfs(int s, edges* e, int n, int ex) {
        queue<int> q;
        q.push(s);
        bool visited[n];
        while (!q.empty()) {
            int current = q.front();
            q.pop();
            for (int i = 0; i < e[current].size(); i++) {
                if visited[





            }





        }

    }
    

    ll diameter(int s, edges* e, int n, int ex) {
        int longest = bfs(s, e, n, ex).first;
        return bfs(longest, e, n, ex).second;
    }



    ll getLength(vector<int> A, vector<int> B, vector<int> L) {
        int n = A.size();
        int a[n], b[n], l[n];
        edges e[n + 1];

        for (int i=0;i<n-1;i++) {
            e[a[i]].push_back(make_pair(b[i], l[i]));
            e[b[i]].push_back(make_pair(a[i], l[i]));
            a[i] = A[i];
            b[i] = B[i];
            l[i] = L[i];
        }

        ll maxlen = 0;
        for (int i=0;i<n-1;i++) {
            maxlen = max(maxlen, diameter(a[i], e, n + 1, b[i]) + diameter(b[i], e, n + 1, a[i]) + l[i]);
            

            


        }










    }


};


int main() {
    QuadraticLaw ql;
    int aa[3] = {0, 0, 0};
    int bb[3] = {1, 2, 3};
    int cc[3] = {2, 4, 8};

    vector<int> a (aa, aa + sizeof(aa) / sizeof(int));
    vector<int> b (aa, aa + sizeof(bb) / sizeof(int));
    vector<int> c (aa, aa + sizeof(cc) / sizeof(int));

    cout << ql.getLength(a, b, c);


    return 0;
}
