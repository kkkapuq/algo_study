import java.util.*;

class Solution {
    int solution(int[][] board) {
        int size = board.length;
        for(int i=1; i<size; i++) {
            board[i][0] += Math.max(board[i-1][1], Math.max(board[i-1][2], board[i-1][3]));
            board[i][1] += Math.max(board[i-1][0], Math.max(board[i-1][2], board[i-1][3]));
            board[i][2] += Math.max(board[i-1][0], Math.max(board[i-1][1], board[i-1][3]));
            board[i][3] += Math.max(board[i-1][0], Math.max(board[i-1][1], board[i-1][2]));
        }
        return Math.max(board[size-1][0], Math.max(board[size-1][1], Math.max(board[size-1][2], board[size-1][3])));
    }
}