function replaceHeroChild(newChild) {
    var hero = document.getElementById('hero');
    var existingChild = hero.firstChild; 

    if (existingChild) {
        hero.removeChild(existingChild);
    }

    hero.appendChild(newChild);
}


// function Marks() {

//     var marksDiv = document.createElement("div");
//     marksDiv.setAttribute("id", "marksDiv");
//     marksDiv.textContent = "View Marks";

//     var viewOption = document.createElement("a");
//     viewOption.setAttribute("href", "#");
//     viewOption.textContent = "View Marks";

//     marksDiv.appendChild(viewOption);

//     replaceHeroChild(marksDiv);
// }

// function createDropdownButton() {
//     // Create the button element
//     var dropdownButton = document.createElement("button");
    
//     // Set button attributes
//     dropdownButton.setAttribute("id", "dropdownButton");
//     dropdownButton.textContent = "Dropdown"; // Set button text
    
//     // Create the dropdown content
//     var dropdownContent = document.createElement("div");
//     dropdownContent.setAttribute("id", "dropdownContent");
//     dropdownContent.classList.add("dropdown-content");
    
//     // Add options to the dropdown content
//     var option1 = document.createElement("a");
//     option1.setAttribute("href", "#");
//     option1.textContent = "Option 1";
//     dropdownContent.appendChild(option1);
    
//     var option2 = document.createElement("a");
//     option2.setAttribute("href", "#");
//     option2.textContent = "Option 2";
//     dropdownContent.appendChild(option2);
    
//     // Append the dropdown content to the button
//     dropdownButton.appendChild(dropdownContent);
    
//     // Append the button to the desired container
//     var container = document.getElementById("container"); // Replace "container" with the ID of your desired container
//     container.appendChild(dropdownButton);
// }

// // Call the function to create the dropdown button
// createDropdownButton();




// function Attendance() {

//     var attendanceDiv = document.createElement("div");
//     attendanceDiv.setAttribute("id", "attendanceDiv");

//     var viewOption1 = document.createElement("a");
//     viewOption1.setAttribute("href", "#");
//     viewOption1.textContent = "View Attendance by Semester";

//     var viewOption2 = document.createElement("a");
//     viewOption2.setAttribute("href", "#");
//     viewOption2.textContent = "View Attendance by Section";

//     var viewOption3 = document.createElement("a");
//     viewOption3.setAttribute("href", "#");
//     viewOption3.textContent = "View Attendance by Subject Code";

//     attendanceDiv.appendChild(viewOption1);
//     attendanceDiv.appendChild(viewOption2);
//     attendanceDiv.appendChild(viewOption3);

//     replaceHeroChild(attendanceDiv);
// }

function AddUser()
{
    
    var addUserDiv = document.createElement("div");
    addUserDiv.setAttribute('id','NewUserForm');

    var form = document.createElement("form");

    var emailInput = document.createElement("input");
    emailInput.setAttribute("type", "email");
    emailInput.setAttribute("placeholder", "Email");
    emailInput.setAttribute("name", "email");

    var passwordInput = document.createElement("input");
    passwordInput.setAttribute("type", "password");
    passwordInput.setAttribute("placeholder", "Password");
    passwordInput.setAttribute("name", "password");

    var usernameInput = document.createElement("input");
    usernameInput.setAttribute("type", "text");
    usernameInput.setAttribute("placeholder", "Username");
    usernameInput.setAttribute("name", "username");

    var userTypeKeyInput = document.createElement("input");
    userTypeKeyInput.setAttribute("type", "text");
    userTypeKeyInput.setAttribute("placeholder", "User Type Key");
    userTypeKeyInput.setAttribute("name", "user_type_key");

    var userTypeInput = document.createElement("input");
    userTypeInput.setAttribute("type", "text");
    userTypeInput.setAttribute("placeholder", "User Type");
    userTypeInput.setAttribute("name", "user_type");

    var submitButton = document.createElement("button");
    submitButton.setAttribute("type", "submit");
    submitButton.textContent = "Add User";

    form.appendChild(emailInput);
    form.appendChild(passwordInput);
    form.appendChild(usernameInput);
    form.appendChild(userTypeKeyInput);
    form.appendChild(userTypeInput);
    form.appendChild(submitButton);

    addUserDiv.appendChild(form);

    replaceHeroChild(addUserDiv);
}


var textboxContainer; 

function showTextBox(type) {
    if (!textboxContainer) {
        textboxContainer = document.createElement('div');
        textboxContainer.setAttribute('id', 'textboxContainer');
        document.body.appendChild(textboxContainer); 

        textboxContainer.addEventListener('mousedown', function (event) {
            event.stopPropagation(); 
        });
    }

    textboxContainer.innerHTML = '';

    var inputText = document.createElement('input');
    var submitButton = document.createElement('button');
    submitButton.setAttribute('type', 'submit');
    submitButton.innerText = 'Search';
    inputText.setAttribute('type', 'text');
    inputText.value = ''; 

    switch (type) {
        case 'semester':
            inputText.placeholder = 'Enter Semester (eg. 5)';
            break;
        case 'section':
            inputText.placeholder = 'Enter Section (eg. A)';
            break;
        case 'subject':
            inputText.placeholder = 'Enter Subject Code (eg. 21CSXX)';
            break;
        default:
            inputText.placeholder = 'Enter Value';
    }

    textboxContainer.appendChild(inputText);
    textboxContainer.appendChild(submitButton);

    inputText.focus();
}

function submitValue() {
    var inputValue = document.querySelector('#textboxContainer input[type="text"]').value;
    // Depending on the input value, redirect to appropriate page
    console.log('Submitted value:', inputValue);
    // You can redirect to a new page using window.location.href = 'newpage.html';
}
