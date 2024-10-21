import java.util.Scanner;

public class problemno1 {
    public static void template(){
        System.out.println("================================================================================");
        System.out.println("Program mencetak pola bintang dan bilangan sesuai dengan input nilai n");
        System.out.println("================================================================================");
        System.out.println("Input nilai yang valid : 5 <= n <= 89 dan n bilangan ganjil");
        System.out.println("================================================================================");
    }

    public static int hasil(String Informasi, Scanner scan){
        System.out.print(Informasi);
        int inputNilai = 0;
        inputNilai = scan.nextInt();
        return inputNilai;
    }

    public static boolean validasi(int n){
        if(n >= 5 && n <= 89 && n % 2 == 1){
            return true;
        }else{
            System.out.println("Tidak Valid");
            return false;
        }
    }

    public static int fixGanjil(int bilGanjil){
        if(bilGanjil >= 9){
            return 1;
        }else{
            bilGanjil += 2;
            return bilGanjil;
        }
    }

    public static int fixGenap(int bilGenap){
        if(bilGenap >= 8){
            return 2;
        }else{
            bilGenap += 2;
            return bilGenap;
        }
    }

    public static void cetak(int n){
        int bilGanjil = 1;
        int bilGenap = 2;
        int half = (n - 1)/2;
        for(int y = 0; y <= half; y++){
            for(int x = 0; x < y; x++){
                System.out.print(" ");
            }
            if(y != half){
                System.out.print(bilGanjil);
                bilGanjil = fixGanjil(bilGanjil);
            }
            for(int wp = 0; wp < ((half - y) * 2) - 1; wp++){
                System.out.print(" ");
            }
            System.out.print("*");
            System.out.println();
        }
        for(int y = 0; y < half; y++){
            for(int x = 0; x < half - y - 1; x++){
                System.out.print(" ");
            }
            System.out.print(bilGenap);
            bilGenap = fixGenap(bilGenap);
            for(int wp = 0; wp < (y * 2) + 1; wp++){
                System.out.print(" ");
            }
            System.out.print("*");
            System.out.println();
        }
    }

    public static void badjinganLoEdwin() {
        Scanner scan = new Scanner(System.in);
        while(true){
            template();
            int n = hasil("Masukkan nilai n : ",scan);
            if(validasi(n)){
                cetak(n);
                break;
            }else{
                continue;
            }
        }
    }
}
