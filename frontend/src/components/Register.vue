<template>
  <div class="container-fluid vh-100 d-flex justify-content-center align-items-center">
    <div class="register-form">
      <form class="register-container" style="width: 19rem; max-width: 100%;">

        <div class="mb-4">
          <input type="text" id="name" class="form-control border-custom" placeholder="Nome" />
        </div>

        <div class="mb-4">
          <input type="email" id="email" class="form-control border-custom" placeholder="Email" />
        </div>

        <div class="mb-4 position-relative"> <!-- Adicionei a classe position-relative aqui -->
          <input type="password" id="password" class="form-control border-custom" placeholder="Senha" />
          <i class="fas fa-eye-slash toggle-password" onclick="togglePasswordVisibility('password', this)"></i>
        </div>

        <div class="mb-4 position-relative"> <!-- Adicionei a classe position-relative aqui -->
          <input type="password" id="confirmPassword" class="form-control border-custom" placeholder="Repetir Senha" />
          <i class="fas fa-eye-slash toggle-password" onclick="togglePasswordVisibility('confirmPassword', this)"></i>
        </div>

        <!-- User Type selection -->
        <div class="form-outline mb-4">
          <div class="form-check">
            <input class="form-check-input" type="radio" name="userType" id="client" value="client" checked />
            <label class="form-check-label" for="client">Cliente</label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="radio" name="userType" id="employee" value="employee" />
            <label class="form-check-label" for="employee">Funcionário</label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="radio" name="userType" id="admin" value="admin" />
            <label class="form-check-label" for="admin">Administrador</label>
          </div>
        </div>

        <!-- Submit button -->
        <button type="button" class="btn btn-primary btn-block mb-4">Registrar</button>

        <!-- Register buttons -->
        <div class="text-center">
          <p>Já possui conta? <a href="/login">Entrar</a></p>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    function togglePasswordVisibility(inputId, icon) {
      const passwordInput = document.getElementById(inputId);

      if (passwordInput.type === "password") {
        passwordInput.type = "text";
        icon.classList.remove("fa-eye-slash");
        icon.classList.add("fa-eye");
      } else {
        passwordInput.type = "password";
        icon.classList.remove("fa-eye");
        icon.classList.add("fa-eye-slash");
      }
    }

    // Adiciona a função ao escopo global para que seja acessível no HTML
    window.togglePasswordVisibility = togglePasswordVisibility;
  });
</script>

<style>
.container-fluid {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.register-form {
  height: 100%;
  max-width: 400px;
  margin: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.register-container {
  padding: 1rem;
  border: 1px solid rgba(128, 128, 128, 0.8);
  border-radius: 5px;
  background-color: rgb(243, 243, 243);
}

.border-custom {
  background-color: white;
  border: 1px solid rgba(128, 128, 128, 0.8);
  border-radius: 5px;
  color: rgba(128, 128, 128, 0.8);
}

.border-custom:focus,
.border-custom:valid {
  border: 1px solid rgba(128, 128, 128, 0.8);
}

.border-custom::placeholder {
  color: rgba(128, 128, 128, 0.8);
}

.toggle-password {
  cursor: pointer;
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
}
</style>
