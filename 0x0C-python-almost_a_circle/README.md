<html>
<h1>Project: Python Almost a circle</h1>
<p><strong>In this project we will review Unit testing, how to serialize and deserialize a Class, what is *args and **kwargs and how to handle named arguments in a function.</strong></p>
<body>
<li>Task 0: All your files, classes and methods must be unit tested and be PEP 8 validated.</li>
<li>Task 1: Write the first class Base.</li>
<li>Task 2: Write the class Rectangle that inherits from Base.</li>
<li>Task 3: Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded).</li>
<li>Task 4: Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.</li>
<li>Task 5: Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.</li>
<li>Task 6: Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>.</li>
<li>Task 7: Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y.</li>
<li>Task 8: Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute.</li>
<li>Task 9: Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes.</li>
<li>Task 10: Write the class Square that inherits from Rectangle.</li>
<li>Task 11: Update the class Square by adding the public getter and setter size.</li>
<li>Task 12: Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes.</li>
<li>Task 13: Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle.</li>
<li>Task 14: Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square.</li>
<li>Task 15: Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries.</li>
<li>Task 16: Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file.</li>
<li>Task 17: Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string.</li>
<li>Task 18: Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set.</li>
<li>Task 19: Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances.</li>
</body>
<br>
<br>
<footer>Made by: <strong>Daniel Baquero</stong></footer>
</html>