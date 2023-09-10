#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <memory.h>
using namespace std;

int dx[] = { 0, 1, 0, -1 };
int dy[] = { -1, 0, 1, 0 };
int n, m, ans;
int visited[102][102];
int map[200][200];
queue<pair<int, int>> q;
int x, y, t, k, h;
vector<pair<int, int>> worm;
bool InRange(int y, int x)
{
	if (y >= n || y < 0 || x < 0 || x >= n)
		return false;
	return true;
}

void Dfs(int y, int x, int depth)
{
	for (int i = 0; i < 4; ++i)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (InRange(ny, nx) && !visited[ny][nx] && map[ny][nx] > depth)
		{
			visited[ny][nx] = 1;
			Dfs(ny, nx, depth);
		}
	}
}

int main()
{
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; j++)
		{
			cin >> map[i][j];
		}
	}

	ans = -1;

	// 장마 높이일때 마다 탐색을 진행한다 
	// 
	for (int i = 0; i < 101; ++i)
	{
		int cnt = 0;
		memset(visited, 0, sizeof(visited));

		for (int j = 0; j < n; ++j)
		{
			for (int k = 0; k < n; ++k)
			{
				if (!visited[j][k] && map[j][k] > i)
				{
					visited[j][k] = 1;
					Dfs(j, k, i);
					cnt++;
				}
			}
		}
		ans = max(ans, cnt);
	}

	cout << ans << endl;
	return 0;
}