document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('myForm').addEventListener('submit', function (event) {
        var email = document.getElementById('email').value;
        var password = document.getElementById('password').value;
        var subject = document.getElementById('subject').value;
        var body = document.getElementById('body').value;

        if (!email || !password || !subject || !body) {
            alert('All fields are required!');
            event.preventDefault();
        }
    });
});
