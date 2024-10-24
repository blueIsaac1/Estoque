 document.addEventListener("DOMContentLoaded", function() {
            const loginForm = document.querySelector("form");
            const usernameInput = document.querySelector("input[type='text']");
            const passwordInput = document.querySelector("input[type='password']");
            const loginButton = document.querySelector("button[type='submit']");

            loginForm.addEventListener("submit", function(event) {
                event.preventDefault();
                const username = usernameInput.value;
                const password = passwordInput.value;

                if (username === "" || password === "") {
                    alert("Por favor, preencha todos os campos.");
                }
                // Login de Administrador
                else if (username === "admin" && password === "123456") {
                    alert("Login bem-sucedido como administrador!");
                    window.location.href = "/inicioadmin/"; // Redireciona para a página de admin
                }
                // Login de Fornecedor
                else if (username === "forn" && password === "123456") {
                    alert("Login bem-sucedido como fornecedor!");
                    window.location.href = "/inicioforn/"; // Redireciona para a página do fornecedor
                }
                // Login inválido
                else {
                    alert("Usuário ou senha incorretos.");
                }
            });
        });