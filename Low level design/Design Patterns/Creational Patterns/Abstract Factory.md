# Factory Method Pattern

The Factory Method Pattern is a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created. It helps promote loose coupling between client classes and the classes they instantiate.
# Abstract Factory Pattern

The Abstract Factory Pattern is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. It is useful when there are multiple types of objects that need to be created together.

## Key Concepts
1. **Abstract Factory**: Declares methods for creating abstract products.
2. **Concrete Factory**: Implements the creation methods for specific product families.
3. **Abstract Product**: Defines the interface for a type of product.
4. **Concrete Product**: Implements the Abstract Product interface.

## Advantages
- Ensures consistency among related objects.
- Promotes code reusability and scalability.
- Reduces coupling between client code and concrete classes.

## Example: GUI Factory

### Step 1: Define Abstract Products
```java
public interface Button {
    void render();
}

public interface Checkbox {
    void render();
}
```

### Step 2: Create Concrete Products
```java
public class WindowsButton implements Button {
    @Override
    public void render() {
        System.out.println("Rendering Windows Button");
    }
}

public class MacButton implements Button {
    @Override
    public void render() {
        System.out.println("Rendering Mac Button");
    }
}

public class WindowsCheckbox implements Checkbox {
    @Override
    public void render() {
        System.out.println("Rendering Windows Checkbox");
    }
}

public class MacCheckbox implements Checkbox {
    @Override
    public void render() {
        System.out.println("Rendering Mac Checkbox");
    }
}
```

### Step 3: Define the Abstract Factory
```java
public interface GUIFactory {
    Button createButton();
    Checkbox createCheckbox();
}
```

### Step 4: Implement Concrete Factories
```java
public class WindowsFactory implements GUIFactory {
    @Override
    public Button createButton() {
        return new WindowsButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new WindowsCheckbox();
    }
}

public class MacFactory implements GUIFactory {
    @Override
    public Button createButton() {
        return new MacButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new MacCheckbox();
    }
}
```

### Step 5: Client Code
```java
public class Application {
    private GUIFactory factory;

    public Application(GUIFactory factory) {
        this.factory = factory;
    }

    public void renderUI() {
        Button button = factory.createButton();
        Checkbox checkbox = factory.createCheckbox();
        button.render();
        checkbox.render();
    }

    public static void main(String[] args) {
        GUIFactory windowsFactory = new WindowsFactory();
        Application windowsApp = new Application(windowsFactory);
        windowsApp.renderUI();

        GUIFactory macFactory = new MacFactory();
        Application macApp = new Application(macFactory);
        macApp.renderUI();
    }
}
```

## Output
```
Rendering Windows Button
Rendering Windows Checkbox
Rendering Mac Button
Rendering Mac Checkbox
```

## Summary
The Abstract Factory Pattern is ideal for creating families of related objects. It ensures that the objects created by a factory are compatible and promotes flexibility in switching between different product families.
## Key Concepts
1. **Creator Class**: Defines the factory method that returns an object of a product class.
2. **Product Interface**: Specifies the interface for the objects created by the factory method.
3. **Concrete Product**: Implements the Product interface.
4. **Concrete Creator**: Overrides the factory method to return an instance of a specific Concrete Product.

## Advantages
- Promotes code reusability and flexibility.
- Reduces dependency on specific classes.
- Makes code easier to test and maintain.

## Example: Shape Factory

### Step 1: Define the Product Interface
```java
public interface Shape {
    void draw();
}
```

### Step 2: Create Concrete Products
```java
public class Circle implements Shape {
    @Override
    public void draw() {
        System.out.println("Drawing a Circle");
    }
}

public class Rectangle implements Shape {
    @Override
    public void draw() {
        System.out.println("Drawing a Rectangle");
    }
}
```

### Step 3: Define the Creator Class
```java
public abstract class ShapeFactory {
    public abstract Shape createShape();
}
```

### Step 4: Implement Concrete Creators
```java
public class CircleFactory extends ShapeFactory {
    @Override
    public Shape createShape() {
        return new Circle();
    }
}

public class RectangleFactory extends ShapeFactory {
    @Override
    public Shape createShape() {
        return new Rectangle();
    }
}
```

### Step 5: Client Code
```java
public class Main {
    public static void main(String[] args) {
        ShapeFactory circleFactory = new CircleFactory();
        Shape circle = circleFactory.createShape();
        circle.draw();

        ShapeFactory rectangleFactory = new RectangleFactory();
        Shape rectangle = rectangleFactory.createShape();
        rectangle.draw();
    }
}
```

## Output
```
Drawing a Circle
Drawing a Rectangle
```

## Summary
The Factory Method Pattern allows the creation of objects without specifying their exact class. It delegates the instantiation logic to subclasses, making the code more flexible and extensible.