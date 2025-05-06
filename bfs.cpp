#include<iostream>
#include<vector>
#include<queue>
#include<stack>
using namespace std;

vector<bool> visit;

void edge(vector<int> adj[], int u, int v)
{
	adj[u].push_back(v);
}

void bfs(int s, vector<int> adj[])
{
	queue<int> q;
	q.push(s);
	visit[s]=true;
	while(!q.empty())
	{
		int u = q.front();
		cout<<u<<" ";
		q.pop();
		for(int i=0; i<adj[u].size(); i++) {
			if(!visit[adj[u][i]])
			{
				q.push(adj[u][i]);
				visit[adj[u][i]]=true;
			}
		}
	}
}

void dfs(int s, vector<int> adj[])
{
	stack<int> stk;
	stk.push(s);
	visit[s]=true;
	while(!stk.empty())
	{
		int u = stk.top();
		cout<<u<<" ";
		stk.pop();
		for(int i=0; i<adj[u].size(); i++) {
			if(!visit[adj[u][i]])
			{

				stk.push(adj[u][i]);
				visit[adj[u][i]]=true;
			}
		}
	}
}

int main()
{
	int n,e;

	cout<<"Enter no of vertices:";
	cin>>n;

	cout<<"Enter no of edges:";
	cin>>e;

	visit.assign(n,false);

	int i,u,v;
	vector<int> adj[n];
	cout<<"Enter Start vertex and end vertex of edge:";
	for(i=0; i<e; i++) {
		cin>>u>>v;

		edge(adj,u,v);
	}

	cout<<"BFS:"<<endl;
	bfs(0,adj);
	cout<<endl;
	visit.assign(n,false);
	cout<<"DFS: "<<endl;
	dfs(0,adj);
	cout<<endl;
	return 0;
}

/* I/P
Enter no of vertices:6
Enter no of edges:10
Enter Start vertex and end vertex of edge:0 1
0 3
1 2
1 3
2 3
2 4
2 5
3 4
3 5
4 5
*/