import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    private static Stack<Integer> stack1 = new Stack<Integer>(); 
    private static Stack<Integer> stack2 = new Stack<Integer>();

    private static void flush() {
        if (stack2.isEmpty()) {
            if (stack1.isEmpty()) {
                return;
            } else {
                while (!stack1.isEmpty()) {
                    Integer popValue = (Integer) stack1.pop();
                    stack2.push(popValue);
                }
            }
        }
    }

    private static void solve(String[] lineInputs) {
        if (lineInputs.length > 1) {
            int input1 = Integer.parseInt(lineInputs[0]);
            int input2 = Integer.parseInt(lineInputs[1]);
            if (input1 == 1) {
                stack1.push(input2);
            }
        } else {
            int input = Integer.parseInt(lineInputs[0]);
            if (input == 2) {
                flush();
                stack2.pop();
            } else if (input == 3) {
                flush();
                Integer peekValue = (Integer) stack2.peek();
                System.out.println(peekValue);
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            String[] lineInputs = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            solve(lineInputs);
        }

        scanner.close();
    }
}