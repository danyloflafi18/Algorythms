import drawManager.DrawManager;





public class Main {

    public static void main(String[] args) {
        DrawManager drawManager = new DrawManager();
        System.out.println("Johnny should wait " + drawManager.measureExecutionTime(
                7,2,new Integer[]{1,1,1,1,5,5}) + " minutes");
    }
}
