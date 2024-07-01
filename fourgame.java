import java.util.Scanner;

public class fourgame {
    public static final int ROWS = 6;
    public static final int COLS = 7;
    public static final char EMPTY_SLOT = '.';
    public static final char PLAYER_ONE = 'X';
    public static final char PLAYER_TWO = 'O';

    public static void main(String[] args) {
        char[][] board = new char[ROWS][COLS];
        initializeBoard(board);
        printBoard(board);
        boolean gameWon = false;
        char currentPlayer = PLAYER_ONE;

        while (!gameWon && !isBoardFull(board)) {
            int col = getPlayerMove(currentPlayer);
            if (makeMove(board, col, currentPlayer)) {
                printBoard(board);
                if (checkWin(board, currentPlayer)) {
                    gameWon = true;
                    System.out.println("Player " + currentPlayer + " wins!");
                } else {
                    currentPlayer = (currentPlayer == PLAYER_ONE) ? PLAYER_TWO : PLAYER_ONE;
                }
            } else {
                System.out.println("Column " + col + " is full. Try another column.");
            }
        }

        if (!gameWon) {
            System.out.println("The game is a draw.");
        }
    }

    public static void initializeBoard(char[][] board) {
        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                board[row][col] = EMPTY_SLOT;
            }
        }
    }

    public static void printBoard(char[][] board) {
        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                System.out.print(board[row][col] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static int getPlayerMove(char player) {
        Scanner scanner = new Scanner(System.in);
        int col;
        do {
            System.out.print("Player " + player + ", enter column (0-6): ");
            col = scanner.nextInt();
        } while (col < 0 || col >= COLS);
        return col;
    }

    public static boolean makeMove(char[][] board, int col, char player) {
        for (int row = ROWS - 1; row >= 0; row--) {
            if (board[row][col] == EMPTY_SLOT) {
                board[row][col] = player;
                return true;
            }
        }
        return false;
    }

    public static boolean checkWin(char[][] board, char player) {
        // Check horizontal
        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS - 3; col++) {
                if (board[row][col] == player && board[row][col + 1] == player && board[row][col + 2] == player && board[row][col + 3] == player) {
                    return true;
                }
            }
        }
        // Check vertical
        for (int row = 0; row < ROWS - 3; row++) {
            for (int col = 0; col < COLS; col++) {
                if (board[row][col] == player && board[row + 1][col] == player && board[row + 2][col] == player && board[row + 3][col] == player) {
                    return true;
                }
            }
        }
        // Check diagonal (bottom left to top right)
        for (int row = 3; row < ROWS; row++) {
            for (int col = 0; col < COLS - 3; col++) {
                if (board[row][col] == player && board[row - 1][col + 1] == player && board[row - 2][col + 2] == player && board[row - 3][col + 3] == player) {
                    return true;
                }
            }
        }
        // Check diagonal (top left to bottom right)
        for (int row = 0; row < ROWS - 3; row++) {
            for (int col = 0; col < COLS - 3; col++) {
                if (board[row][col] == player && board[row + 1][col + 1] == player && board[row + 2][col + 2] == player && board[row + 3][col + 3] == player) {
                    return true;
                }
            }
        }
        return false;
    }

    public static boolean isBoardFull(char[][] board) {
        for (int col = 0; col < COLS; col++) {
            if (board[0][col] == EMPTY_SLOT) {
                return false;
            }
        }
        return true;
    }
}
