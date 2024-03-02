document.addEventListener("DOMContentLoaded", function () {
    // Select all dropdown links
    var dropdownLinks = document.querySelectorAll(".dropdown-content a");

    // Add click event listener to each dropdown link
    dropdownLinks.forEach(function (link) {
        link.addEventListener("click", function (event) {
            // Prevent the default action of the link
            event.preventDefault();

            // Select the main-div container
            var mainDiv = document.getElementById("main-div");

            // Remove any existing children of main-div
            mainDiv.innerHTML = '';

            // Generate content based on the clicked link
            var content = generateContent(link.textContent);

            // Append the generated content as a child to main-div
            mainDiv.appendChild(content);
        });
    });

    // Function to generate content based on the clicked link
    function generateContent(linkText) {
        // Create a new div element
        var newDiv = document.createElement("div");

        // Generate content based on the link text
        switch (linkText) {
            case "View Student Marks":
                newDiv.textContent = generateStudentMarksContent();
                break;
            case "View Student Attendance":
                newDiv.textContent = "Table to view student attendance";
                break;
            case "View All Students":
                newDiv.textContent = "Table to view all students";
                break;
            case "View Subject Details":
                newDiv.textContent = "Table to view subject details";
                break;
            case "Add Subject":
                newDiv.textContent = "Form to add subject";
                break;
            case "Edit Subject":
                newDiv.textContent = "Form to edit subject";
                break;
            case "Delete Subject":
                newDiv.textContent = "Form to delete subject";
                break;
            case "View Faculty Details":
                newDiv.textContent = "Table to view faculty details";
                break;
            case "Assign Faculty to Subject":
                newDiv.textContent = "Form to assign faculty to subject";
                break;
            case "Add Faculty":
                newDiv.textContent = "Form to add faculty";
                break;
            case "Delete Faculty":
                newDiv.textContent = "Form to delete faculty";
                break;
            case "View Users":
                newDiv.textContent = "Table to view users";
                break;
            case "Add User":
                newDiv.textContent = addNewUserOption();
                break;
            case "Edit User":
                newDiv.textContent = "Form to edit user";
                break;
            case "Delete User":
                newDiv.textContent = "Form to delete user";
                break;
            default:
                newDiv.textContent = "Content for " + linkText;
                break;
        }

        // Return the new div element with the generated content
        return newDiv;
    }

    // Function to generate content for "View Student Marks"
    function generateStudentMarksContent() {
        // Create a new div element
        var newDiv = document.createElement("div");

        // Make an AJAX request to the Django view
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "{% url 'GetStudentMarksWithMax' %}", true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                // Parse the JSON response
                var responseData = JSON.parse(xhr.responseText);

                // Create the filter dropdown
                var filterDropdown = createFilterDropdown(responseData.filters);

                // Create the table and render student marks
                var table = createStudentMarksTable(responseData.studentMarks);

                // Append the filter dropdown and the table to the new div
                newDiv.appendChild(filterDropdown);
                newDiv.appendChild(table);
            }
        };
        xhr.send();

        // Return the new div element
        return newDiv;
    }

    // Function to create the filter dropdown
    function createFilterDropdown(filters) {
        var select = document.createElement("select");
        select.classList.add("filter-dropdown");

        // Add default option
        var defaultOption = document.createElement("option");
        defaultOption.text = "Select Filter";
        defaultOption.disabled = true;
        defaultOption.selected = true;
        select.appendChild(defaultOption);

        // Add filter options
        filters.forEach(function (filter) {
            var option = document.createElement("option");
            option.value = filter.value;
            option.text = filter.text;
            select.appendChild(option);
        });

        return select;
    }

    // Function to create the student marks table
    function createStudentMarksTable(studentMarks) {
        var table = document.createElement("table");

        // Create table headers
        var thead = document.createElement("thead");
        var headerRow = document.createElement("tr");
        Object.keys(studentMarks[0]).forEach(function (key) {
            var th = document.createElement("th");
            th.textContent = key;
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);
        table.appendChild(thead);

        // Create table body
        var tbody = document.createElement("tbody");
        studentMarks.forEach(function (student) {
            var row = document.createElement("tr");
            Object.values(student).forEach(function (value) {
                var td = document.createElement("td");
                td.textContent = value;
                row.appendChild(td);
            });
            tbody.appendChild(row);
        });
        table.appendChild(tbody);

        return table;
    }
});



  
  var newUserButtonsGenerated = false;

  function addNewUserOption() {
    if (!newUserButtonsGenerated) {
        var newUserOptions = document.createElement("div");
        newUserOptions.id = "new-user-buttons"; // Add an ID to the container div
        newUserOptions.innerHTML = `
            <button id="add-student-button" onclick="showNewStudentForm()">Add New Student</button>
            <button id="add-faculty-button" onclick="showNewFacultyForm()">Add New Faculty</button>
        `;
        document.body.appendChild(newUserOptions);
        newUserButtonsGenerated = true; // Set the flag to true indicating buttons are generated
    }
}



    function showNewStudentForm() {
        var studentForm = document.createElement("form");
        // Populate form fields for adding a new student
        studentForm.innerHTML = `
            <label for="usn">USN:</label>
            <input type="text" id="usn" name="usn"><br>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name"><br>
            <!-- Add other fields as needed -->
            <button type="submit">Submit</button>
        `;
        document.getElementById("main-div").appendChild(studentForm);
    }

    function showNewFacultyForm() {
        var facultyForm = document.createElement("form");
        // Populate form fields for adding a new faculty
        facultyForm.innerHTML = `
            <label for="facultyName">Name:</label>
            <input type="text" id="facultyName" name="facultyName"><br>
            <!-- Add other fields as needed -->
            <button type="submit">Submit</button>
        `;
        document.getElementById("main-div").appendChild(facultyForm);
    }

    // // Call addNewUserOption() when the page is loaded
    // window.onload = addNewUserOption;


    function replaceHeroChild(newChild) {
        var hero = document.getElementById('hero');
        var existingChild = hero.firstChild;
    
        if (existingChild) {
            hero.removeChild(existingChild);
        }
    
        hero.appendChild(newChild);
    }



    document.getElementById("add-student-btn").addEventListener("click", function() {
        document.getElementById("add-student-form").style.display = "block";
        // You can generate the form fields dynamically here
    });
    
    // JavaScript to handle showing the form for adding a new user
    document.getElementById("add-user-btn").addEventListener("click", function() {
        addNewUserOption()
    });