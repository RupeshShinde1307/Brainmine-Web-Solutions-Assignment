// Add event listener for form submission
document.getElementById('userForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    // Collect form data
    const data = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone_number: document.getElementById('phone').value,
        message: document.getElementById('message').value,
    };

    // Send data to the server
    const response = await fetch('/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    });

    // Get response and show alert to user
    const result = await response.json();
    alert(result.success || result.error);
});
