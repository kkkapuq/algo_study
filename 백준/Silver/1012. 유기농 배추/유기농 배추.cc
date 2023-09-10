#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <cstring> // Include for memset
using namespace std;

int dx[] = {0, 1, 0, -1};
int dy[] = {-1, 0, 1, 0};
int n, m, ans;
int visited[52][52]; // Adjusted array size to handle up to 50x50 grid
int map[52][52];     // Adjusted array size to handle up to 50x50 grid
queue<pair<int, int>> q;
int x, y, t, k;

bool inRange(int y, int x)
{
    return y >= 0 && y < n && x >= 0 && x < m;
}

void dfs(int y, int x)
{
    visited[y][x] = 1;

    for (int i = 0; i < 4; ++i)
    {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (inRange(ny, nx) && !visited[ny][nx] && map[ny][nx] == 1)
        {
            dfs(ny, nx);
        }
    }
}

int main()
{
    cin >> t;
    while (t--)
    {
        memset(visited, 0, sizeof(visited)); // Use sizeof(visited) for correct array size
        memset(map, 0, sizeof(map));         // Use sizeof(map) for correct array size
        ans = 0;
        cin >> m >> n >> k;

        for (int i = 0; i < k; ++i)
        {
            int t1 = 0, t2 = 0;
            cin >> t1 >> t2;
            map[t2][t1] = 1;
        }

        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                if (visited[i][j] == 0 && map[i][j] == 1)
                {
                    dfs(i, j);
                    ans++;
                }
            }
        }
        cout << ans << endl;
    }
    return 0;
}