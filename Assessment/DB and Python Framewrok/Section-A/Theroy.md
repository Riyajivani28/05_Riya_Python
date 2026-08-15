1. Explain the Django Request-Response cycle and how it differs from a standard Python script execution.
-->
In Django, when a user sends a request from the browser, the request first goes to the Django URL configuration. The URL determines which view should handle the request. The view processes the request, interacts with the model/database if needed, and returns a response such as an HTML page.
The basic flow is:
Browser → URL → View → Model/Database → Template → Response → Browser
In a normal Python script, the program generally runs from top to bottom when the file is executed. Django is different because it is a web framework that continuously waits for HTTP requests and processes them using URLs, views, models, and templates.

2. Explain why Django Model Fields (CharField, IntegerField) are more robust for profile data than Python dynamic typing.
-->
Python is dynamically typed, so a variable can store different types of values without explicitly defining its type.
For example:
age = 20
age = "twenty"
Django Model Fields provide structure and validation for database data.
For example:
username = models.CharField(max_length=100)
age = models.IntegerField()
Here, CharField is used for text and IntegerField is used for numbers. Django also creates the appropriate database fields and provides validation.
Therefore, Django Model Fields make profile data more structured, consistent, and suitable for database storage.

3. Explain how Django Forms handle automated input validation for usernames and age ranges.
-->
Django Forms automatically validate user input based on the field definitions.
For example, a CharField can validate text and maximum length, while an IntegerField validates that the entered value is a number.
We can also add custom validation using a method such as:
def clean_age(self):
    age = self.cleaned_data['age']
    if age <= 13:
        raise forms.ValidationError(
            "User must be over 13 years old."
        )
    return age
When we call:
form.is_valid()
Django checks the form data and returns errors if the data is invalid.

4. Explain how to implement conditional logic in Django Templates to toggle account visibility.
-->
Django Template Language provides {% if %} and {% else %} statements for conditional logic.
For example:
{% if profile.is_public %}
    <p>Account is Public</p>
{% else %}
    <p>Account is Private</p>
{% endif %}
If is_public is True, the template displays Public. Otherwise, it displays Private.
This allows us to control what information is displayed to users based on the profile's visibility status.

5. Explain the difference between iterating through a Python list and a Django QuerySet.
-->
A Python list is a collection of objects stored in Python memory.
Example:
users = ["Riya", "Raj", "Amit"]
for user in users:
    print(user)
A Django QuerySet represents a collection of database records.
Example:
profiles = UserProfile.objects.all()
for profile in profiles:
    print(profile.username)
The main difference is that a Python list contains data already stored in memory, while a QuerySet represents data retrieved from the database through Django's ORM.
QuerySets also provide database-related features such as filtering, ordering, and querying.

6. Explain why the Django ORM is preferred over Python dictionaries for persistent profile storage.
-->
A Python dictionary stores data temporarily in memory.
Example:
profile = {
    "username": "Riya",
    "age": 22
}
If the program stops, this data will normally be lost unless it is saved somewhere.
Django ORM stores profile data in a database using Django Models.
Example:
UserProfile.objects.all()
The ORM provides features such as:
Saving data permanently
Retrieving records
Updating records
Deleting records
Filtering database records
Working with relational databases
Therefore, Django ORM is preferred because it provides persistent, structured, and reliable database storage for profile information.