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
 
public class tst2 
{
  public static void main(String[] args)
  {  
  String day = "Friay";
  switch(day)
  {
    case "Sunday": 
    System.out.println("sunday");
    break; // if break is not present we will execute all subset of codes after the first subset of code is executed so all sysout willl be executed
    case "Friday" : 
    System.out.println("Friday");
    break;
    default: System.out.println("error"); // break not needed since last code in switch 
  }
  }
}
*/
/*
 
public class tst2 
{
  public static void main(String[] args) 
  {
  String str = "q";
  int x=1,z=1,y=1;
    if (x==y && y==z)  // && = both condition must be true : || = either one of the condition must be true  :  ! =  not true ie reverse boolen value
    {
      System.out.println("x,y,z are all equal ");  
    } 
    if (str.equals("q") || str.equals("Q") ) // to compare string we need specific function  [ string_variable.equal() ]  
    {
      System.out.println("string is equal to q to Q ");
    }
  }
}
*/


/* 
public class tst2 
{
  public static void main(String[] args) 
  {

    String name ="";
    name.isBlank(); // check if a string is black 
    // do {} while();  // if just while u don't need ; // do while execute atleast once 
    // for (;;) {} this will execute an infinite for loop without any para meters
    // u can initialize multiple variable with for loop  

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

public class tst2 
{
  public static void main(String[] args) 
  {
String cars []= {" \" ","\'"}; // if u accest -ve or after size u get arr out of bound error
String car [][]= new String[30][25];
 car [0][0]="\\";// u can assig with arr[][]={},{}; where arr[] is empty or pointing to particular row 

 // cars_length = cars.length(); // a function to get length of array
 // for 2d array arr.length() will give clumn length // arr[0].length will give column length of that particular column 0 can be replaced with i 
 // so that we get length of that particular row 
int arr_int [];//array declaration
arr_int = new int[20]; // allocating meemor to an array 
// or  int [] arr_int = new int [20]; 
System.out.println(cars[0]);
System.out.println(car[0][0]); // for a loop runing only pring u can use (arr[]+" ") for space between each elemnt on print 
  }
}  

*/
 

/* 

public class tst2 
{
  public static void main(String[] args) 
  {
    String Pri = "Pri";
    boolean equal = true ;
    equal = Pri.equals("Priyanshu"); // string.equal() will compare and give boolean value can use another string or "" 
    // equals () is case sensitive to combat that we can use string.equalsIgnoreCase() function 
    int length = Pri.length();
    char index = Pri.charAt(2);// acces a particual index of string with .charAt
    int indexs = Pri.indexOf("r"); // this will find the index of "r" in the string Pri
    boolean empty = Pri.isEmpty()//will check if no charcter and only whitespace
    Pri.isBlank();// will check if no char , only whitespace, and is null
    Pri.toLowerCase()// for lower all element 
    Pri.toUpperCase()// for ucase all elelemnt
    Pri.trim() // remove all space infront and back of string 
    Pri.replace(index, index) // (old,new)  can use ('r','u')
    System.out.println(index);
  }
}  

*/


 /* 
public class tst2 {

 public static void main(String[] args) {
  
  // wrapper class =  provides a way to use primitive data types as reference data types
  //     reference data types contain useful methods
  // wrapper class increases step need to acces data so for big data wrapper class will increase resouce load 
  //     can be used with collections (ex.ArrayList)
  
  //primitive  //wrapper  //String is already ref
  //---------  //-------  
  // boolean  Boolean
  // char   Character
  // int   Integer
  // double  Double
  
  // autoboxing = the automatic conversion that the Java compiler makes between the primitive types and their corresponding object wrapper classes
  // unboxing = the reverse of autoboxing. Automatic conversion of wrapper class to primitive
  
  Boolean a = true;  // all autobox here since wrapper object was assigned primitive value // u can still treat them as prmitive since unboxing is auto 
  Character b = '@';
  Integer c = 123;
  Double d = 3.14;
  String e = "Pri";

  a.parseBoolean(e) // wrapper class variable have acces to even larger set of functions 
  
 }
 
}

*/



/* 

import java.util.ArrayList;

public class tst2 {

	public static void main(String[] args) 
  {
			
		// ArrayList = 	a resizable array. 
		//				Elements can be added and removed after compilation phase
		//				store reference data types // if want to use prim such as int then use wrapper Integer
		
		ArrayList<String> food = new ArrayList<String>(); 
    
    
    int arr [] = new int[] {2,3,4,5}; // here new int will create an instance of that array and u can mention size in new Int[size] 
    // u don't need to give array size if u are directly giving value during initializer with {}
    // if u don't give value during initializing then u have give value to each elemnt by loop 
    // array intializing of object can only be done with {} during declaration , u can't declare then give value with {} since array won't be intialized then 
    
    
    // therfore only  leagal way to create array are 
    
    
    // int arr [] = new int[] {} when u want to create blank of specif size remove {} if no value given during declaration
    
    
    // int[] arr2 = {,,} here declaraion and assigning value is one step 
    
    
    // last method will require multiple line of codes 
    // int arr[]; // declaration 
    // arr[0]=1; // assignment with intializing 

    // also use  datatype[] VarName as good practive 
    // ArrayList<datatype> VarName = new ArrayList<datatype>()
    // ArrayList<datatype> acts as one dataype same with structure in C

    int[] arr2 = {3,3,4,5};
    System.out.println(arr2[0]);
		
		
    
    food.add("pizza");
		food.add("hamburger");
		food.add("hotdog");
		
		food.set(0, "sushi");  // set a value at certain index arrlist.set(index,elemnt)
		food.remove(2);
		food.clear();
		
		for(int i=0; i<food.size(); i++) // use arraylist.size() instead of arr.length() since diff data type 
    {
			System.out.println(food.get(i));
		}
	}
}

*/


