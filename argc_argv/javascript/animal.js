class Animal {
    constructor(name, species) {
      this.name = name;
      this.species = species;
    }
  
    introduce() {
      console.log(`Hi, I'm ${this.name}, a ${this.species}.`);
    }
  }
  
  class Dog extends Animal {
    constructor(name, breed, age) {
      super(name, "dog");
      this.breed = breed;
      this.age = age;
    }
  
    bark() {
      console.log("Woof woof!");
    }
  
    introduce() {
      super.introduce();
      console.log(`I'm a ${this.age}-year-old ${this.breed}.`);
    }
  }
  
  class Cat extends Animal {
    constructor(name, color) {
      super(name, "cat");
      this.color = color;
    }
  
    meow() {
      console.log("Meow meow!");
    }
  
    introduce() {
      super.introduce();
      console.log(`I'm {this.color} in color.`);
    }
  }
  
  const dog = new Dog("Buddy", "Golden Retriever" 5);
  const cat = new Cat("Whiskers", "Tabby");
  
  dog.introduce();
  dogbark();
  
  cat.introduce();
  cat.meow()  