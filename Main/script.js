document.getElementById("signup-form").addEventListener("submit", function (e) {
    e.preventDefault();

    // Get user input
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Create an object to send to the server
    const userData = {
        username: username,
        password: password
    };

    // Send user data to the server (to be implemented in the backend)
    sendDataToServer(userData);
});