/* 

import java.util.*;

public class tst2 {

	public static void main(String[] args) 
  {
		
		ArrayList<ArrayList<String>> groceryList = new ArrayList(); // u can change size of list during runtime // we create and array list that can stor araylist of string as data type 
		
		ArrayList<String> bakeryList = new ArrayList();
		bakeryList.add("pasta");
		bakeryList.add("garlic bread");
		bakeryList.add("donuts");
		
		ArrayList<String> produceList = new ArrayList();
		produceList.add("tomatoes");
		produceList.add("zucchini");
		produceList.add("peppers");
		
		ArrayList<String> drinksList = new ArrayList();
		drinksList.add("soda");
		drinksList.add("coffee");
		
		groceryList.add(bakeryList);
		groceryList.add(produceList);
		groceryList.add(drinksList);
		
		System.out.println(groceryList.get(0).get(2)); // this will display enture list but use ArrayList.get(index) for a specific element can be stacked through for index of index
		
	}
}


*/

/* 

import java.util.ArrayList;

public class tst2 
{

	public static void main(String[] args) 
  {
			
		// for-each = 	traversing technique to iterate through the elements in an array/collection
		//				less steps, more readable
		//				less flexible
		
		//String[] animals = {"cat","dog","rat","bird"};
		ArrayList<String> animals = new ArrayList<String>();
		
		animals.add("cat");
		animals.add("dog");
		animals.add("rat");
		animals.add("bird");
		
		for(String i : animals) // for ( every_string index :_(represents in) string_var) 
    // this will iterate once for each element in collections
    {
			System.out.println(i);
		}
  }  
}  

*/

/* 
public class tst2 {

	public static void main(String[] args) 
  {		
		// method = a block of code that is executed whenever it is called upon
		
		int x = 3;
		int y = 4;
		
		int z = add(x,y);

		System.out.println(z);
	}
	
	static int add(int x, int y) // we use static here since calling from a static main u can't call unstatic method
  {		
		int z = x + y;
		return z;
	}
	
}

*/

/* 
public class tst2 {

	public static void main(String[] args) {
		
		// overloaded methods = methods that share the same name but have different parameters
		//						method name + parameters = method signature
		
		double x = add(1.0,2.0,3.0,4.0);
		
		System.out.println(x);
		
	}
	
	static int add(int a, int b) {
		System.out.println("This is overloaded method #1");
		return a + b;
	}
	static int add(int a, int b, int c) {
		System.out.println("This is overloaded method #2");
		return a + b + c;
	}
	static int add(int a, int b, int c, int d) {
		System.out.println("This is overloaded method #3");
		return a + b + c + d;
	}
	static double add(double a, double b) {
		System.out.println("This is overloaded method #4");
		return a + b;
	}
	static double add(double a, double b, double c) {
		System.out.println("This is overloaded method #5");
		return a + b + c;
	}
	static double add(double a, double b, double c, double d) {
		System.out.println("This is overloaded method #6");
		return a + b + c + d;
	}	
}

*/


/* 

public class tst2 {

	public static void main(String[] args) {

		// printf() = 	an optional method to control, format, and display text to the console window
		//				two arguments = format string + (object/variable/value)
		//				% [flags] [precision] [width] [conversion-character]

    // when declaring variable use final to make in immutable -- final int x - 25;

				
		boolean myBoolean = true;
		char myChar = '@';
		String myString = "Bro";
		int myInt = 50;
		double myDouble = 1000;
			
		// [conversion-character]
		//System.out.printf("%b",myBoolean);
		//System.out.printf("%c",myChar);
		//System.out.printf("%s",myString);
		//System.out.printf("%d",myInt);
		//System.out.printf("%f",myDouble);
		
		//[width]
		// minimum number of characters to be written as output
		//System.out.printf("Hello %10s",myString);
		
		//[precision]
		// sets number of digits of precision when outputting floating-point values
		//System.out.printf("You have this much money %.1f",myDouble);
		
		// [flags]
		// adds an effect to output based on the flag added to format specifier
		// - : left-justify
		// + : output a plus ( + ) or minus ( - ) sign for a numeric value
		// 0 : numeric values are zero-padded
		// , : comma grouping separator if numbers > 1000
		
		//System.out.printf("You have this much money %,f",myDouble);
	}
}

*/


//*******************************************
public class Main {

	public static void main(String[] args) {
		
		Car myCar1 = new Car();
		Car myCar2 = new Car();

		System.out.println(myCar1.make);
		System.out.println(myCar1.model);

		myCar1.drive();
		myCar1.brake();
	}
}
//*******************************************
public class Car {

	String make = "Chevrolet";
	String model = "Corvette";
	int year = 2020;
	String color = "blue";
	double price = 50000.00;
	
	void drive() {
		System.out.println("You drive the car");
	}
	void brake() {
		System.out.println("You step on the brakes");
	}	
}
//*******************************************


//  oop- 3:00:00

