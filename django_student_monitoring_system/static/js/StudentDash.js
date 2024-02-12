function changeButtonText(button, newText) {
    // Store the original text
    var originalText = button.textContent;
    
    // Change text to new text after 1 second
    button.textContent = newText;

    // Restore original text when mouse leaves the button
    button.onmouseout = function() {
        button.textContent = originalText;
    };
}

