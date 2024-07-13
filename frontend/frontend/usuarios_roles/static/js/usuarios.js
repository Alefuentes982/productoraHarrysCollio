document.addEventListener('DOMContentLoaded', function () {
    if (document.getElementById('register-form')) {
        document.getElementById('register-form').addEventListener('submit', registerUser);
    }
    if (document.getElementById('login-form')) {
        document.getElementById('login-form').addEventListener('submit', loginUser);
    }
});

function registerUser(event) {
    event.preventDefault();
    const formData = new FormData(document.getElementById('register-form'));
    fetch('http://localhost:9020/usuarios_roles/register/', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Registro exitoso');
                window.location.href = '/login/';
            } else {
                alert('Error en el registro');
            }
        })
        .catch(error => console.error('Error:', error));
}

function loginUser(event) {
    event.preventDefault();
    const formData = new FormData(document.getElementById('login-form'));
    fetch('http://localhost:9020/usuarios_roles/login/', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Login exitoso');
                window.location.href = '/';
            } else {
                alert('Error en el login');
            }
        })
        .catch(error => console.error('Error:', error));
}