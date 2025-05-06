#include <iostream>
#include <vector>
#include <string>

using namespace std;

void printBoard(vector<vector<char>> board) {
    int n = board.size();
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }

    cout << "---------------\n";
}

bool isSafe(vector<vector<char>> board, int row, int col) {
    int n = board.size();
    //vertical
    for(int j=0; j<col; j++) {
        if(board[row][j] == 'Q') {
            return false;
        }
    }

    //horizontal
    for(int i=0; i<row; i++) {
        if(board[i][col] == 'Q') {
            return false;
        }
    }

    //diagonal left
    for(int i=row-1, j=col-1; i>=0 && j>=0; i--, j--) {
        if(board[i][j] == 'Q') {
            return false;
        }
    }

    //diagonal right
    for(int i=row-1, j=col+1; i>=0 && j<n; i--, j++) {
        if(board[i][j] == 'Q') {
            return false;
        }
    }
    return true;
}


int nQueens(vector<vector<char>> board, int row) {
    int n = board.size();
    if(row == n) {
        printBoard(board);
        return 1;
    }

    // int count = 0;
    for(int j=0; j<n; j++) {
        if(isSafe(board, row, j)) {
            board[row][j] = 'Q';
            // count += 
            nQueens(board, row+1);
            board[row][j] = '.';
        }
    }

    // return count;
}

int main(){
    vector<vector<char>> board;
    int n;
    cout<<"Enter the size of the board: ";
    cin>>n;
    cout<<"The possible solutions are:\n";
    cout<<"---------------\n";
    for(int i=0;i<n;i++){
        vector<char>temp;
        for(int j=0;j<n;j++){
            temp.push_back('.');
        }
        board.push_back(temp);
    }

    // printBoard(board);
    nQueens(board,0);

}


//USING ARRAYS

// #include <iostream>
// using namespace std;

// #define MAX 15 // You can increase this if needed

// void printBoard(char board[MAX][MAX], int n) {
//     for(int i = 0; i < n; i++) {
//         for(int j = 0; j < n; j++) {
//             cout << board[i][j] << " ";
//         }
//         cout << endl;
//     }
//     cout << "---------------\n";
// }

// bool isSafe(char board[MAX][MAX], int row, int col, int n) {
//     // check column (vertical)
//     for(int i = 0; i < row; i++) {
//         if(board[i][col] == 'Q') return false;
//     }

//     // check diagonal left
//     for(int i = row-1, j = col-1; i >= 0 && j >= 0; i--, j--) {
//         if(board[i][j] == 'Q') return false;
//     }

//     // check diagonal right
//     for(int i = row-1, j = col+1; i >= 0 && j < n; i--, j++) {
//         if(board[i][j] == 'Q') return false;
//     }

//     return true;
// }

// int nQueens(char board[MAX][MAX], int row, int n) {
//     if(row == n) {
//         printBoard(board, n);
//         return 1;
//     }

//     int count = 0;
//     for(int col = 0; col < n; col++) {
//         if(isSafe(board, row, col, n)) {
//             board[row][col] = 'Q';
//             count += nQueens(board, row + 1, n);
//             board[row][col] = '.';
//         }
//     }
//     return count;
// }

// int main() {
//     char board[MAX][MAX];
//     int n;

//     cout << "Enter the size of the board: ";
//     cin >> n;

//     // initialize board with '.'
//     for(int i = 0; i < n; i++)
//         for(int j = 0; j < n; j++)
//             board[i][j] = '.';

//     cout << "The possible solutions are:\n";
//     cout << "---------------\n";
//     nQueens(board, 0, n);
// }
