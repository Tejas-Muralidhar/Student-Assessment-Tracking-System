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
                newDiv.appendChild(generateStudentMarksContent());
                break;
            case "View Student Attendance":
                newDiv.appendChild(generateStudentAttendanceContent());
                break;
            case "View All Students":
                newDiv.appendChild(generateAllStudentsContent());
                break;
            case "View Subject Details":
                newDiv.appendChild(viewSubjectDetails());
                break;
            case "Add Subject":
                newDiv.appendChild(addSubjectContent());
                break;
            case "Edit Subject":
                newDiv.appendChild(editSubjectContent());
                break;
            case "Delete Subject":
                newDiv.appendChild(deleteSubjectContent());
                break;
            case "View Faculty Details":
                newDiv.appendChild(viewFaculty());
                break;
            case "Assign Faculty to Subject":
                newDiv.appendChild(assignFacultyContent());
                break;
            case "Delete Faculty":
                newDiv.appendChild(deleteFacultyContent());
                break;
            case "View Users":
                newDiv.appendChild(viewUsers());
                break;
            case "Add User":
                newDiv.appendChild(addUserContent());
                break;
            case "Edit User":
                newDiv.appendChild(editUserContent());
                break;
            case "Delete User":
                newDiv.appendChild(deleteUserContent());
                break;
            default:
                newDiv.textContent = "Content for " + linkText;
                break;
        }

        // Return the new div element with the generated content
        return newDiv;
    }

    function generateStudentMarksContent() {
        // Create a new div element
        var newDiv = document.createElement("div");
        newDiv.id = 'ContentDiv';
        var marksData; // Declare marksData here

        // Make an AJAX request to fetch student marks data
        var xhrMarks = new XMLHttpRequest();
        xhrMarks.onreadystatechange = function () {
            if (xhrMarks.readyState === XMLHttpRequest.DONE) {
                if (xhrMarks.status === 200) {
                    marksData = JSON.parse(xhrMarks.responseText); // Assign marksData here
                    // Check if marks data is available
                    if (marksData && marksData.marks && (marksData.marks.theorymarks || marksData.marks.labmarks)) {

                        newDiv.innerHTML = "<p>Filter Your Search: </p>";
                        var filterdiv = document.createElement('div');
                        var columnDropdown = document.createElement("select");
                        columnDropdown.id = "column-dropdown";
                        var defaultOption = document.createElement("option");
                        defaultOption.text = "Select column...";
                        columnDropdown.add(defaultOption);
                        // Get the keys from the first item in marksData.marks.theorymarks array
                        Object.keys(marksData.marks.theorymarks[0]).forEach(function (key) {
                            var option = document.createElement("option");
                            option.text = key;
                            columnDropdown.add(option);
                        });
                        filterdiv.appendChild(columnDropdown);

                        // Create a search input field
                        var searchInput = document.createElement("input");
                        searchInput.type = "text";
                        searchInput.id = "search-input"; // Assign an id to the search input
                        searchInput.placeholder = "Search...";
                        filterdiv.appendChild(searchInput);

                        newDiv.appendChild(filterdiv);

                        // Display theory marks
                        if (marksData.marks.theorymarks && marksData.marks.theorymarks.length > 0) {
                            newDiv.appendChild(createMarksTable(marksData.marks.theorymarks, "Theory Marks"));
                        } else {
                            var p = document.createElement('p');
                            p.innerHTML = "No theory marks available";
                            newDiv.appendChild(p);
                        }
                        // Display lab marks
                        if (marksData.marks.labmarks && marksData.marks.labmarks.length > 0) {
                            newDiv.appendChild(createMarksTable(marksData.marks.labmarks, "Lab Marks"));
                        } else {
                            var p = document.createElement('p');
                            p.innerHTML = "No lab marks available";
                            newDiv.appendChild(p);
                        }

                        // Add event listeners after creating elements
                        columnDropdown.addEventListener("change", filterTable);
                        searchInput.addEventListener("input", filterTable);
                    } else {
                        var p = document.createElement('p');
                        p.innerHTML = "No marks available at the moment";
                        newDiv.appendChild(p);
                    }
                } else {
                    var p = document.createElement('p');
                    p.innerHTML = "Error fetching marks data: " + xhrMarks.statusText;
                    newDiv.appendChild(p);
                }
            }
        };
        // Open the AJAX request to fetch marks data from the view
        xhrMarks.open("GET", "/admin/view-student-marks/", true);
        // Send the AJAX request
        xhrMarks.send();

        // Function to create a table for marks
        function createMarksTable(marks, caption) {
            // Create a new table element
            var table = document.createElement("table");
            // Create table caption
            var tableCaption = document.createElement("caption");
            tableCaption.textContent = caption;
            table.appendChild(tableCaption);
            // Create table header row using <th> instead of <tr>
            var headerRow = document.createElement("tr");
            for (var header in marks[0]) {
                var headerCell = document.createElement("th"); // Create <th> instead of <td>
                headerCell.textContent = header;
                headerRow.appendChild(headerCell);
            }
            table.appendChild(headerRow); // Append the header row to the table

            // Create table body rows
            marks.forEach(function (mark) {
                var row = table.insertRow();
                for (var key in mark) {
                    var cell = row.insertCell();
                    if (mark[key] === null) {
                        cell.textContent = '-';
                    }
                    else {
                        cell.textContent = mark[key];
                    }
                }
            });
            return table;
        }


        function filterTable() {
            // Check if marksData is defined
            if (!marksData) return;
            var selectedColumn = document.getElementById("column-dropdown").value;
            var searchText = document.getElementById("search-input").value.toUpperCase();
            var rows = newDiv.querySelectorAll("table tbody tr");
            rows.forEach(function (row) {
                var cellText = row.querySelector("td:nth-child(" + (Object.keys(marksData.marks.theorymarks[0]).indexOf(selectedColumn) + 1) + ")").textContent.toUpperCase();
                if (selectedColumn === "Select column..." || cellText.includes(searchText)) {
                    row.style.display = "";
                } else {
                    row.style.display = "none";
                }
            });
        }

        // Return the new div element
        return newDiv;
    }





    // Function to generate content for "View Student Attendance"
    function generateStudentAttendanceContent() {
        // Create a new div element
        var newDiv = document.createElement("div");
        newDiv.id = "ContentDiv";
        var attendanceData; // Define attendanceData variable here

        // Make an AJAX request to fetch student attendance data
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    attendanceData = JSON.parse(xhr.responseText); // Assign attendanceData here
                    // Check if attendance data is available
                    if (attendanceData && attendanceData.attendance) {
                        // Create a dropdown to select column name
                        newDiv.innerHTML = "<p>Filter Your Search: </p>";
                        var filterdiv = document.createElement('div');
                        var columnDropdown = document.createElement("select");
                        columnDropdown.id = "column-dropdown";
                        var defaultOption = document.createElement("option");
                        defaultOption.text = "Select column...";
                        columnDropdown.add(defaultOption);
                        Object.keys(attendanceData.attendance[0]).forEach(function (key) {
                            var option = document.createElement("option");
                            option.text = key;
                            columnDropdown.add(option);
                        });
                        columnDropdown.addEventListener("change", filterTable);
                        filterdiv.appendChild(columnDropdown);

                        // Create a search input field
                        var searchInput = document.createElement("input");
                        searchInput.type = "text";
                        searchInput.id = "search-input"; // Assign an id to the search input
                        searchInput.placeholder = "Search...";
                        searchInput.addEventListener("input", filterTable);
                        filterdiv.appendChild(searchInput);

                        newDiv.appendChild(filterdiv);

                        // Create a table element
                        var table = document.createElement("table");
                        // Create table header row
                        var headerRow = document.createElement("tr");
                        for (var header in attendanceData.attendance[0]) {
                            var headerCell = document.createElement("th"); // Create <th> instead of <td>
                            headerCell.textContent = header;
                            headerRow.appendChild(headerCell);
                        }
                        table.appendChild(headerRow); // Append the header row to the table

                        // Create table body rows
                        attendanceData.attendance.forEach(function (attendanceRecord) {
                            var row = table.insertRow();
                            for (var key in attendanceRecord) {
                                var cell = row.insertCell();
                                if (attendanceRecord[key] === null) {
                                    cell.textContent = '-';
                                }
                                else {
                                    cell.textContent = attendanceRecord[key];
                                }
                            }
                        });
                        // Append the table to the new div
                        newDiv.appendChild(table);
                    } else {
                        // If no attendance data available, display a message
                        var p = document.createElement('p');
                        p.innerHTML = "No attendance data available";
                        newDiv.appendChild(p);
                    }
                } else {
                    // If there is an error in fetching attendance data, display an error message
                    var p = document.createElement('p');
                    p.innerHTML = "Error fetching attendance data: " + xhr.statusText;
                    newDiv.appendChild(p);
                }
            }
        };
        // Open the AJAX request to fetch attendance data from the view
        xhr.open("GET", "/admin/view-student-attendance/", true);
        // Send the AJAX request
        xhr.send();

        // Function to handle filtering
        function filterTable() {
            var selectedColumn = document.getElementById("column-dropdown").value;
            var searchText = document.getElementById("search-input").value.toUpperCase();
            var rows = document.querySelectorAll("#main-div table tbody tr");
            rows.forEach(function (row) {
                var cellText = row.querySelector("td:nth-child(" + (Object.keys(attendanceData.attendance[0]).indexOf(selectedColumn) + 1) + ")").textContent.toUpperCase();
                if (selectedColumn === "Select column..." || cellText.includes(searchText)) {
                    row.style.display = "";
                } else {
                    row.style.display = "none";
                }
            });
        }

        // Return the new div element
        return newDiv;
    }

    // Function to generate content for "View All Students"
    // Function to generate content for "View All Students"
    function generateAllStudentsContent() {
        // Create a new div element
        var newDiv = document.createElement("div");
        newDiv.id = 'ContentDiv';
        var studentsData; // Define studentsData variable here

        // Make an AJAX request to fetch all students data
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    studentsData = JSON.parse(xhr.responseText); // Assign studentsData here
                    // Check if students data is available
                    if (studentsData && studentsData.students) {
                        // Create a dropdown to select column name
                        newDiv.innerHTML = "<p>Filter Your Search: </p>";
                        var filterdiv = document.createElement('div');
                        var columnDropdown = document.createElement("select");
                        columnDropdown.id = "column-dropdown";
                        var defaultOption = document.createElement("option");
                        defaultOption.text = "Select column...";
                        columnDropdown.add(defaultOption);
                        Object.keys(studentsData.students[0]).forEach(function (key) {
                            var option = document.createElement("option");
                            option.text = key;
                            columnDropdown.add(option);
                        });
                        columnDropdown.addEventListener("change", filterTable);
                        filterdiv.appendChild(columnDropdown);

                        // Create a search input field
                        var searchInput = document.createElement("input");
                        searchInput.type = "text";
                        searchInput.id = "search-input"; // Assign an id to the search input
                        searchInput.placeholder = "Search...";
                        searchInput.addEventListener("input", filterTable);
                        filterdiv.appendChild(searchInput);

                        newDiv.appendChild(filterdiv);

                        // Create a table element
                        var table = document.createElement("table");

                        var headerRow = document.createElement("tr");
                        for (var header in studentsData.students[0]) {
                            var headerCell = document.createElement("th"); // Create <th> instead of <td>
                            headerCell.textContent = header;
                            headerRow.appendChild(headerCell);
                        }
                        table.appendChild(headerRow); // Append the header row to the table
                        // Create table body rows
                        studentsData.students.forEach(function (student) {
                            var row = table.insertRow();
                            for (var key in student) {
                                var cell = row.insertCell();
                                if (student[key] === null) {
                                    cell.textContent = '-';
                                }
                                else {
                                    cell.textContent = student[key];
                                }
                            }
                        });
                        // Append the table to the new div
                        newDiv.appendChild(table);
                    } else {
                        // If no students data available, display a message
                        var p = document.createElement('p');
                        p.innerHTML = "No Student data available";
                        newDiv.appendChild(p);
                    }
                } else {
                    // If there is an error in fetching students data, display an error message
                    var p = document.createElement('p');
                    p.innerHTML = "Error fetching student data: " + xhr.statusText;
                    newDiv.appendChild(p);
                }
            }
        };
        // Open the AJAX request to fetch students data from the view
        xhr.open("GET", "/admin/view-students/", true);
        // Send the AJAX request
        xhr.send();

        // Function to handle filtering
        function filterTable() {
            var selectedColumn = document.getElementById("column-dropdown").value;
            var searchText = document.getElementById("search-input").value.toUpperCase();
            var rows = document.querySelectorAll("#main-div table tbody tr");
            rows.forEach(function (row) {
                var cellText = row.querySelector("td:nth-child(" + (Object.keys(studentsData.students[0]).indexOf(selectedColumn) + 1) + ")").textContent.toUpperCase();
                if (selectedColumn === "Select column..." || cellText.includes(searchText)) {
                    row.style.display = "";
                } else {
                    row.style.display = "none";
                }
            });
        }

        // Return the new div element
        return newDiv;
    }


    function viewSubjectDetails() {
        // Create a new div element
        var newDiv = document.createElement("div");
        newDiv.id = 'ContentDiv';

        // Make an AJAX request to fetch subject details
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    var subjectsData = JSON.parse(xhr.responseText);
                    // Check if subjects data is available
                    if (subjectsData && subjectsData.marks) {
                        // Display theory subjects
                        if (subjectsData.marks.theorymarks && subjectsData.marks.theorymarks.length > 0) {
                            newDiv.appendChild(createSubjectTable(subjectsData.marks.theorymarks, "Theory Subjects"));
                        } else {
                            var p = document.createElement('p');
                            p.innerHTML = "No theory subject details available";
                            newDiv.appendChild(p);
                        }
                        // Display lab subjects
                        if (subjectsData.marks.labmarks && subjectsData.marks.labmarks.length > 0) {
                            newDiv.appendChild(createSubjectTable(subjectsData.marks.labmarks, "Lab Subjects"));
                        } else {
                            var p = document.createElement('p');
                            p.innerHTML = "No lab subject details available";
                            newDiv.appendChild(p);
                        }
                    } else {
                        var p = document.createElement('p');
                        p.innerHTML = "No subject details available";
                        newDiv.appendChild(p);
                    }
                } else {
                    var p = document.createElement('p');
                    p.innerHTML = "Error fetching subject data: " + xhr.statusText;
                    newDiv.appendChild(p);
                }
            }
        };
        // Open the AJAX request to fetch subjects data from the view
        xhr.open("GET", "/admin/view-subjects/", true);
        // Send the AJAX request
        xhr.send();

        // Function to create a table for subjects
        function createSubjectTable(subjects, caption) {
            // Create a new table element
            var table = document.createElement("table");
            // Create table caption
            var tableCaption = document.createElement("caption");
            tableCaption.textContent = caption;
            table.appendChild(tableCaption);

            var headerRow = document.createElement("tr");
            for (var header in subjects[0]) {
                var headerCell = document.createElement("th"); // Create <th> instead of <td>
                headerCell.textContent = header;
                headerRow.appendChild(headerCell);
            }
            table.appendChild(headerRow); // Append the header row to the table

            // Create table body rows
            subjects.forEach(function (subject) {
                var row = table.insertRow();
                for (var key in subject) {
                    var cell = row.insertCell();
                    if (subject[key] === null) {
                        cell.textContent = '-';
                    } else {
                        cell.textContent = subject[key];
                    }
                }
            });
            return table;
        }

        // Return the new div element
        return newDiv;
    }


    function viewFaculty() {
        // Create a new div element
        var newDiv = document.createElement("div");
        newDiv.id = 'ContentDiv';

        // Make an AJAX request to fetch faculty data
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    var facultyData = JSON.parse(xhr.responseText);
                    // Check if faculty data is available
                    if (facultyData && facultyData.faculty && facultyData.faculty.length > 0) {
                        newDiv.appendChild(createFacultyTable(facultyData.faculty, "Faculty Members"));
                    } else {
                        var p = document.createElement('p');
                        p.innerHTML = "No faculty data available";
                        newDiv.appendChild(p);
                    }
                } else {
                    var p = document.createElement('p');
                    p.innerHTML = "Error fetching faculty data: " + xhr.statusText;
                    newDiv.appendChild(p);
                }
            }
        };
        // Open the AJAX request to fetch faculty data from the view
        xhr.open("GET", "/admin/view-faculty/", true);
        // Send the AJAX request
        xhr.send();

        // Function to create a table for faculty members
        function createFacultyTable(faculty, caption) {
            // Create a new table element
            var table = document.createElement("table");
            // Create table caption
            var tableCaption = document.createElement("caption");
            tableCaption.textContent = caption;
            table.appendChild(tableCaption);

            var headerRow = document.createElement("tr");
            for (var header in faculty[0]) {
                var headerCell = document.createElement("th"); // Create <th> instead of <td>
                headerCell.textContent = header;
                headerRow.appendChild(headerCell);
            }
            table.appendChild(headerRow); // Append the header row to the table

            // Create table body rows
            faculty.forEach(function (member) {
                var row = table.insertRow();
                for (var key in member) {
                    var cell = row.insertCell();
                    if (member[key] === null) {
                        cell.textContent = '-';
                    } else {
                        cell.textContent = member[key];
                    }
                }
            });
            return table;
        }

        // Return the new div element
        return newDiv;
    }

    function viewUsers() {
        // Create a new div element
        var newDiv = document.createElement("div");
        newDiv.id = 'ContentDiv';

        // Make an AJAX request to fetch users data
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    var userData = JSON.parse(xhr.responseText);
                    // Check if users data is available
                    if (userData && userData.users && userData.users.length > 0) {
                        newDiv.appendChild(createUsersTable(userData.users, "Users"));
                    } else {
                        var p = document.createElement('p');
                        p.innerHTML = "No user data available";
                        newDiv.appendChild(p);
                    }
                } else {
                    var p = document.createElement('p');
                    p.innerHTML = "Error fetching user data: " + xhr.statusText;
                    newDiv.appendChild(p);
                }
            }
        };
        // Open the AJAX request to fetch users data from the view
        xhr.open("GET", "/admin/view-users/", true);
        // Send the AJAX request
        xhr.send();

        // Function to create a table for users
        function createUsersTable(users, caption) {
            // Create a new table element
            var table = document.createElement("table");
            // Create table caption
            var tableCaption = document.createElement("caption");
            tableCaption.textContent = caption;
            table.appendChild(tableCaption);

            // Create table header row
            var headerRow = document.createElement("tr");
            for (var header in users[0]) {
                var headerCell = document.createElement("th"); // Create <th> instead of <td>
                headerCell.textContent = header;
                headerRow.appendChild(headerCell);
            }
            table.appendChild(headerRow); // Append the header row to the table

            // Create table body rows
            users.forEach(function (user) {
                var row = table.insertRow();
                for (var key in user) {
                    var cell = row.insertCell();
                    if (user[key] === null) {
                        cell.textContent = '-';
                    } else {
                        cell.textContent = user[key];
                    }
                }
            });
            return table;
        }

        // Return the new div element
        return newDiv;
    }

    function addSubjectContent() {
        // Create a new div element for the content
        var newDiv = document.createElement("div");
        newDiv.id = "ContentDiv";

        // Create a heading
        var heading = document.createElement("h2");
        heading.textContent = "Register New Subject:";
        heading.style.marginBottom = "0";
        var subheading = document.createElement("p");
        subheading.textContent = "Trying to add the data of an already existing subject will lead to editing the Subject details!";
        newDiv.appendChild(heading);
        newDiv.appendChild(subheading);

        // Create a form element
        var form = document.createElement("form");
        form.action = "/admin/add-edit-subject/"; // URL of the backend view
        form.method = "POST"; // HTTP method
        form.style.padding = "20px"; // Padding for the form
        form.style.background = "whitesmoke"; // Background color of the form
        form.style.border = "2px solid #09015f"; // Border color of the form
        form.style.borderRadius = "10px"; // Rounded corners for the form

        // Create labels and inputs for each detail
        var labels = ["Subject Title:", "Subject Code:", "Semester:", "Number of Credits:", "Subject Type:", "Enter Maximum IA Marks:", "Enter Maximum Assignment Marks:", "Enter Maximum Quiz Marks:", "Enter Maximum Observation Marks:", "Enter Maximum Record Marks:", "Enter Maximum Viva Marks:", "Final Internal Marks Split:", "Final External Marks Split:"];
        var inputNames = ["subject_name", "subject_code", "semester", "credits", "lab_or_theory", "MaxIA", "MaxAssignment", "MaxQuiz", "MaxObservation", "MaxRecord", "MaxViva", "MaxInternals", "MaxExternals"];

        for (var i = 0; i < labels.length; i++) {
            var label = document.createElement("label");
            label.textContent = labels[i];
            label.style.display = "block"; // Make label display as block to put each label on a new line

            var input = document.createElement("input");
            input.type = "text";
            input.name = inputNames[i];
            input.required = true;
            input.style.marginBottom = "10px"; // Add some bottom margin to the input fields
            input.style.width = "100%";
            input.style.height = "30px";

            if (i === 0 || i === 1) { // Subject name and Subject code are strings
                input.type = "text";
            } else { // Everything else is a number
                input.type = "number";
                input.min = 0; // Minimum value is 1 for all numbers
                input.required = true;
                if (i === 2) { // Semester: between 1 and 8
                    input.min = 1;
                    input.max = 8;
                } else if (i === 3) { // Credits: above 0
                    input.min = 1;
                }
            }

            if (i === 4) { // If it's the "Subject Type" field
                input = document.createElement("select");
                input.style.width = "100%";
                input.style.height = "40px";
                input.name = inputNames[i];
                input.required = true;
                input.style.marginBottom = "10px"; // Add some bottom margin to the select field

                // Option for Lab
                var labOption = document.createElement("option");
                labOption.value = "0";
                labOption.textContent = "Lab";
                input.appendChild(labOption);

                // Option for Theory
                var theoryOption = document.createElement("option");
                theoryOption.value = "1";
                theoryOption.textContent = "Theory";
                input.appendChild(theoryOption);
            }

            form.appendChild(label);
            form.appendChild(input);
        }

        // Create a submit button
        var submitButton = document.createElement("input");
        submitButton.type = "submit";
        submitButton.value = "Submit";
        submitButton.style.marginTop = "10px"; // Add some top margin to the submit button
        submitButton.style.backgroundColor = "#ff7d20"; // Orange background color
        submitButton.style.color = "white"; // White text color
        submitButton.style.padding = "10px 20px"; // Padding for the button

        form.appendChild(submitButton);

        // Append the form to the content div
        newDiv.appendChild(form);

        return newDiv;
    }


    // Function to generate content for "Edit Subject"
    function editSubjectContent() {
        // Create a new div element for the content
        var newDiv = document.createElement("div");
        newDiv.id = "ContentDiv";

        // Create a heading
        var heading = document.createElement("h2");
        heading.style.marginBottom = "0";
        heading.textContent = "Edit a Registered Subject:";
        var subheading = document.createElement("p");
        subheading.textContent = "Trying to edit the data of a non-existent subject will lead to the creation of a new Subject!";

        newDiv.appendChild(heading);
        newDiv.appendChild(subheading);

        // Create a form element
        var form = document.createElement("form");
        form.action = "/admin/add-edit-subject/"; // URL of the backend view
        form.method = "POST"; // HTTP method
        form.style.padding = "20px"; // Padding for the form
        form.style.background = "whitesmoke"; // Background color of the form
        form.style.border = "2px solid #09015f"; // Border color of the form
        form.style.borderRadius = "10px"; // Rounded corners for the form

        // Create labels and inputs for each detail
        var labels = ["Subject Title:", "Subject Code:", "Semester:", "Number of Credits:", "Subject Type:", "Enter Maximum IA Marks:", "Enter Maximum Assignment Marks:", "Enter Maximum Quiz Marks:", "Enter Maximum Observation Marks:", "Enter Maximum Record Marks:", "Enter Maximum Viva Marks:", "Final Internal Marks Split:", "Final External Marks Split:"];
        var inputNames = ["subject_name", "subject_code", "semester", "credits", "lab_or_theory", "MaxIA", "MaxAssignment", "MaxQuiz", "MaxObservation", "MaxRecord", "MaxViva", "MaxInternals", "MaxExternals"];

        for (var i = 0; i < labels.length; i++) {
            var label = document.createElement("label");
            label.textContent = labels[i];
            label.style.display = "block"; // Make label display as block to put each label on a new line

            var input = document.createElement("input");
            input.type = "text";
            input.name = inputNames[i];
            input.required = true;
            input.style.marginBottom = "10px"; // Add some bottom margin to the input fields
            input.style.width = "100%";
            input.style.height = "30px";

            if (i === 0 || i === 1) { // Subject name and Subject code are strings
                input.type = "text";
            } else { // Everything else is a number
                input.type = "number";
                input.min = 0; // Minimum value is 1 for all numbers
                input.required = true;
                if (i === 2) { // Semester: between 1 and 8
                    input.min = 1;
                    input.max = 8;
                } else if (i === 3) { // Credits: above 0
                    input.min = 1;
                }
            }

            if (i === 4) { // If it's the "Subject Type" field
                input = document.createElement("select");
                input.style.width = "100%";
                input.style.height = "40px";
                input.name = inputNames[i];
                input.required = true;
                input.style.marginBottom = "10px"; // Add some bottom margin to the select field

                // Option for Lab
                var labOption = document.createElement("option");
                labOption.value = "0";
                labOption.textContent = "Lab";
                input.appendChild(labOption);

                // Option for Theory
                var theoryOption = document.createElement("option");
                theoryOption.value = "1";
                theoryOption.textContent = "Theory";
                input.appendChild(theoryOption);
            }

            form.appendChild(label);
            form.appendChild(input);
        }

        // Create a submit button
        var submitButton = document.createElement("input");
        submitButton.type = "submit";
        submitButton.value = "Submit";
        submitButton.style.marginTop = "10px"; // Add some top margin to the submit button
        submitButton.style.backgroundColor = "#ff7d20"; // Orange background color
        submitButton.style.color = "white"; // White text color
        submitButton.style.padding = "10px 20px"; // Padding for the button

        form.appendChild(submitButton);

        // Append the form to the content div
        newDiv.appendChild(form);

        return newDiv;
    }

    // Function to generate content for "Delete Subject"
    function deleteSubjectContent() {
        // Create a new div element
        var newDiv = document.createElement("div");
        newDiv.id = "ContentDiv";

        var heading = document.createElement("h2");
        heading.style.marginBottom = "0";
        heading.textContent = "Delete a Registered Subject:";
        var subheading = document.createElement("p");
        subheading.textContent = "Trying to delete the data of a non-existent subject will not perform any operation!";

        newDiv.appendChild(heading);
        newDiv.appendChild(subheading);

        // Create a form element
        var form = document.createElement("form");
        form.action = "/admin/delete-subject/"; // URL of the backend view
        form.method = "POST"; // HTTP method
        form.style.marginTop = "2%";
        form.style.padding = "20px"; // Padding for the form
        form.style.background = "whitesmoke"; // Background color of the form
        form.style.border = "2px solid #09015f"; // Border color of the form
        form.style.borderRadius = "10px"; // Rounded corners for the form

        // Create a label for input
        var label = document.createElement("label");
        label.textContent = "Enter subject code to delete:";
        label.style.display = "block"; // Make label display as block to put it on a new line
        form.appendChild(label);

        // Create an input field for subject code
        var input = document.createElement("input");
        input.type = "text";
        input.name = "subject_code";
        input.required = true;
        input.style.marginBottom = "10px"; // Add some bottom margin to the input field
        form.appendChild(input);

        // Create a submit button
        var submitButton = document.createElement("input");
        submitButton.type = "submit";
        submitButton.value = "Submit";
        submitButton.style.backgroundColor = "#ff7d20"; // Orange background color
        submitButton.style.color = "white"; // White text color
        submitButton.style.padding = "10px 20px"; // Padding for the button
        form.appendChild(submitButton);

        // Add event listener to the form for confirmation message
        form.addEventListener("submit", function (event) {
            var confirmation = confirm("Are you sure you want to delete this subject?");
            if (!confirmation) {
                event.preventDefault(); // Prevent form submission if user clicks cancel
            }
        });

        // Append the form to the new div
        newDiv.appendChild(form);

        return newDiv;
    }


    // Function to generate content for "Assign Faculty to Subject"
    function assignFacultyContent() {
        // Create a new div element
        var newDiv = document.createElement("div");
        newDiv.id = "ContentDiv";

        var heading = document.createElement("h2");
        heading.style.marginBottom = "0";
        heading.textContent = "Assign a Registered Faculty to a Existing Subject:";
        var subheading = document.createElement("p");
        subheading.textContent = "Trying to enter an invalid Faculty ID or a non existent Subject Code will lead to no action being performed!";

        newDiv.appendChild(heading);
        newDiv.appendChild(subheading);

        // Create a form element
        var form = document.createElement("form");
        form.action = "/admin/map-faculty-subject/"; // URL of the backend view
        form.method = "POST"; // HTTP method
        form.style.padding = "20px"; // Padding for the form
        form.style.background = "whitesmoke"; // Background color of the form
        form.style.border = "2px solid #09015f"; // Border color of the form
        form.style.borderRadius = "10px"; // Rounded corners for the form

        // Create labels and inputs for each detail
        var labels = ["Faculty ID:", "Subject Code:", "Section:", "Semester:"];
        var inputNames = ["faculty_id", "subject_code", "section", "semester"];

        for (var i = 0; i < labels.length; i++) {
            var label = document.createElement("label");
            label.textContent = labels[i];
            label.style.display = "block"; // Make label display as block to put each label on a new line

            var input = document.createElement("input");
            input.style.width = "100%";
            input.style.height = "35px";
            input.type = "text";
            input.name = inputNames[i];
            input.required = true;
            input.style.marginBottom = "10px"; // Add some bottom margin to the input fields

            if (i === 0) { // If it's the "Faculty ID" field
                input.type = "number";
                input.min = 1000;
                input.max = 9999;
            } else if (i === 1) { // If it's the "Subject Code" field
                input.maxLength = 10;
                // Convert input to uppercase
                input.addEventListener('input', function () {
                    this.value = this.value.toUpperCase();
                });
            } else if (i === 2) { // If it's the "Section" field
                input.maxLength = 1;
                // Check if section is a letter
                input.addEventListener('input', function () {
                    var regex = /^[a-zA-Z]$/;
                    if (!regex.test(this.value)) {
                        this.setCustomValidity('Section must be a letter.');
                    } else {
                        this.setCustomValidity('');
                    }
                });
                // Convert input to uppercase
                input.addEventListener('blur', function () {
                    this.value = this.value.toUpperCase();
                });
            } else if (i === 3) { // If it's the "Semester" field
                input.type = "number";
                input.min = 1;
                input.max = 8;
            }

            form.appendChild(label);
            form.appendChild(input);
        }

        // Create a submit button
        var submitButton = document.createElement("input");
        submitButton.type = "submit";
        submitButton.value = "Submit";
        submitButton.style.marginTop = "10px"; // Add some top margin to the submit button
        submitButton.style.backgroundColor = "#ff7d20"; // Orange background color
        submitButton.style.color = "white"; // White text color
        submitButton.style.padding = "10px 20px"; // Padding for the button

        form.appendChild(submitButton);

        // Append the form to the new div
        newDiv.appendChild(form);

        return newDiv;
    }


    // Function to generate content for "Delete Faculty"
    function deleteFacultyContent() {
        // Create a new div element
        var newDiv = document.createElement("div");
        newDiv.id = "ContentDiv";
        newDiv.textContent = "Form to delete faculty";
        return newDiv;
    }

    // Function to generate content for "Add User"
    function addUserContent() {
        // Create a new div element
        var newDiv = document.createElement("div");
        newDiv.id = "ContentDiv";
        newDiv.textContent = "Add user Form";
        return newDiv;
    }

    // Function to generate content for "Edit User"
    function editUserContent() {
        // Create a new div element
        var newDiv = document.createElement("div");
        newDiv.id = "ContentDiv";
        newDiv.textContent = "Form to edit user";
        return newDiv;
    }

    // Function to generate content for "Delete User"
    function deleteUserContent() {
        // Create a new div element
        var newDiv = document.createElement("div");
        newDiv.id = "ContentDiv";
        newDiv.textContent = "Form to delete user";
        return newDiv;
    }
})
