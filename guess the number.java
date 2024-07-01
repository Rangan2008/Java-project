import java.util.Random;
import java.util.Scanner;

public class guess {
    public static void main(String[] args) {
        Random rand = new Random();
        Scanner scanner = new Scanner(System.in);

        int numberToGuess = rand.nextInt(100) + 1;
        int guess;
        int attempts = 0;

        System.out.println("Guess a number between 1 and 100:");

        do {
            guess = scanner.nextInt();
            attempts++;

            if (guess > numberToGuess) {
                System.out.println("Too high, try again.");
            } else if (guess < numberToGuess) {
                System.out.println("Too low, try again.");
            }

        } while (guess != numberToGuess);

        System.out.println("Yes, you guessed the number!");
        System.out.println("It took you " + attempts + " attempts to guess the number.");

        scanner.close();
    }
}