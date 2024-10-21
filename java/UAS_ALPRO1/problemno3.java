import java.util.Scanner;

public class problemno3 {
    public static void template(){
        System.out.println("================================================================================");
        System.out.println("Program mencetak pola bintang dan bilangan sesuai dengan input nilai n");
        System.out.println("================================================================================");
        System.out.println("Input nilai yang valid : 5 <= n <= 89 dan n bilangan ganjil");
        System.out.println("================================================================================");
    } 
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        while(true){
            template();
            System.out.print("Edwin anak gila : ");
            int n = scan.nextInt();
            switch (n) {
                case 1:
                    problemno1.badjinganLoEdwin();
                    break;
                case 2:
                    problemno2.badjinganLoYulia();
                    break;
                default:
                    System.out.println("Tidak Valid");
                    continue;
            }
            while(true){
                System.out.print("Apakah ingin keluar dari UKDC ? : ");
                int n2 = scan.nextInt();
                switch (n2) {
                    case 1:
                        System.out.println("Program Mengulang : "); 
                        break;
                    case 0:
                        System.out.println("Program Berhenti");
                        scan.close();
                        return;
                    default:
                        System.out.print("Salahnya sendiri masuk UKDC");
                        continue;
                }
                break;
            }
        }
    }
}
