package UTS_ALPRO.semester1;

import java.util.Scanner;

public class soalno1 {
    public static void main(String[] args){
        int n, x, y;
        System.out.println("==================================================");
        System.out.println("Input nilai n yang valid harus memenuhi ketentuan");
        System.out.println("5 <= n <= 89 dan n merupakan bilangan ganjil");
        System.out.println("==================================================");
        Scanner scan = new Scanner(System.in);
        System.out.print("Masukkan nilai n : ");
        n = scan.nextInt();
        
        while (!((n >= 5 && n <= 89) && (n % 2 == 1))) {
        System.out.println("==================================================");
        System.out.println("Input nilai n yang valid harus memenuhi ketentuan");
        System.out.println("5 <= n <= 89 dan n merupakan bilangan ganjil");
        System.out.println("==================================================");
        System.out.print("Masukkan nilai n : ");
        n = scan.nextInt();
        }
        scan.close();
        for(y = n; y > 0; y--){
            for(x = y; x > 0; x--){
                System.out.print(" ");
            }
            if(y % 2 == 1){
                for(x = 1; x <= n * 2; x+=2){
                    System.out.print(x);
                }
            } else {
                for(x = 2; x <= n * 2; x+=2){
                    System.out.print(x);
                }
            }
            System.out.println();
        }
    }
}