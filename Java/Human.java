public class Human {

	String name;
	int age;
	double weight;
	
	Human(String name,int age,double weight) // constructor , same name as class , runs once when class is instancized with new.class_name
    {		
		this.name = name;
		this.age = age;
		this.weight = weight;
	}
	
	void eat() // method 
    {
		System.out.println(this.name+" is eating");
	}
	void drink() {
		System.out.println(this.name+" is drinking *burp*");
	}
		
}