/*
import java.util.Scanner;
public class tst2 
{
  public static void main (String[]args)
  {
    String temp = null;
    Scanner scr = new Scanner(System.in);
    // Scanner_class object_Of_scanner_(u name it) = new creates_new Scanner_constructor(auto run function) (INputStream source
    // (we used sytem in but we can use file , string etc)) 
    System.out.print("enter a string:");
    temp = scr.nextLine();  // for int scr.nextInt(); wrong will give input exception mishandle 
    scanner.nextLine() // just to clear the input buffer of /n since nextINT DOES NOT READ /N hence it will leave /n in input buffer which will be entered in next scr call for string 
      System.out.println(temp);
    System.out.println("test for s.o.p");
  }
}
 */


/*
public class tst2 
{
 public static void main(String[] args) 
 {
    int n = 10;
    double y;
   y = (double)n/3 ;
   System.out.println(y);
 } 
}
 */

 /*
  import javax.swing.JOptionPane;
 public class tst2 
 {
  public static void main(String[] args) 
  {
    String name = JOptionPane.showInputDialog("Enter something \n (stored as string )");
    System.out.println(name);
    JOptionPane.showMessageDialog(null, "hello "+name);

    int age = Integer.parseInt(JOptionPane.showInputDialog("enter age"));
    JOptionPane.showMessageDialog(null, "ur "+age+" year's old ");

    double height = Double.parseDouble(JOptionPane.showInputDialog("enter Height \n (in cm) "));
    JOptionPane.showMessageDialog(null, "ur "+height+"cm tall ");
    // use specific data type with XXX.parse... since joptions input function accepts string
  }
 }
  */

/*
  import java.util.Scanner;
  public class tst2 
  {
    public static void main(String[] args) 
    {
      double x,y,hyp ;
      //Math.max(x, y) check for greater 
      // Math.abs () will give absolute value ie. remove neg sign 
      // Math.sqrt()
      //Math.round()
      //Math.ceil() will always round up 
      //Math.floor()will always round down 
      Scanner scr = new Scanner(System.in);
      System.out.println("Enter value of sides(use space to seprate two ints): ");
      x=scr.nextDouble();
      y=scr.nextDouble();
      hyp= x*x + y*y ;
      System.out.println("hypotenius : "+Math.sqrt(hyp));
      scr.close();
    }
  }
 */

 /*
  import java.util.Random;
 public class tst2 
 {
  public static void main(String[] args) 
  {
    Random rnd =new Random();  // creating an instance/object of random class 
    int x = rnd.nextInt(6)+1;// in rnd.nextInt(arg) u can set arg for range till arg , but since comp start with 0 it will include 0 but exclude 6 to counter that we can use ....+1
    System.out.println(x);
  }
 }
 */


/*  

Char c = '';
c = scr.next().charAt(0) // next will take input after its exceution 
unitl u run across space or enter // charAt() is string function which
u use to take a specific index elemnt of entered string ie if u  use 0
and enter "hello" only h of the string will be inputed . 
The method throws IndexOutOfBoundsException if the index argument is negative 
or not less than the length of the string

*/

/*
 for (;;) {} this will execute an infinite for loop without any para meters
 u can initialize multiple variable with for loop  
 */

 //1:28:15 - array
 

