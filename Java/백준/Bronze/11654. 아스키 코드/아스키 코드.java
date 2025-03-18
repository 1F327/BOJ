import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char ch;
        ch = sc.next().charAt(0);
        System.out.printf("%d", (int)ch);
        sc.close();
    }
}