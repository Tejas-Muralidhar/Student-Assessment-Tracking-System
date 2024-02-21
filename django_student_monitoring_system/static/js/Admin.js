function replaceHeroChild(newChild) {
    var hero = document.getElementById('hero');

    // Check if hero element exists
    if (!hero) {
        console.error("Hero element not found");
        return; // Exit the function early if hero element is not found
    }

    // Check if hero has any existing child
    if (hero.children.length > 0) {
        var existingChild = hero.children[0];
        hero.removeChild(existingChild); // Remove the existing child
        console.log(hero.childNodes)
    }

    hero.appendChild(newChild); // Append the new child
}


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
    textboxContainer = null;
    if (!textboxContainer) {
        textboxContainer = document.createElement('div');
        textboxContainer.setAttribute('id', 'textboxContainer');
        replaceHeroChild(textboxContainer); 
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
